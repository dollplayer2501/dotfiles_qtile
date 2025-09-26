"""
Built-in Widgets
================

Common widget settings are written here.
"""

from qtile_extras.widget.decorations import PowerLineDecoration
# from qtile_extras.resources import wallpapers
#
from modules.variables import default_wallpaper
#
from theme_colors import Theme_Colors


# widget_defaults = dict(
#   font = "sans",
#   fontsize = 12,
#   padding = 3,
#   # background = Theme_Colors['DarkBlue_default'],
# )
# extension_defaults = widget_defaults.copy()


# Widget Decorations — qtile-extras
#  https://qtile-extras.readthedocs.io/en/stable/manual/how_to/decorations.html
#
common_powerline = {
  'decorations': [
    PowerLineDecoration(
      path = 'forward_slash',
    )
  ]
}


common_config_screen = {
  'wallpaper': default_wallpaper,
  # 'wallpaper': wallpapers.WALLPAPER_TILES,
  'wallpaper_mode': 'fill',
}


common_config_bar = {
  'border_width': [1, 0, 1, 0],
  'border_color': [Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange'], Theme_Colors['Oreange']],
  'margin': [0, 0, 0, 0],
  'opacity': 0.90,
}


# from modules.MyWidget import Uptime
#
# def get_uptime():
# #  return os.popen('uptime -p').read().strip()
#   return os.popen("awk '{print $1}' /proc/uptime | awk '{print int($1)}'").read().strip()

# awk '{print $1}' /proc/uptime | awk '{print int($1)}'


##
