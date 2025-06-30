#
#
#

import re
#
from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.variables import mod1, mod4, terminal_guess
from modules.keys import keys
from modules.layouts import (
    layout_setting_max,
    layout_setting_verticalTile,
    layout_setting_treeTab,
    layout_setting_floating,
    layout_setting_monadWide,
    layout_setting_monadTail,
    layout_setting_matrix,
  )
from modules.functions import go_to_group, go_to_group_and_move_window


groups = [
  # NOTE: xprop | grep WM_CLASS
  # NOTE: and using 2nd argument

  Group(name = '1', label = '1.terminal',
    screen_affinity = 0, position = 1,
    layouts = [
      layout.VerticalTile(**layout_setting_verticalTile),
      layout.TreeTab(**layout_setting_treeTab),
      layout.Max(**layout_setting_max),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(kitty)$"))],
  ),

  Group(name = '2', label = '2.code',
    screen_affinity = 0, position = 2,
    layouts = [
      layout.Max(**layout_setting_max),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(code-oss)$"))],
  ),

  Group(name = '3', label = '3.web',
    screen_affinity = 0, position = 3,
    layouts = [
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(brave-browser|firefox)$"))],
  ),

  Group(name = '4', label = '4.tool',
    screen_affinity = 0, position = 4,
    layouts = [
      layout.MonadWide(**layout_setting_monadWide),
      layout.MonadTall(**layout_setting_monadTail),
      layout.Floating(**layout_setting_floating),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(keepassxc|Notable|Yad|Virt-manager|Mousepad|Thunar)$"))],
  ),

  Group(name = '5', label = '5.misc',
    screen_affinity = 0, position = 5,
    layouts = [
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab),
      layout.Floating(**layout_setting_floating),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(libreoffice|Gimp|Claws-mail)$"))],
  ),


  Group(name = '7', label = '7.sub-1',
    screen_affinity = 1, position = 7,
    layouts = [
      layout.Floating(**layout_setting_floating),
    ],
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(alacritty)$"))],
  ),

  Group(name = '8', label = '8.sub-2',
    screen_affinity = 1,  position = 8,
    layouts = [
      layout.Max(**layout_setting_max),
      layout.Matrix(**layout_setting_matrix, columns = 2),
    ],
    init = True, persist = True,
  ),


  Group(name = '9', label = '9.null',
    screen_affinity = 0, position = 9,
    layouts = [
      layout.Floating(**layout_setting_floating),
      layout.Max(**layout_setting_max),
      layout.Matrix(**layout_setting_matrix, columns = 4),
    ],
    init = True, persist = True,
  ),
]


for i in groups:
  keys.append(
    Key([mod4], i.name, lazy.function(go_to_group(i.name)),
      desc = 'Switch to group {}'.format(i.name))
  )
  keys.append(
    Key([mod4, 'shift'], i.name, lazy.function(go_to_group_and_move_window(i.name)),
      desc = 'Switch to & move focused window to group {}'.format(i.name))
  )


# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
# for vt in range(1, 9):
# for vt in groups:
#   keys.append(
#     Key(['control', 'mod1'], f'f{vt}',
#       lazy.core.change_vt(vt).when(func = lambda: qtile.core.name == 'wayland'),
#       desc = f'Switch to VT{vt}',
#     )
#   )


##

