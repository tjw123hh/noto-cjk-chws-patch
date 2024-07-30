# noto-cjk-chws-patch
仅保留了 noto-cjk-chws 更改的标点部分与“—”（不是 fork 是因为那样文件太大了），让它更容易下载（并且可以将英文夹在这个字体和 noto-fonts-cjk 之间自定义英文字体而不影响全角引号），但是需要自己在 fontconfig 中设置。可通过 AUR 包`noto-fonts-cjk-chws-patch`直接在 Arch Linux 上安装。

保留的标点：‘“〈《「『【〔〖〘〚〝（［｛｟（［·‧・；：’”〉》」』】〕〗〙〛〞〟）］｝｠、。，．！？）］—

可在`subsetter.py`中设置。

- 为什么加入“—”？
    - 不加的话如果夹入英文字体（见[#使用方式](#使用方式)），破折号的连字会消失（但其实 [W3C《中文排版需求》草稿](https://w3c.github.io/clreq/)推荐使用`U+2E3A TWO-EM DASH`\[⸺\]）。且由于 Qt 的 Bug（推测是将第一次 fontconfig 匹配到的第一个字体重新给 fontconfig 进行匹配获取字体列表），如果不加入“—”，且将该字体作为`serif`或`sans-serif`的第一个字体，会使`serif`或`sans-serif`在 Qt 程序中使用等宽字体。另外它由于 Bug 而非常细（notofonts/noto-cjk#236）。

字体版本同原字体。

字体改名以避免与原字体重复。字体命名规则如下：

- 有空格：在原字体基础上，在“CJK”之后添加“ CHWS Patch”，如果没有则添加在“Sans”/“Serif”之后。如：
    - Noto Sans CJK SC -> Noto Sans CJK CHWS Patch SC
    - Noto Sans SC -> Noto Sans CHWS Patch SC
- 无空格：在原字体基础上，在“CJK”之后添加“ChwsPatch”，如果没有则添加在“Sans”/“Serif”之后。如：
    - NotoSansCJKsc-Regular -> NotoSansCJKChwsPatchsc-Regular

## 使用方式

在 fontconfig 中，将其置于原字体（`Noto Sans`或`Noto Serif`）之前。
可以在原字体与该字体之间夹入英文字体（或是其他字体），实现更改英文字体的同时保留一些与英文标点共用码位的中文标点（如““”“””）。（缺点是显示斜体时倾斜程度可能不同，但中文一般不用斜体。）

如果需要默认开启标点挤压特性，可在 fontconfig 配置中设置`fontfeatures`字段（Qt 尚未支持，参见[QTBUG-78645](https://bugreports.qt.io/browse/QTBUG-78645)）。

示例（`~/.config/fontconfig/fonts.conf`，`<fontconfig>`元素中）：
```xml
    <match target="font">
        <test name="family" compare="contains">
            <string>CHWS Patch</string>
        </test>
        <edit binding="strong" name="fontfeatures">
            <string>chws</string>
            <string>vchw</string>
        </edit>
    </match>
```

# noto-cjk-chws
使用 [chws_tool](https://github.com/googlefonts/chws_tool) 添加了 OpenType chws/vchw 特性（标点挤压）的 Noto CJK 字体。
使用这些特性可以从字体层面实现标点挤压，如果有自己喜欢的字体也可以用 [chws_tool](https://github.com/googlefonts/chws_tool) 试试。

原仓库虽然有为了符合 Google Fonts 要求而添加 `chws`/`vchw` 的字体（`google-fonts` 目录下），但不全。这里没有更改字体名是因为我没有对字体作任何其他更改，它可以完全替代原本的 Noto Sans CJK 字体。

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
