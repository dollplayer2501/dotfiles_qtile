# Other Information

This is not directly related to Qtile settings, but it is about the scripts that support the Qtile environment.


<!-- ###################################################################### -->
## `./scripts/screenshot_to_closeup_bar.sh`

```
cd ~/.config/qtile
sh ./scripts/screenshot_to_closeup_bar.sh ~/Picture/EndeavourOS_Qtile_yyyy-mm-dd_hh-nn-ss.png
sh ./scripts/screenshot_to_closeup_bar.sh ~/Picture/EndeavourOS_Qtile_yyyy-mm-dd_hh-nn-ss.png true
```

Use ImageMagick to extract only the widget bar area of ​​the screenshot image (in my case, the bottom part) and create an image.  
If you specify `true` as the second argument, the reduced full screen will also be concatenated.  
The output file name is fixed to `_EndeavourOS_Qtile_yyyy-mm-dd_hh-nn-ss_short.png` or `_EndeavourOS_Qtile_yyyy-mm-dd_hh-nn-ss_full.png` (when the second argument is set to `true`).


<!-- ###################################################################### -->
## `./scripts/gen-keybinding-img`、`./script/gen-keybinding-img.sh`

See [Modification of `gen-keybinding-img`](./05_01-gen-keybinding-img.md).


<!-- ###################################################################### -->
## `./scripts/create_ToC.py`

```
cd ~/.config/qtile
python3 ./scripts/create_ToC.py
```

A script to generate the ToC (Table of contents) for `./README.md` and `./doc/README.md`.


<!-- ###################################################################### -->
## `./scripts/convert_color_layout_icons.sh`

```
cd ~/.config/qtile
sh ./scripts/convert_color_layout_icons.sh
```

ImageMagick is used to change the color of the icon files in `/usr/lib/python3.13/site-packages/libqtile/resources/layout-icons/*.png` and output them to `./.config/qtile/icons/`.


<!-- -->
