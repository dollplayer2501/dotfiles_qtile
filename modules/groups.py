#
#
#

#
from libqtile.config import DropDown, Key, Group, Match, ScratchPad
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.keys import keys
# from modules.layouts import layouts

from modules.variables import mod1, mod4, terminal_guess
#
import re

# NOTE: How can I get my groups to stick to screens? -- Qtile:Frequently Asked Questions
# https://docs.qtile.org/en/stable/manual/faq.html#how-can-i-get-my-groups-to-stick-to-screens


groups = [
  # INFO: xprop | grep WM_CLASS
  # INFO: and using 2nd argument

  Group(name = '1', position = 1, label = '1.terminal',
    # INFO: That pattern is OK, but my layouts config does not apply.
    # layouts = [layout.VerticalTile(), layout.TreeTab()],
    # layouts = ['verticaltile', 'max'],
    layout = 'verticaltile',
    screen_affinity = 0,
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(kitty)$"))],
  ),

  Group(name = '2', position = 2, label = '2.code',
    layout = 'max',
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(code-oss)$"))],
  ),

  Group(name = '3', position = 3, label = '3.web',
    layout = 'max',
    screen_affinity = 0,
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(brave-browser|firefox)$"))],
  ),

  Group(name = '4', position = 4, label = '4.tool',
    layout = 'max',
    screen_affinity = 0,
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(keepassxc|Notable|Yad|Virt-manager|Mousepad|Thunar)$"))],
  ),

  Group(name = '5', position = 5, label = '5.misc',
    layout = 'treetab',
    screen_affinity = 0,
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(libreoffice|Gimp|Claws-mail)$"))],
  ),

  # TODO: Add Virt-manager workspace?


  Group(name = '7', position = 7, label = '7.Sub-1',
    layout = 'max',
    screen_affinity = 1,
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(alacritty)$"))],
  ),

  Group(name = '8', position = 8, label = '8.Sub-2',
    layout = 'max',
    screen_affinity = 1,
    init = True, persist = True,
  ),


  Group(name = '9', position = 9, label = '9.null',
    layout = 'max',
    screen_affinity = 0,
    init = True, persist = True,
  ),
]


def go_to_group(name: str):
  def _inner(qtile):
    if len(qtile.screens) == 1:
      qtile.groups_map[name].toscreen()
      return

    if name in '123459':
      qtile.focus_screen(0)
      qtile.groups_map[name].toscreen()
    else:
      qtile.focus_screen(1)
      qtile.groups_map[name].toscreen()

  return _inner

def go_to_group_and_move_window(name: str):
  def _inner(qtile):
    if len(qtile.screens) == 1:
      qtile.current_window.togroup(name, switch_group = True)
      return

    if name in '123459':
      qtile.current_window.togroup(name, switch_group = False)
      qtile.focus_screen(0)
      qtile.groups_map[name].toscreen()
    else:
      qtile.current_window.togroup(name, switch_group = False)
      qtile.focus_screen(1)
      qtile.groups_map[name].toscreen()

  return _inner

for i in groups:
  keys.append(
    Key([mod4], i.name, lazy.function(go_to_group(i.name)))
  )
  keys.append(
    Key([mod4, 'shift'], i.name, lazy.function(go_to_group_and_move_window(i.name)))
  )


# for i in groups:
  # keys.extend([
    # mod4 + group number = switch to group
    ## Key([mod4], i.name,
    ##   lazy.group[i.name].toscreen(),
    ##   desc = 'Switch to group {}'.format(i.name),
    ## ),

    # mod4 + shift + group number = switch to & move focused window to group
    ## Key([mod4, 'shift'], i.name,
    ##   lazy.window.togroup(i.name, switch_group = True),
    ##   desc = 'Switch to & move focused window to group {}'.format(i.name),
    ## ),

    # Or, use below if you prefer not to switch to that group.
    # # mod4 + shift + group number = move focused window to group
    # Key([mod4, "shift"], i.name, lazy.window.togroup(i.name),
    #     desc="move focused window to group {}".format(i.name)),
  # ])

  # keys.append(
  #   Key(['control', 'mod1'], f'f{i.name}',
  #     lazy.core.change_vt(i.name).when(func = lambda: qtile.core.name == 'wayland'),
  #     desc = f'Switch to VT{i.name}',
  #   )
  # )


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

