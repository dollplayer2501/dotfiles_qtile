#
#
#

import os
from datetime import datetime
#
from libqtile.utils import guess_terminal


mod1 = 'mod1' # Alt
mod4 = 'mod4' # Windows key

terminal_guess = guess_terminal() # Xcfe4-terminai
terminal_gpu = 'wezterm'

terminal_main = 'kitty'
terminal_sub1 = 'alacritty'
terminal_sub8 = 'wezterm'
terminal_sub9 = 'xfce4-terminal'


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

