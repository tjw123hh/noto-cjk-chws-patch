#!/usr/bin/bash
shopt -s globstar

unzip Sans/SuperOTC/NotoSansCJK.ttc.zip -d Sans/SuperOTC/
rm Sans/SuperOTC/NotoSansCJK.ttc.zip
unzip Serif/SuperOTC/NotoSerifCJK.ttc.zip -d Serif/SuperOTC/
rm Serif/SuperOTC/NotoSerifCJK.ttc.zip
rm Serif/SuperOTC/LICENSE
# 原仓库由于字体文件非常大，使用zip压缩了，这里可以直接提供

find . -type f \( -iname "*.ttf" -o -iname "*.ttc" -o -iname "*.otf" \) ! -iname "*Chws*" -exec python subsetter.py {} +

printf "删除源文件？[Y/n]"
read answer
if [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
    find . -type f \( -iname "*.ttf" -o -iname "*.ttc" -o -iname "*.otf" -o -iname "*.woff2" \) ! -iname "*Chws*" -exec rm -f {} +
fi

printf "删除空目录？[Y/n]"
read answer
if [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
    find . -type d -empty -delete
fi
