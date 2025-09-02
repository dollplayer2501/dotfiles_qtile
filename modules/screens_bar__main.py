#
# Built-in Widgets — Qtile 0.30.1.dev1+gfecc37d documentation
#  https://docs.qtile.org/en/latest/manual/ref/widgets.html#
#
# qtile-extras documentation
#  https://qtile-extras.readthedocs.io/en/stable/
#

#
from libqtile import bar, qtile
from libqtile.config import Screen
from libqtile.lazy import lazy
#
from qtile_extras import widget
# from libqtile import widget
#
from modules.variables import (
  font_set,
  current_gengou_reiwa,
  custom_icon_path,
)
from modules.screens_bar___common import (
  common_powerline,
  common_config_screen,
  common_config_bar,
)
from modules.popup import show_power_menu
#
from theme_colors import Theme_Colors


screen_main = Screen(
  **common_config_screen,

  bottom = bar.Bar(
    [
      ## ------------------------------------

      widget.Prompt(
        fontsize = 20,
        font = font_set['sub2'],

        cursor_color = Theme_Colors['Oreange'],
        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      ## ------------------------------------

      # widget.CurrentLayout(
      #   padding = 0,
      #   fontsize = 16,
      #   font = font_set['sub2'],
        # custom_icon_paths = custom_icon_path,
      #   foreground = Theme_Colors['Oreange'],
      #   background = Theme_Colors['DarkBlue_default'],
      # ),

      widget.CurrentLayoutIcon(
        padding = 4,
        scale = 0.8,

        custom_icon_paths = custom_icon_path,
        foreground = Theme_Colors['Debug'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      # Uptime(),

      widget.GroupBox(
        visible_groups = ['1', '2', '3', '4', '5', '9'],

        fontsize = 18,
        font = font_set['main'],

        margin = 0,
        margin_x = 0,
        margin_y = 4,

        active = Theme_Colors['LightBlue'],
        block_highlight_text_color = Theme_Colors['Oreange'],
        borderwidth = 0,

        inactive = Theme_Colors['Purple'],
        foreground = Theme_Colors['Debug'],
        background = Theme_Colors['DarkBlue_default'],

        **common_powerline,
      ),

      ## ------------------------------------

      # widget.WindowName(
      #   fontsize = 18,
      #   font = font_set['sub1'],
      #   foreground = Theme_Colors['LightBlue'],
      #   empty_group_string = '＼(^o^)／',
      #   padding = 0,
      #   background = Theme_Colors['DarkBlue_lighten'],
      #   **common_powerline,
      # ),

      widget.WindowTabs(
        fontsize = 18,
        font = font_set['sub1'],

        markup = True,
        selected = ('<u>', '</u>'),
        padding = 0,

        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_lighten'],

        **common_powerline,
      ),

      # INFO: Getting errors when moving across workspaces in application?
      # widget.TaskList(
      #   fontsize = 16,
      #   font = font_set['sub1'],
      #   borderwidth = 1,
      #   margin = 0,
      #   margin_x = 2,
      #   margin_y = 0,
      #   padding = 0,
      #   padding_x = 2,
      #   padding_y = 0,
      #   icon_size = 18,
      #   unfocused_border = 'None',
      #   urgent_alert_method = 'border',
      #   border = Theme_Colors['Purple'],
      #   urgent_border = Theme_Colors['Oreange'],
      #   foreground = Theme_Colors['LightBlue'],
      #   background = Theme_Colors['DarkBlue_lighten'],
      #   **common_powerline,
      # ),

      ## ------------------------------------

      # TODO: When Cmus is not launched,
      #  the width is set to zero and the page is not displayed.
      # widget.Cmus(
      #   fontsize = 16,
      #   font = font_set['main'],
      #   scroll = True,
      #   scroll_fixed_width = True,
      #   width = 50,
      #   playing_color = Theme_Colors['LightBlue'],
      #   stopped_color = Theme_Colors['Oreange'],
      #   background = Theme_Colors['DarkBlue_default'],
      #   **common_powerline,
      # ),

      widget.CPU(
        format = 'CPU: {load_percent}%',
        # format = 'CPU: {freq_current}GHz {load_percent}%',

        padding = 4,
        fontsize = 18,
        font = font_set['main'],

        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      # INFO: need `python-psutil`
      # widget.ThermalSensor(
      #   format = '{temp:.1f}{unit}',
      #   fontsize = 22,
      #   font = font_set['sub2'],
      #   foreground = Theme_Colors['LightBlue'],
      #   background = Theme_Colors['DarkBlue_default'],
      # ),

      widget.ThermalZone(
        high = 31,
        crit = 41,

        format = '{temp}°C',
        format_crit = '{temp}°C!!',
        # format_crit = '{temp}°C CRIT!',

        padding = 4,
        fontsize = 16,
        font = font_set['main'],

        fgcolor_normal = Theme_Colors['LightBlue'],
        fgcolor_high = Theme_Colors['Oreange'],
        fgcolor_crit = Theme_Colors['Red'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      widget.Memory(
        format = 'Mem: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
        # format = 'Mem: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm} Swap: {SwapUsed:.0f}{ms}/{SwapTotal:.0f}{ms}',
        measure_mem = 'G',
        # measure_swap = 'G',

        padding = 4,
        fontsize = 16,
        font = font_set['main'],

        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      # widget.HDD(
      #   format = 'HDD: {HDDPercent}%',
      #   device = 'nvme0n1',
      #   fontsize = 16,
      #   font = font_set['sub2'],
      #   foreground = Theme_Colors['LightBlue'],
      #   background = Theme_Colors['DarkBlue_default'],
      # ),

      widget.CheckUpdates(
        display_format = 'Upd: {updates}',
        distro = 'Arch_checkupdates',
        update_interval = 600,
        no_update_string = 'NoUpd',
        initial_text = 'Now checking',

        padding = 4,
        fontsize = 16,
        font = font_set['main'],

        foreground = Theme_Colors['LightBlue'], # this is initial?
        colour_have_updates = Theme_Colors['LightBlue'],
        colour_no_updates = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      widget.Volume(
        emoji = False,

        fmt = 'Vol:{}',
        mute_format = 'Mute',

        padding = 4,
        fontsize = 16,
        font = font_set['main'],

        mouse_callbacks = {
          # Button1 is mute on/off
          'Button3': lambda: qtile.cmd_spawn('pavucontrol'),
        },

        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),

      # widget.TextBox(
      #   text=get_uptime(),
      #   update_interval=60,  # 60秒ごとに更新
      # ),

      # INFO: NB Systray is incompatible with Wayland, consider using StatusNotifier instead
      # widget.StatusNotifier(),

      # widget.Net(
      #   # format = 'Net:{down:6.2f}{down_suffix:<2}↓{up:6.2f}{up_suffix:<2}↑',
      #   format = 'Net: {down:.2f}{down_suffix}/{up:.2f}{up_suffix}',
      #   prefix = 'M',
      #   fontsize = 22,
      #   font = font_set['sub2'],
      #   foreground = Theme_Colors['LightBlue'],
      #   background = Theme_Colors['DarkBlue_default'],
      # ),

      ## ------------------------------------

      widget.Clock(
        format = '%Y' + '/R' + str(current_gengou_reiwa) + '-%m-%d %a %H:%M',

        padding = 10,
        fontsize = 22,
        font = font_set['main'],

        foreground = Theme_Colors['Oreange'],
        background = Theme_Colors['DarkBlue_default'],

        **common_powerline,
      ),

      ## ------------------------------------

      widget.Systray(
        icon_size = 14,
        padding = 2,

        background = Theme_Colors['DarkBlue_lighten'],
      ),

      # widget.Bluetooth(),

      # widget.BatteryIcon(
      #   scale = 1.4,
      #   padding = 0,
      #   background = Theme_Colors['DarkBlue_lighten'],
      # ),

      ## ------------------------------------

      widget.TextBox(
        fmt = '  ',
        fontsize = 18,
        font = font_set['main'],
        padding = 0,
        mouse_callbacks = {
          'Button1': lazy.function(show_power_menu),
        },
        foreground = Theme_Colors['Purple'],
        background = Theme_Colors['DarkBlue_lighten'],
      ),

      # widget.QuickExit(
        # default_text = '[logoff]',
      #   default_text = '  ',
      #   countdown_start = 3,
      #   countdown_format='{}',
      #   fontsize = 18,
      #   font = font_set['main'],
      #   foreground = Theme_Colors['Purple'],
      #   background = Theme_Colors['DarkBlue_lighten'],
      # ),

      # INFO: WARNING libqtile __init__.py:import_class():L108 Unmet dependencies for 'qtile_extras.widget.syncthing.Syncthing': No module named 'dbus_fast'
      # widget.Syncthing(
      #   api_key = 'tSfbt9mM6doJgs2R25A66H6ay2gdFkrN',
      #   server = 'http://127.0.0.1:8384/',
      #   server = 'http://localhost:8384',
      #   background = Theme_Colors['DarkBlue_lighten'],
      #   hide_on_idle = False,
      #   show_bar = True,
      # ),

      # INFO: WARNING libqtile __init__.py:import_class():L108 Unmet dependencies for 'qtile_extras.widget.statusnotifier.StatusNotifier': No module named 'dbus_next'
      # need `python-pyxdg` and `python-dbus-next`, not `python-dbus-fast`
      # widget.StatusNotifier(
      #   background = Theme_Colors['DarkBlue_lighten'],
      # ),

      # INFO: WARNING libqtile __init__.py:import_class():L108 Unmet dependencies for 'libqtile.widget.wlan.Wlan': No module named 'iwlib'
      # widget.Wlan(),

      # INFO: try!
      # widget.Bluetooth(),
    ],

    24,
    **common_config_bar,
  ),
  # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
  # By default we handle these events delayed to already improve performance, however your system might still be struggling
  # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
  # x11_drag_polling_rate = 60,
)


##

