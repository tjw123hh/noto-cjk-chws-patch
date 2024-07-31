#!/bin/bash

# Until Sans and Serif are split into two repos on https://github.com/notofonts
# we have everything in this single repo https://github.com/tjw123hh/noto-cjk-chws-patch
# This script will make a new release for Sans. To do a Serif release use gh-release-noto-cjk-serif.sh
# Requires GitHub CLI (https://github.com/cli/cli/releases)

VERSION=2.004
PKGVER=20240731
PKGREL=1

echo "Download individual assets from below or through the download [guide](https://github.com/tjw123hh/noto-cjk-chws-patch/tree/main/Sans#downloading-noto-sans-cjk)." > Sans/git-release-notes.md

cd Sans
zip -j -r -v 00_NotoSansCJKChwsPatch.ttc.zip SuperOTC/NotoSansCJKChwsPatch.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 01_NotoSansCJKChwsPatch-OTF-VF.zip Variable/OTF Variable/OTC/NotoSansCJKChwsPatch-VF.otf.ttc Variable/OTC/NotoSansMonoCJKChwsPatch-VF.otf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 02_NotoSansCJKChwsPatch-TTF-VF.zip Variable/TTF Variable/OTC/NotoSansCJKChwsPatch-VF.ttf.ttc Variable/OTC/NotoSansMonoCJKChwsPatch-VF.ttf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 03_NotoSansCJKChwsPatch-OTC.zip OTC LICENSE --exclude "*.zip" "*.DS_Store" "OTC/NotoSansCJKChwsPatch.ttc"
zip -r -v 04_NotoSansCJKChwsPatch-OTF.zip OTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 05_NotoSansCJKChwsPatch-SubsetOTF.zip SubsetOTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 06_NotoSansCJKChwsPatchjp.zip OTF/Japanese LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 07_NotoSansCJKChwsPatchkr.zip OTF/Korean LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 08_NotoSansCJKChwsPatchsc.zip OTF/SimplifiedChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 09_NotoSansCJKChwsPatchtc.zip OTF/TraditionalChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 10_NotoSansCJKChwsPatchhk.zip OTF/TraditionalChineseHK LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 11_NotoSansMonoCJKChwsPatchjp.zip Mono/NotoSansMonoCJKChwsPatchjp* LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 12_NotoSansMonoCJKChwsPatchkr.zip Mono/NotoSansMonoCJKChwsPatchkr* LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 13_NotoSansMonoCJKChwsPatchsc.zip Mono/NotoSansMonoCJKChwsPatchsc* LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 14_NotoSansMonoCJKChwsPatchtc.zip Mono/NotoSansMonoCJKChwsPatchtc* LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 15_NotoSansMonoCJKChwsPatchhk.zip Mono/NotoSansMonoCJKChwsPatchhk* LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 16_NotoSansChwsPatchJP.zip SubsetOTF/JP LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 17_NotoSansChwsPatchKR.zip SubsetOTF/KR LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 18_NotoSansChwsPatchSC.zip SubsetOTF/SC LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 19_NotoSansChwsPatchTC.zip SubsetOTF/TC LICENSE --exclude "*.zip" "*.DS_Store"
zip -j -r -v 20_NotoSansChwsPatchHK.zip SubsetOTF/HK LICENSE --exclude "*.zip" "*.DS_Store"

gh release create Sans${PKGVER}-${PKGREL} --title "Noto Sans CJK Version ${VERSION} (OTF, OTC, Super OTC, Subset OTF, Variable OTF/TTF)" -F git-release-notes.md --target main \
        '00_NotoSansCJKChwsPatch.ttc.zip#Static Super OTC' \
        '01_NotoSansCJKChwsPatch-OTF-VF.zip#All Variable OTF/OTC' \
        '01_NotoSansCJKChwsPatch-OTF-VF.zip#All Variable OTF/OTC' \
        '02_NotoSansCJKChwsPatch-TTF-VF.zip#All Variable TTF/OTC' \
        '03_NotoSansCJKChwsPatch-OTC.zip#All Static Language Specific OTCs' \
        '04_NotoSansCJKChwsPatch-OTF.zip#All Static Language Specific OTFs' \
        '05_NotoSansCJKChwsPatch-SubsetOTF.zip#All Static Region Specific Subset OTFs' \
        '06_NotoSansCJKChwsPatchjp.zip#Language Specific OTFs Japanese (日本語)' \
        '07_NotoSansCJKChwsPatchkr.zip#Language Specific OTFs Korean (한국어)' \
        '08_NotoSansCJKChwsPatchsc.zip#Language Specific OTFs Simplified Chinese (简体中文)' \
        '09_NotoSansCJKChwsPatchtc.zip#Language Specific OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '10_NotoSansCJKChwsPatchhk.zip#Language Specific OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '11_NotoSansMonoCJKChwsPatchjp.zip#Language Specific Monospace OTFs Japanese (日本語)' \
        '12_NotoSansMonoCJKChwsPatchkr.zip#Language Specific Monospace OTFs Korean (한국어)' \
        '13_NotoSansMonoCJKChwsPatchsc.zip#Language Specific Monospace OTFs Simplified Chinese (简体中文)' \
        '14_NotoSansMonoCJKChwsPatchtc.zip#Language Specific Monospace OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '15_NotoSansMonoCJKChwsPatchhk.zip#Language Specific Monospace OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '16_NotoSansChwsPatchJP.zip#Region Specific Subset OTFs Japanese (日本語)' \
        '17_NotoSansChwsPatchKR.zip#Region Specific Subset OTFs Korean (한국어)' \
        '18_NotoSansChwsPatchSC.zip#Region Specific Subset OTFs Simplified Chinese (简体中文)' \
        '19_NotoSansChwsPatchTC.zip#Region Specific Subset OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '20_NotoSansChwsPatchHK.zip#Region Specific Subset OTFs Traditional Chinese — Hong Kong (繁體中文—香港)'

rm *.zip
rm git-release-notes.md
cd ..
