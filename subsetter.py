#!/usr/bin/env python3

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter
import sys

subsetter = Subsetter()
subsetter.populate(text="‘“〈《「『【〔〖〘〚〝（［｛｟（［·‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—")

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
            dic.FamilyName = namer(dic.FamilyName)
            dic.FullName = namer(dic.FullName)


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
