"""
Groups
======

The layout that can be used is set for each workspace.
For layout settings, see `./modules/layouts.py`.

I have a dual monitor setup, but I only use one screen.

https://docs.qtile.org/en/stable/manual/config/groups.html
"""

import re
#
from libqtile.config import Key, Group, Match
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.variables import MOD4, SHIFT
from modules.keys import keys
from modules.layouts import (
    layout_setting_columns,
    layout_setting_floating,
    layout_setting_matrix,
    layout_setting_max,
    layout_setting_monadTall,
    layout_setting_monadWide,
    layout_setting_treeTab,
    layout_setting_verticalTile,
  )
from modules.functions import go_to_group, go_to_group_and_move_window


groups = [

  Group(screen_affinity = 0, position = 1,
    name = '1', label = '1.terminal',
    layouts = [
      layout.TreeTab(**layout_setting_treeTab),
      layout.VerticalTile(**layout_setting_verticalTile),
      layout.Max(**layout_setting_max),
    ],
    matches = [
      Match(wm_class = 'kitty'),
      Match(wm_class = 'Notable'),
    ],
    init = True, persist = True,
  ),

  Group(screen_affinity = 0, position = 2,
    name = '2', label = '2.code',
    layouts = [
      layout.Max(**layout_setting_max),
    ],
    matches = [
      Match(wm_class = 'code-oss'),
    ],
    init = True, persist = True,
  ),

  Group(screen_affinity = 0, position = 3,
    name = '3', label = '3.web',
    layouts = [
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab),
    ],
    matches = [
      Match(wm_class = 'brave-browser'),
      Match(wm_class = 'firefox'),
      Match(wm_class = 'keepassxc'),
    ],
    init = True, persist = True,
  ),

  Group(screen_affinity = 0, position = 4,
    name = '4', label = '4.tool',
    layouts = [
      layout.MonadWide(**layout_setting_monadWide),
      layout.MonadTall(**layout_setting_monadTall),
      layout.Floating(**layout_setting_floating),
    ],
    matches = [
      Match(wm_class = 'Thunar'),
      Match(wm_class = 'Mousepad'),
      Match(wm_class = 'Virt-manager'),
      Match(wm_class = 'Yad'),
    ],
    init = True, persist = True,
  ),

  Group(screen_affinity = 0, position = 5,
    name = '5', label = '5.misc',
    layouts = [
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab),
      layout.Floating(**layout_setting_floating),
    ],
    matches = [
      Match(wm_class = 'libreoffice'),
      Match(wm_class = 'Gimp'),
      Match(wm_class = 'Claws-mail'),
      Match(wm_class = 'steam'),
    ],
    init = True, persist = True,
  ),


  Group(screen_affinity = 1, position = 7,
    name = '7', label = '7.sub-1',
    layouts = [
      layout.Floating(**layout_setting_floating),
    ],
    init = True, persist = True,
  ),

  Group(screen_affinity = 1, position = 8,
    name = '8', label = '8.sub-2',
    layouts = [
      layout.Max(**layout_setting_max),
      layout.Matrix(**layout_setting_matrix, columns = 4),
    ],
    init = True, persist = True,
  ),


  Group(screen_affinity = 0, position = 9,
    name = '9', label = '9.null',
    layouts = [
      layout.Matrix(**layout_setting_matrix, columns = 4),
      layout.Columns(**layout_setting_columns),
      layout.Floating(**layout_setting_floating),
    ],
    init = True, persist = True,
  ),
]


for i in groups:
  keys.append(
    Key([MOD4], i.name, lazy.function(go_to_group(i.name)),
      desc = 'Switch to group {}'.format(i.name))
  )
  keys.append(
    Key([MOD4, SHIFT], i.name, lazy.function(go_to_group_and_move_window(i.name)),
      desc = 'Switch to & move focused window to group {}'.format(i.name))
  )


##

