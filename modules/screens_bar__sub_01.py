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
#
from qtile_extras import widget
# from libqtile import widget
#
from modules.variables import (
  font_set,
  custom_icon_path,
)
from modules.screens_bar___common import (
  common_powerline,
  common_config_screen,
  common_config_bar,
)
#
from theme_colors import Theme_Colors


screen_sub_01 = Screen(
  #
  # NOTE: Multiple monitor
  # TODO: I want to manage the same settings separately.
  #

  **common_config_screen,

  bottom = bar.Bar(
    [
      ## ------------------------------------

      # widget.CurrentLayout(
      #   padding = 0,
      #   fontsize = 16,
      #   font = font_set['sub2'],
      #   # custom_icon_paths = custom_icon_path,
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

      ## ------------------------------------

      widget.GroupBox(
        visible_groups = ['7', '8'],

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
        background = Theme_Colors['DarkBlue_lighten'],

        **common_powerline,
      ),

      widget.WindowTabs(
        fontsize = 18,
        font = font_set['sub1'],

        markup = True,
        selected = ('<u>', '</u>'),
        padding = 0,

        foreground = Theme_Colors['LightBlue'],
        background = Theme_Colors['DarkBlue_default'],
      ),
    ],
    24,
    **common_config_bar,
  ),
)


##

