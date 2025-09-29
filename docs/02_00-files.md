# File Structure

Normally, Qtile's configuration consists of a single file at `.config/qtile/config.py`, but I have split it into multiple files.  
Originally, I referred to the community edition of EndeavourOS as a guide.

The general structure is as follows:

```
~/.config/qtile/
 ├─ docs/
 ├─ icons/                  # Images used in Qtile
 │   ├─ layout-*.png
 │   └─ svgrepo-com-*.svg
 ├─ keybind-map/            # Output destination of `./scripts/gen-keybinding-img`
 │   └─ *.png
 ├─ modules/                # The actual configurations
 │   └─ *.py
 ├─ scripts/
 │   ├─ autostart.sh
 │   ├─ gen-keybinding-img
 │   └─ shutdown.sh
 └─ config.py               # Qtile's configuration file,
                            # the actual configurations are `modules/*.py`
```


<!-- -->
