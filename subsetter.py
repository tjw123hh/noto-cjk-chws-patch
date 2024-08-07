#!/usr/bin/env python3

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter
import sys

subsetter = Subsetter()
subsetter.populate(text="‘“〈《「『【〔〖〘〚〝（［｛｟（［·‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—")

def namer(arg):
    if type(arg) == bytes:
        return namer(arg.decode("utf-16-be")).encode("utf-16-be")
    if type(arg) == str:
        if " " in arg:
            if "CHWS Patch" in arg:
                return arg
            if "Noto Sans CJK" in arg:
                return arg.replace("Noto Sans CJK", "Noto Sans CJK CHWS Patch")
            if "Noto Sans Mono CJK" in arg:
                return arg.replace("Noto Sans Mono CJK", "Noto Sans Mono CJK CHWS Patch")
            if "Noto Serif CJK" in arg:
                return arg.replace("Noto Serif CJK", "Noto Serif CJK CHWS Patch")
            if "Noto Sans" in arg:
                return arg.replace("Noto Sans", "Noto Sans CHWS Patch")
            if "Noto Sans Mono" in arg:
                return arg.replace("Noto Sans Mono", "Noto Sans Mono CHWS Patch")
            return arg.replace("Noto Serif", "Noto Serif CHWS Patch")
        if "ChwsPatch" in arg:
            return arg
        if "NotoSansCJK" in arg:
            return arg.replace("NotoSansCJK", "NotoSansCJKChwsPatch")
        if "NotoSansMonoCJK" in arg:
            return arg.replace("NotoSansMonoCJK", "NotoSansMonoCJKChwsPatch")
        if "NotoSerifCJK" in arg:
            return arg.replace("NotoSerifCJK", "NotoSerifCJKChwsPatch")
        if "NotoSans" in arg:
            return arg.replace("NotoSans", "NotoSansChwsPatch")
        if "NotoSansMono" in arg:
            return arg.replace("NotoSansMono", "NotoSansMonoChwsPatch")
        return arg.replace("NotoSerif", "NotoSerifChwsPatch")
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
