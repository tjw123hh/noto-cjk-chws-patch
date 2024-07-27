#!/bin/bash

# Until Sans and Serif are split into two repos on https://github.com/notofonts
# we have everything in this single repo https://github.com/tjw123hh/noto-cjk-chws
# This script will make a new release for Serif. To do a Sans release use gh-release-noto-cjk-sans.sh
# Requires GitHub CLI (https://github.com/cli/cli/releases)

VERSION=2.002

echo "Download individual assets from below or through the download [guide](https://github.com/tjw123hh/noto-cjk-chws/tree/main/Serif#downloading-noto-serif-cjk)." > Serif/git-release-notes.md

cd Serif
zip -j -r -v 01_NotoSerifCJKChwsPatch.ttc.zip SuperOTC/NotoSerifCJKChwsPatch.ttc --exclude "*.zip" "*.DS_Store"
zip -r -v 02_NotoSerifCJKChwsPatch-OTF-VF.zip Variable/OTF Variable/OTC/NotoSerifCJKChwsPatch-VF.otf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 03_NotoSerifCJKChwsPatch-TTF-VF.zip Variable/TTF Variable/OTC/NotoSerifCJKChwsPatch-VF.ttf.ttc LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 04_NotoSerifCJKChwsPatchOTC.zip OTC LICENSE --exclude "*.zip" "*.DS_Store" "OTC/NotoSerifCJKChwsPatch.ttc"
zip -r -v 05_NotoSerifCJKChwsPatchOTF.zip OTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 06_NotoSerifCJKChwsPatchSubsetOTF.zip SubsetOTF LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 07_NotoSerifCJKChwsPatchjp.zip OTF/Japanese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 08_NotoSerifCJKChwsPatchkr.zip OTF/Korean LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 09_NotoSerifCJKChwsPatchsc.zip OTF/SimplifiedChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 10_NotoSerifCJKChwsPatchtc.zip OTF/TraditionalChinese LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 11_NotoSerifCJKChwsPatchhk.zip OTF/TraditionalChineseHK LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 12_NotoSerifChwsPatchJP.zip SubsetOTF/JP LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 13_NotoSerifChwsPatchKR.zip SubsetOTF/KR LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 14_NotoSerifChwsPatchSC.zip SubsetOTF/SC LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 15_NotoSerifChwsPatchTC.zip SubsetOTF/TC LICENSE --exclude "*.zip" "*.DS_Store"
zip -r -v 16_NotoSerifChwsPatchHK.zip SubsetOTF/HK LICENSE --exclude "*.zip" "*.DS_Store"

gh release create Serif${VERSION}_CHWS_Patch --title "Noto Serif CJK CHWS Patch Version ${VERSION} (OTF, OTC, Super OTC, Subset OTF, Variable OTF/TTF)" -F git-release-notes.md --target main \
        '01_NotoSerifCJKChwsPatch.ttc.zip#Static Super OTC' \
        '02_NotoSerifCJKChwsPatch-OTF-VF.zip#All Variable OTF/OTC' \
        '03_NotoSerifCJKChwsPatch-TTF-VF.zip#All Variable TTF/OTC' \
        '04_NotoSerifCJKChwsPatchOTC.zip#All Static Language Specific OTCs' \
        '05_NotoSerifCJKChwsPatchOTF.zip#All Static Language Specific OTFs' \
        '06_NotoSerifCJKChwsPatchSubsetOTF.zip#All Static Region Specific Subset OTFs' \
        '07_NotoSerifCJKChwsPatchjp.zip#Language Specific OTFs Japanese (日本語)' \
        '08_NotoSerifCJKChwsPatchkr.zip#Language Specific OTFs Korean (한국어)' \
        '09_NotoSerifCJKChwsPatchsc.zip#Language Specific OTFs Simplified Chinese (简体中文)' \
        '10_NotoSerifCJKChwsPatchtc.zip#Language Specific OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '11_NotoSerifCJKChwsPatchhk.zip#Language Specific OTFs Traditional Chinese — Hong Kong (繁體中文—香港)' \
        '12_NotoSerifChwsPatchJP.zip#Region Specific Subset OTFs Japanese (日本語)' \
        '13_NotoSerifChwsPatchKR.zip#Region Specific Subset OTFs Korean (한국어)' \
        '14_NotoSerifChwsPatchSC.zip#Region Specific Subset OTFs Simplified Chinese (简体中文)' \
        '15_NotoSerifChwsPatchTC.zip#Region Specific Subset OTFs Traditional Chinese — Taiwan (繁體中文—臺灣)' \
        '16_NotoSerifChwsPatchHK.zip#Region Specific Subset OTFs Traditional Chinese — Hong Kong (繁體中文—香港)'

rm *.zip
rm git-release-notes.md
cd ..
