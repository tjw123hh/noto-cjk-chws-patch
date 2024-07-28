# noto-cjk-chws-patch
仅保留了 noto-cjk-chws 的标点部分（不是 fork 是因为那样文件太大了），让它更容易下载（并且可以将英文夹在这个字体和 noto-fonts-cjk 之间自定义英文字体而不影响全角引号），但是需要自己在 fontconfig 中设置。

保留的标点：‘“〈《「『【〔〖〘〚〝（［｛｟（［‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—

可在`subsetter.py`中设置。

字体版本同原字体。

字体改名以避免与原字体重复。字体命名规则如下：

- 有空格：在原字体基础上，在“CJK”之后添加“ CHWS Patch”，如果没有则添加在“Sans”/“Serif”之后。如：
    - Noto Sans CJK SC -> Noto Sans CJK CHWS Patch SC
    - Noto Sans SC -> Noto Sans CHWS Patch SC
- 无空格：在原字体基础上，在“CJK”之后添加“ChwsPatch”，如果没有则添加在“Sans”/“Serif”之后。如：
    - NotoSansCJKsc-Regular -> NotoSansCJKChwsPatchsc-Regular

# noto-cjk-chws
使用 [chws_tool](https://github.com/googlefonts/chws_tool) 添加了 OpenType chws/vchw 特性（标点挤压）的 Noto CJK 字体。
使用这些特性可以从字体层面实现标点挤压，如果有自己喜欢的字体也可以用 [chws_tool](https://github.com/googlefonts/chws_tool) 试试。

原仓库虽然有为了符合 Google Fonts 要求而添加 chws/vchw 的字体（`google-fonts` 目录下），但不全。这里没有更改字体名是因为我没有对字体作任何其他更改，它可以完全替代原本的 Noto Sans CJK 字体。

[测试说明](https://github.com/googlefonts/chws_tool#visual-test)

# Noto CJK fonts

Download individual fonts from the download guides for [Noto Sans CJK](https://github.com/googlefonts/noto-cjk/tree/main/Sans#downloading-noto-sans-cjk) or [Noto Serif CJK](https://github.com/googlefonts/noto-cjk/tree/main/Serif#downloading-noto-serif-cjk) or look in [Releases](https://github.com/googlefonts/noto-cjk/releases)

Release notes and version history are documented separately for [Sans](https://github.com/googlefonts/noto-cjk/blob/main/Sans/NEWS.md#noto-sans-cjk-release-notes) and [Serif](https://github.com/googlefonts/noto-cjk/blob/main/Serif/NEWS.md#noto-serif-cjk-release-notes)

Noto CJK fonts are also available on [Google Fonts](https://fonts.google.com/noto/fonts) but under different names than in this repository. The two letter code here is replaced at Google Fonts as follows:

- *JP* -> *Japanese*
- *KR* -> *Korean*
- *SC* -> *Simplified Chinese*
- *TC* -> *Traditional Chinese*
- *HK* -> *Hong Kong*
