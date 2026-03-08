#!/usr/bin/env python3
from fontTools.subset import Subsetter
from east_asian_spacing.builder import Builder
from east_asian_spacing.font import Font
from east_asian_spacing.config import Config
from copy import deepcopy
import sys
import asyncio

tran = {
    "Noto Sans CJK": "Noto Sans CJK CHWS Patch",
    "Noto Sans Mono CJK": "Noto Sans Mono CJK CHWS Patch",
    "Noto Serif CJK": "Noto Serif CJK CHWS Patch",
    "Noto Sans": "Noto Sans CHWS Patch",
    "Noto Sans Mono": "Noto Sans Mono CHWS Patch",
    "Noto Serif": "Noto Serif CHWS Patch",
    "NotoSansCJK": "NotoSansCJKChwsPatch",
    "NotoSansMonoCJK": "NotoSansMonoCJKChwsPatch",
    "NotoSerifCJK": "NotoSerifCJKChwsPatch",
    "NotoSans": "NotoSansChwsPatch",
    "NotoSansMono": "NotoSansMonoChwsPatch",
    "NotoSerif": "NotoSerifChwsPatch"
    }

base_subsetter = Subsetter()
base_subsetter.options.name_IDs = "*"         # 保留所有 nameID
# 只有保留所有 nameID（默认只保留 nameID 1~6）才能使 fontconfig 正确识别子集化后的字体，因为 Noto CJK 在 nameID=16/17（排版字族名/样式名）存储正确的字族与样式（如 Black、DemiLight、Light 等），nameID=1/2（基本的字族名/样式名）只能存储基本的 Regular、Bold 变体名。（见 https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids。）
base_subsetter.options.name_languages = "*"   # 保留所有语言
# 保留所有语言的记录（默认只保留英文），但实际上名称都是英文的，主要是想让 fontconfig 正确识别字体的语言⸺实际上 fontconfig 还是会识别成英文，但还是先留着比较好（
base_subsetter.options.ignore_missing_glyphs = True

def namer(arg):
    if type(arg) == bytes:
        return namer(arg.decode("utf-16-be")).encode("utf-16-be")
    if type(arg) == str:
        for before in tran:
            if tran[before] in arg:
                return arg
            elif before in arg:
                return arg.replace(before, tran[before])
    return arg

def list_namer(li):
    for i, v in enumerate(li):
        li[i] = namer(v)

def dict_namer(di):
    for k, v in di.items():
        di[k] = namer(v)

async def change_name(font):
    for record in font['name'].names:
        record.string = namer(record.string)

    if "CFF " in font.keys():
        cff = font["CFF "].cff
        list_namer(cff.strings.strings)
        list_namer(cff.fontNames)
        for dic in cff:
            dict_namer(dic.rawDict)

async def get_glyphs_from_gpos(ttfont):
    gpos = ttfont["GPOS"].table
    indices = {
        idx
        for fr in gpos.FeatureList.FeatureRecord
        if fr.FeatureTag in ("chws", "vchw")
        for idx in fr.Feature.LookupListIndex
    }
    glyphs = set()
    for idx in indices:
        for sub in gpos.LookupList.Lookup[idx].SubTable:
            if hasattr(sub, "Coverage"):
                glyphs.update(sub.Coverage.glyphs)
            if hasattr(sub, "PairSet"):
                for ps in sub.PairSet:
                    for pvr in ps.PairValueRecord:
                        glyphs.add(pvr.SecondGlyph)
            if hasattr(sub, "ClassDef1"):
                glyphs.update(sub.ClassDef1.classDefs)
                glyphs.update(sub.ClassDef2.classDefs)
    return glyphs

async def subset(ttfont, **kwargs):
    s = deepcopy(base_subsetter)
    s.populate(**kwargs)
    s.subset(ttfont)

async def update_lookup_count(ttfont):
    # builder.build() 追加了新 lookup 但未更新 LookupCount，
    # 导致 subset_lookups 用旧值过滤时把新增的 chws lookup 全部丢弃。
    ll = ttfont["GPOS"].table.LookupList
    ll.LookupCount = len(ll.Lookup)

async def modify_collection(font_collection, path):
    config = Config.for_collection(font_collection)
    builder = Builder(font_collection, config)
    await builder.build()
    if builder.has_spacings:
        all_changed_ttfonts = set()
        for spacing in builder._spacings:
            gids = spacing.horizontal.glyph_id_set | spacing.vertical.glyph_id_set
            changed_ttfonts = {font.ttfont for font in spacing.changed_fonts}
            all_changed_ttfonts |= changed_ttfonts
            for ttfont in changed_ttfonts:
                await update_lookup_count(ttfont)
                await subset(ttfont, gids=gids, text="—⸺…⋯")
                await change_name(ttfont)
        for i, ttfont in list(enumerate(font_collection.ttfonts))[::-1]:
            if ttfont not in all_changed_ttfonts:
                del font_collection.ttfonts[i]
    else:
        glyphs_by_offset = {}
        for i, ttfont in list(enumerate(font_collection.ttfonts))[::-1]:
            reader_offset = ttfont.reader.tables.get("GPOS").offset
            # If the font does not have `GPOS`, `reader_offset` is `None`.
            if reader_offset is None:
                del font_collection.ttfonts[i]
                continue

            glyphs = glyphs_by_offset.get(reader_offset)
            if glyphs is None:
                glyphs = await get_glyphs_from_gpos(ttfont)
                glyphs_by_offset[reader_offset] = glyphs

            if not glyphs:
                del font_collection.ttfonts[i]
                continue

            await subset(ttfont, glyphs=glyphs, text="—⸺…⋯")
            await change_name(ttfont)

    if any(font_collection.ttfonts):
        new_path = namer(path)
        print(f"Saving to: {new_path}")
        font_collection.ttcollection.save(namer(path))
    else:
        print("Skipped because not applicable")

async def modify(path):
    print(f"Processing font: {path}")
    font = Font.load(path)
    if font.is_collection:
        return await modify_collection(font, path)

    config = Config.default
    builder = Builder(font, config)
    await builder.build()
    ttfont = font.ttfont
    if builder.has_spacings:
        spacing = builder._spacings[0]
        gids = spacing.horizontal.glyph_id_set | spacing.vertical.glyph_id_set
        await update_lookup_count(ttfont)
        await subset(ttfont, gids=gids)
    else:
        if not (glyphs := await get_glyphs_from_gpos(ttfont)):
            print("Skipped because not applicable")
            return
        await subset(ttfont, glyphs=glyphs, text="—⸺…⋯")

    await change_name(ttfont)
    new_path = namer(path)
    print(f"Saving to: {new_path}")
    font.ttfont.save(new_path)

async def main():
    sem = asyncio.Semaphore(4)  # 同时最多 4 个

    async def limited(path):
        async with sem:
            await modify(path)

    coros = (limited(path) for path in sys.argv[1:])
    await asyncio.gather(*coros)

if __name__ == "__main__":
    asyncio.run(main())
