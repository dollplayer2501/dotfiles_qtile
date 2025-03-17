#
# Built-in Extensions
#   https://docs.qtile.org/en/latest/manual/ref/extensions.html
#

#
from libqtile import extension
#
from theme_colors import Theme_Colors
#
from modules.variables import font_set


dmenu_setting = {
  'dmenu_bottom': False,
  # 'dmenu_lines': None,
  'dmenu_lines': 45,
  'font': font_set['sub2'],
  'fontsize': 12,

  'dmenu_prompt': '>>',

  'background': Theme_Colors['DarkBlue_default'],
  'foreground': Theme_Colors['LightBlue'],
  # 'selected_background': Theme_Colors['Oreange'],
  'selected_background': Theme_Colors['Purple'],
  'selected_foreground': Theme_Colors['DarkBlue_default']
}


dmenu_normal = extension.DmenuRun(
  **dmenu_setting,
)


dmenu_power = extension.CommandSet(
  commands = {
    'Shutdown': 'systemctl poweroff',
    'Reboot':   'systemctl reboot',

    # TODO: Logout does not work?
    # "Lock": "betterlockscreen -l",
    # "Hibernate": "sudo pm-hibernate",
    # "Suspend": "sudo pm-suspend"
    # "Logout": lazy.shutdown(),
  },

  **dmenu_setting,
)


dmenu_terminal = extension.CommandSet(
  commands = {
    'xfce4-terminal': 'xfce4-terminal',
    'alacritty':      'alacritty',
    'kitty':          'kitty',
    'wezterm':        'wezterm',
    'ghostty':        'ghostty',
  },

  **dmenu_setting,
)


dmenu_window = extension.WindowList(
  **dmenu_setting,
)


##

