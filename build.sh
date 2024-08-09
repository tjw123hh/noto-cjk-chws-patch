#!/usr/bin/bash

unzip Sans/SuperOTC/NotoSansCJK.ttc.zip -d Sans/SuperOTC/
rm Sans/SuperOTC/NotoSansCJK.ttc.zip
unzip Serif/SuperOTC/NotoSerifCJK.ttc.zip -d Serif/SuperOTC/
rm Serif/SuperOTC/NotoSerifCJK.ttc.zip
# 原仓库由于字体文件非常大，使用zip压缩了，这里可以直接提供

process_font() {
    font_path="$1"
    echo "Processing font: $font_path"
    add-chws -o "$(dirname $font_path)" "$font_path"
    python subsetter.py "$font_path"
}

export -f process_font

# fonttools打不开*.woff2

find . -type f \( -iname "*.ttf" -o -iname "*.ttc" -o -iname "*.otf" \) -exec bash -c '
    for file do
        process_font "$file"
    done
' bash {} +

echo "删除源文件？[Y/n]"
read answer
if [ "$answer" = "Y" ] || [ "$answer" = "y" ]; then
    find . -type f \( -iname "*.ttf" -o -iname "*.ttc" -o -iname "*.otf" \) ! -iname "*Chws*" -exec rm -f {} +
    rm android/*.woff2
fi

# zip -m Sans/SuperOTC/NotoSansCJK.ttc.zip Sans/SuperOTC/NotoSansCJK.ttc
# zip -m Serif/SuperOTC/NotoSerifCJK.ttc.zip Serif/SuperOTC/NotoSerifCJK.ttc
