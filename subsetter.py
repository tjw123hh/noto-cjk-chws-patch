#!/usr/bin/env python3

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter
import sys

subsetter = Subsetter()
subsetter.options.name_IDs = "*"         # 保留所有 nameID
# 只有保留所有 nameID（默认只保留 nameID 1~6）才能使 fontconfig 正确识别子集化后的字体，因为 Noto CJK 在 nameID=16/17（排版字族名/样式名）存储正确的字族与样式（如 Black、DemiLight、Light 等），nameID=1/2（基本的字族名/样式名）只能存储基本的 Regular、Bold 变体名。（见 https://learn.microsoft.com/en-us/typography/opentype/spec/name#name-ids。）
subsetter.options.name_languages = "*"   # 保留所有语言
# 保留所有语言的记录（默认只保留英文），但实际上名称都是英文的，主要是想让 fontconfig 正确识别字体的语言⸺实际上 fontconfig 还是会识别成英文，但还是先留着比较好（
subsetter.populate(text="‘“〈《「『【〔〖〘〚〝（［｛｟（［·‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—…")

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
    for i in range(len(li)):
        li[i] = namer(li[i])

def dict_namer(di):
    for k in di:
        di[k] = namer(di[k])

def modify(font):
    subsetter.subset(font)

    for record in font['name'].names:
        record.string = namer(record.string)

    if "CFF " in font.keys():
        cff = font["CFF "].cff
        list_namer(cff.strings.strings)
        list_namer(cff.fontNames)
        for dic in cff:
            dict_namer(dic.rawDict)

path = sys.argv[1]

if path.endswith("ttc"):
    ttc = TTCollection(path)
    for font in ttc:
        modify(font)
    ttc.save(namer(path))
else:
    font = TTFont(path)
    modify(font)
    font.save(namer(path))
