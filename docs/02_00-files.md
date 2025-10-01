# File Structure

Normally, Qtile configuration is configured in a single file at `~/.config/qtile/config.py`, but I split it into multiple files. This was inspired by the community edition of Qtile on EndeavourOS. (The current version is not split.)

The general structure is as follows:

```
~/.config/qtile/
 ├─ docs/                      # This document
 ├─ icons/                     # Images used in Qtile
 │   ├─ layout-*.png
 │   └─ svgrepo-com-*.svg
 ├─ keybind-map/               # Output destination of `./scripts/gen-keybinding-img`
 │   └─ *.png
 ├─ modules/                   # The actual configurations
 │   └─ *.py
 ├─ scripts/
 │   ├─ autostart.sh
 │   ├─ gen-keybinding-img
 │   ├─ gen-keybinding-img.sh  # `./scripts/gen-keybinding-img` startup script
 │   └─ shutdown.sh
 └─ config.py                  # Qtile's configuration file,
                               # the actual configurations are `modules/*.py`
```


<!-- -->
