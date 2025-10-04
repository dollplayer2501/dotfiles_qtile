# Other Information

This is not directly related to Qtile settings, but it is about the scripts that support the Qtile environment.  
Anything not covered here is documented separately.


<!-- ###################################################################### -->
## GPU load display

I'm using `widget.GenPollText` and issuing `"amdgpu_top -n 1 -J | jq '.devices[0].gpu_activity.GFX.value'"`.


<!-- ###################################################################### -->
## Japanese Imperial Calendar

I'm a Japanese person living in Japan. I rarely use the Japanese calendar in my daily life, but when I need to, I can't remember the Japanese calendar and it's very inconvenient.  
For this reason, I set the `format` of `widget.Clock` to the following:

```
format = '%Y' + '/R' + str(current_gengou_reiwa) + '-%m-%d %a %H:%M',
```

The contents of the `current_gengou_reiwa` function are written below in [`./modules/variables.py`](../modules/variables.py).

```
current_gengou_reiwa = int(current_date_time.strftime('%Y')) - 2018
```

In other words, it only supports Reiwa. There's no need to go back in time, but if the era name changes in the future, you'll need to support it.


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

See [Modification of `gen-keybinding-img`](./08_01-gen-keybinding-img.md).


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
