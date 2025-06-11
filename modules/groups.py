#
#
#

#
from libqtile.config import DropDown, Key, Group, Match, ScratchPad
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.keys import keys
from modules.layouts import layout_setting_max, layout_setting_verticalTile, layout_setting_treeTab, layout_setting_floating
from modules.variables import mod1, mod4, terminal_guess
#
import re

# NOTE: How can I get my groups to stick to screens? -- Qtile:Frequently Asked Questions
# https://docs.qtile.org/en/stable/manual/faq.html#how-can-i-get-my-groups-to-stick-to-screens


groups = [
  # INFO: xprop | grep WM_CLASS
  # INFO: and using 2nd argument

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
      layout.Max(**layout_setting_max),
      layout.TreeTab(**layout_setting_treeTab),
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

  # TODO: Add Virt-manager workspace?


  Group(name = '7', label = '7.sub-1',
    screen_affinity = 1, position = 7,
    layout = 'max',
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(alacritty)$"))],
  ),

  Group(name = '8', label = '8.sub-2',
    screen_affinity = 1,  position = 8,
    layout = 'max',
    init = True, persist = True,
  ),


  Group(name = '9', label = '9.null',
    screen_affinity = 0, position = 9,
    layouts = [
      layout.Max(**layout_setting_max),
    ],
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

