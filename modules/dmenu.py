#
# Built-in Extensions
#   https://docs.qtile.org/en/latest/manual/ref/extensions.html
#

#
from libqtile import extension
from libqtile.lazy import lazy
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
    # NOTE: see i3-wm of EndeavourOS
    'Systemctl:Shutdown':    'systemctl poweroff',
    'Systemctl:Reboot':      'systemctl reboot',
    'Systemctl:Suspend':     'systemctl suspend',
    'Systemctl:Hibernate':   'systemctl hibernate',
    # NOTE: After the introduction of Xfce4, this system
    'Xfce4:Screensaver':     'xfce4-screensaver-command -l',
    'Xfce4:Lock':            'xfce4-screensaver-command -l',
    #
    'Qtile:Reboot':          lazy.reload_config(),
    # NOTE: Implementing logout from LightDM is difficult for me
    # Therefore, `lazy.shutdown()` is the de facto logout?
    'Qtile:Shutdown/logout': lazy.shutdown(),
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

