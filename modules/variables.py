#
#
#

import os
from datetime import datetime
#
# from libqtile.utils import guess_terminal


MOD4 = 'mod4' # Windows key, Super
ALT = 'mod1'
CONTROL = 'control'
SHIFT = 'shift'
TAB = 'Tab'
SPACE = 'space'
RETURN = 'Return'

UP = 'Up'
DOWN = 'Down'
LEFT = 'Left'
RIGHT = 'Right'


autostart_sh = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
shutdown_sh = os.path.expanduser('~/.config/qtile/scripts/shutdown.sh')

default_wallpaper = '/usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png'

font_set = {
  # 'main': 'Raleway Thin',
  'main': 'Raleway Light',
  'sub1': 'Noto Sans CJK JP Thin',
  'sub2': 'CaskaydiaMono NFM Light',
}

current_date_time = datetime.now()
current_gengou_reiwa = int(current_date_time.strftime('%Y')) - 2018

custom_icon_path = [
  os.path.expanduser('~/.config/qtile/icons')
]


##

