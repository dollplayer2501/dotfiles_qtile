#!/usr/bin/sh

rm -f ~/.config/qtile/keybind-map/*.png
python3 ~/.config/qtile/scripts/gen-keybinding-img --config ~/.config/qtile/config.py --output-dir ~/.config/qtile/keybind-map/
