#!/usr/bin/env python3

from fontTools.ttLib import TTFont, TTCollection
from fontTools.subset import Subsetter, Options
import sys

subsetter = Subsetter()
subsetter.populate(text="‘“〈《「『【〔〖〘〚〝（［｛｟（［‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—")

def namer(arg):
    if type(arg) == bytes:
        if " ".encode("utf-16-be") in arg:
            if "CHWS Patch".encode("utf-16-be") in arg:
                return arg
            if "Noto Sans CJK".encode("utf-16-be") in arg:
                return arg.replace("Noto Sans CJK".encode("utf-16-be"), "Noto Sans CJK CHWS Patch".encode("utf-16-be"))
            if "Noto Serif CJK".encode("utf-16-be") in arg:
                return arg.replace("Noto Serif CJK".encode("utf-16-be"), "Noto Serif CJK CHWS Patch".encode("utf-16-be"))
            if "Noto Sans".encode("utf-16-be") in arg:
                return arg.replace("Noto Sans".encode("utf-16-be"), "Noto Sans CHWS Patch".encode("utf-16-be"))
            return arg.replace("Noto Serif".encode("utf-16-be"), "Noto Serif CHWS Patch".encode("utf-16-be"))
        if "ChwsPatch".encode("utf-16-be") in arg:
            return arg
        if "NotoSansCJK".encode("utf-16-be") in arg:
            return arg.replace("NotoSansCJK".encode("utf-16-be"), "NotoSansCJKChwsPatch".encode("utf-16-be"))
        if "NotoSerifCJK".encode("utf-16-be") in arg:
            return arg.replace("NotoSerifCJK".encode("utf-16-be"), "NotoSerifCJKChwsPatch".encode("utf-16-be"))
        if "NotoSans".encode("utf-16-be") in arg:
            return arg.replace("NotoSans".encode("utf-16-be"), "NotoSansChwsPatch".encode("utf-16-be"))
        return arg.replace("NotoSerif".encode("utf-16-be"), "NotoSerifChwsPatch".encode("utf-16-be"))
    if type(arg) == str:
        if " " in arg:
            if "CHWS Patch" in arg:
                return arg
            if "Noto Sans CJK" in arg:
                return arg.replace("Noto Sans CJK", "Noto Sans CJK CHWS Patch")
            if "Noto Serif CJK" in arg:
                return arg.replace("Noto Serif CJK", "Noto Serif CJK CHWS Patch")
            if "Noto Sans" in arg:
                return arg.replace("Noto Sans", "Noto Sans CHWS Patch")
            return arg.replace("Noto Serif", "Noto Serif CHWS Patch")
        if "ChwsPatch" in arg:
            return arg
        if "NotoSansCJK" in arg:
            return arg.replace("NotoSansCJK", "NotoSansCJKChwsPatch")
        if "NotoSerifCJK" in arg:
            return arg.replace("NotoSerifCJK", "NotoSerifCJKChwsPatch")
        if "NotoSans" in arg:
            return arg.replace("NotoSans", "NotoSansChwsPatch")
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
