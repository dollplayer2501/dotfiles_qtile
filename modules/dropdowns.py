#
# Groups
#   https://docs.qtile.org/en/latest/manual/config/groups.html#dropdown
#

from libqtile.config import DropDown, Key, KeyChord, ScratchPad
from libqtile.lazy import lazy
#
from modules.groups import groups


## TODO: dropdown of xfce4-terminal does not work?

dropdown_common_settings = {
  'width': 0.8,
  'height': 0.9,
  # 'x': 0,
  'y':  0.01,
  'opacity': 0.9,
  'match': None,
  'on_focus_lost_hide': False,
  'warp_pointer': False,
}

dropdowns = [
  DropDown('alacritty', ['alacritty'], **dropdown_common_settings),
  DropDown('mousepad',  ['mousepad'],  **dropdown_common_settings),
  DropDown('notable',   ['notable'],   **dropdown_common_settings),
]


# NOTE: This may not be necessary, it works even without it.
for i in dropdowns:
  i.floating = True


groups.append(
  ScratchPad('scratchpad', dropdowns),
)


##

