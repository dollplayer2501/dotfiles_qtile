# Other information

Qtileとは直接関係ないが、Qtile環境を支えているスクリプトに関して。


## スクリーンショットの撮影

`scrot`を使っている。
現状、Fishシェルの関数にしているため（私のFishシェルのドットファイルは非公開）、その件に関して。
一部、複数画面と被るが、メインはコチラで。


## `./script/convert_color_layout_icons.sh`

ImageMagickを使い、`/usr/lib/python3.13/site-packages/libqtile/resources/layout-icons/*.png`のアイコンファイルの色を変更して、`./.config/qtile/icons/`に出力している。


## `./script/screenshot_to_closeup_bar.sh`

ImageMagickを使い、スクリーンショット画像のウィジェットバーの範囲のみ（私の場合は下部）、抽出して画像を作成する。


## `./script/gen-keybinding-img`、`./script/gen-keybinding-img.sh`

[Modification of `gen-keybinding-img`](./05_01-gen-keybinding-img.md)


## `./script/create_ToC.py`

`./README.md`や`./doc/README.md`のToC、Table of contentsを生成するスクリプト。




