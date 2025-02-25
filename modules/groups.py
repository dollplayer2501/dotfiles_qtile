#
#
#

#
from libqtile.config import DropDown, Key, Group, Match, ScratchPad
from libqtile.lazy import lazy
from libqtile import layout
#
from modules.keys import keys
from modules.variables import mod1, mod4, terminal_guess
#
import re



groups = [
  # MEMO: xprop | grep WM_CLASS
  # MEMO: and using 2nd argument

  Group(name = '1', position = 1, label = '1.terminal',
    # TODO: This is original, not configration.
    # layouts = [layout.VerticalTile(), layout.TreeTab()],
    # TODO: This does not work.
    # layouts = ['verticaltile', 'max'],
    layout = 'verticaltile', 
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
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(brave-browser|firefox)$"))],
  ),

  Group(name = '4', position = 4, label = '4.tool',
    layout = 'max',
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(keepassxc|Notable|Yad|Virt-manager|Mousepad|Thunar)$"))],
  ),

  Group(name = '5', position = 5, label = '5.misc',
    layout = 'treetab',
    init = True, persist = True,
    matches = [Match(wm_class = re.compile(r"^(libreoffice|Gimp|Claws-mail)$"))],
  ),

  Group(name = '9', position = 9, label = '9.null',
    layout = 'max',
    init = True, persist = True,
  ),
]


for i in groups:
  keys.extend([
    # mod4 + group number = switch to group
    Key([mod4], i.name,
      lazy.group[i.name].toscreen(),
      desc = 'Switch to group {}'.format(i.name),
    ),

    # mod4 + shift + group number = switch to & move focused window to group
    Key([mod4, 'shift'], i.name,
      lazy.window.togroup(i.name, switch_group = True),
      desc = 'Switch to & move focused window to group {}'.format(i.name),
    ),

    # Or, use below if you prefer not to switch to that group.
    # # mod4 + shift + group number = move focused window to group
    # Key([mod4, "shift"], i.name, lazy.window.togroup(i.name),
    #     desc="move focused window to group {}".format(i.name)),
  ])

  keys.append(
    Key(['control', 'mod1'], f'f{i.name}',
      lazy.core.change_vt(i.name).when(func = lambda: qtile.core.name == 'wayland'),
      desc = f'Switch to VT{i.name}',
    )
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

