#
# Groups
#   https://docs.qtile.org/en/latest/manual/config/groups.html#dropdown
#

#
from libqtile.config import DropDown, Key, ScratchPad
from libqtile.lazy import lazy
#
from modules.variables import mod1, mod4, terminal_sub1
#
from modules.keys import keys
from modules.groups import groups


## TODO: dropdown of xfce4-terminal does not work?

dropdowns = [
  DropDown('scratch_term',      [terminal_sub1],            width = 0.8, height = 0.7, y = 0,    opacity = 0.9),
  DropDown('scratch_keepassxc', ['keepassxc'],              width = 0.8, height = 0.9, y = 0.01, opacity = 0.9),
  DropDown('scratch_mousepad',  ['mousepad'],               width = 0.8, height = 0.9, y = 0.01, opacity = 0.9),
  DropDown('scratch_notable',   ['notable'],                width = 0.8, height = 0.9, y = 0.01, opacity = 0.9),
  DropDown('scratch_thunar',    ['thunar'],                 width = 0.8, height = 0.9, y = 0.01, opacity = 0.9),
  DropDown('scratch_setting',   ['xfce4-settings-manager'], width = 0.8, height = 0.9, y = 0.01, opacity = 0.9),
]


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

