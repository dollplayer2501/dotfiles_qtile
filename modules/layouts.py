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
    # TODO: Setting margin/padding width when in staircase state
    active_bg = ''.join([ Theme_Colors['Purple'], '88' ]),
    active_fg = ''.join([ Theme_Colors['Oreange'] ]),
    bg_color = ''.join([ Theme_Colors['DarkBlue_default'], 'dd' ]),
    border_width = 5,
    font = font_set['sub1'],
    fontshadow = None,
    fontsize = 18,
    inactive_bg = ''.join([ Theme_Colors['DarkBlue_lighten'], 'ee' ]),
    inactive_fg = ''.join([ Theme_Colors['LightBlue'] ]),
    level_shitf = 0,
    margin_left = 0,
    margin_y = 0,
    padding_left = 10,
    padding_x = 0,
    padding_y = 0,
    panel_width = 450,
    place_right = False,
    previous_on_rm = False,
    section_bottom = 10,
    section_fg = ''.join([ Theme_Colors['Purple'] ]),
    section_fontsize = 20,
    section_left = 60,
    section_padding = 10,
    section_top = 10,
    sections = ['TreeTab', 'I dont understand', 'This layout settings'],
    urgent_bg = ''.join([ Theme_Colors['Red'] ]),
    urgent_fg = ''.join([ Theme_Colors['DarkBlue_default'] ]),
    vspace = 0,
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

