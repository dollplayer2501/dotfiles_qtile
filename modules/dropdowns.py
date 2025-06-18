#
# Groups
#   https://docs.qtile.org/en/latest/manual/config/groups.html#dropdown
#

from libqtile.config import DropDown, Key, ScratchPad
from libqtile.lazy import lazy
#
from modules.variables import mod1, mod4, terminal_sub1
from modules.keys import keys
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
  DropDown('scratch_term',      [terminal_sub1],            **dropdown_common_settings),
  DropDown('scratch_keepassxc', ['keepassxc'],              **dropdown_common_settings),
  DropDown('scratch_mousepad',  ['mousepad'],               **dropdown_common_settings),
  DropDown('scratch_notable',   ['notable'],                **dropdown_common_settings),
  DropDown('scratch_thunar',    ['thunar'],                 **dropdown_common_settings),
  DropDown('scratch_setting',   ['xfce4-settings-manager'], **dropdown_common_settings),
]


# NOTE: This may not be necessary, it works even without it.
for i in dropdowns:
  i.floating = True


groups.append(
  ScratchPad('scratchpad', dropdowns),
)


keys.extend([
  Key([mod4, mod1, 'control'], 'k', lazy.group['scratchpad'].dropdown_toggle('scratch_keepassxc'), desc = 'Scratchpad KeepassXC'),
  Key([mod4, mod1, 'control'], 'm', lazy.group['scratchpad'].dropdown_toggle('scratch_mousepad'),  desc = 'Scratchpad Mousepad'),
  Key([mod4, mod1, 'control'], 'n', lazy.group['scratchpad'].dropdown_toggle('scratch_notable'),   desc = 'Scratchpad Notable'),
  Key([mod4, mod1, 'control'], 't', lazy.group['scratchpad'].dropdown_toggle('scratch_thunar'),    desc = 'Scratchpad Thunar'),
  Key([mod4, mod1, 'control'], 'x', lazy.group['scratchpad'].dropdown_toggle('scratch_setting'),   desc = 'Scratchpad Xfce4 setting'),
  Key([mod4, mod1, 'control'], 'w', lazy.group['scratchpad'].dropdown_toggle('scratch_term'),      desc = 'Scratchpad terminal'),
])


##

