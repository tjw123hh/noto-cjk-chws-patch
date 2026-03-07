from fontTools.ttLib import TTCollection

ttc = TTCollection("/media/programming/projects/noto-cjk-chws-patch/Sans/OTC/NotoSansCJKChwsPatch-Regular.ttc")
font = ttc.fonts[0]

gpos = font["GPOS"].table
print("lookup 总数:", len(gpos.LookupList.Lookup))
print("chws lookup indices:", )
for rec in gpos.FeatureList.FeatureRecord:
    if rec.FeatureTag == "chws":
        print(" ", rec.Feature.LookupListIndex)
