#
# Built-in Layouts
#   https://docs.qtile.org/en/stable/manual/ref/layouts.html
#

#
from libqtile import layout
#
from modules.variables import font_set
#
from theme_colors import Theme_Colors


layouts = [

  layout.Max(
    border_width = 0,
    margin = [0, 0, 0, 0],

    only_focused = True,

    border_focus = Theme_Colors['Oreange'],
    border_normal = Theme_Colors['Purple'],
  ),

  layout.VerticalTile(
    border_width = 1,
    margin = [1, 10, 1, 100],

    single_border_width = 1,
    single_margin = [1, 1, 2, 500],

    border_focus = Theme_Colors['Oreange'],
    border_normal = Theme_Colors['Purple'],
  ),

  layout.TreeTab(
    level_shitf = 5,
    margin_left = 5,
    margin_y = 50,
    fontsize = 18,
    font = font_set['main'],

    sections = ['TreeTab', 'I dont understand'],
    section_fg = '#7f3fbf',
    section_fontsize = 18,
    border_width = 10,

    panel_width = 450,
    bg_color = '#08052b80',

    active_bg = '#7f3fbfc0',
    active_fg = '#ff7f7f',

    inactive_bg = '#08052ba0',
    inactive_fg = '#7fbaff',

    urgent_bg = Theme_Colors['Debug'],
    urgent_fg = Theme_Colors['Debug'],
  ),

  # layout.Columns(
  #   border_width = 1,
  #   margin = [1, 1, 1, 1],

  #   border_on_single = True,
  #   margin_on_single = [1, 1, 2, 500],

  #   initial_ratio = 0.6,

  #   border_focus = Theme_Colors['Oreange'],
  #   border_focus_stack = Theme_Colors['Debug'],
  #   border_normal = Theme_Colors['LightBlue'],
  #   border_normal_stack = Theme_Colors['Debug'], 
  # ),

  # layout.Tile(
  #   border_width = 1,
  #   border_focus = Theme_Colors['Oreange'],
  #   border_normal = Theme_Colors['LightBlue'],
  #   margin = [1, 1, 1, 1],
  #   add_after_last = True,
  #   add_on_top = False,
  #   border_on_single = False,
  #   expand = True,
  #   ratio = 0.4,
  #   shift_windows = True,
  #   master_length = 1,
  # ),


  # layout.Bsp(),
  # layout.Columns(),
  # layout.Floating(),
  # layout.Matrix(),
  # layout.Max(),
  # layout.MonadTall(),
  # layout.MonadThreeCol(),
  # layout.MonadWide(),
  # layout.Plasma(),
  # layout.RatioTile(),
  # layout.ScreenSplit(),
  # layout.Slice(),
  # layout.Spiral(),
  # layout.Stack(),
  # layout.Tile(),
  # layout.TreeTab(),
  # layout.VerticalTile(),
  # layout.Zoomy(),
]


##

