#
# Keys
#   https://docs.qtile.org/en/stable/manual/config/keys.html
#

import os
#
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
#
from modules.variables import mod1, mod4
from modules.dmenu import dmenu_normal, dmenu_power, dmenu_terminal, dmenu_window
from modules.popup import show_power_menu
from modules.functions import focus_next_floating


keys = [
  # A list of available commands that can be bound to keys can be found
  # at https://docs.qtile.org/en/latest/manual/config/lazy.html

  # Switch between windows
  Key([mod4], 'h', lazy.layout.left(),  desc = 'Move focus to left'),
  Key([mod4], 'l', lazy.layout.right(), desc = 'Move focus to right'),
  Key([mod4], 'j', lazy.layout.down(),  desc = 'Move focus down'),
  Key([mod4], 'k', lazy.layout.up(),    desc = 'Move focus up'),

  # Move windows between left/right columns or move up/down in current stack.
  # Moving out of range in Columns layout will create new column.

  # INFO: .config/qtile · Derek Taylor / Dotfiles · GitLab
  # https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile?ref_type=heads

  Key([mod4, 'shift'], 'h',
    lazy.layout.shuffle_left(),
    lazy.layout.move_left().when(layout = ['treetab']),
    desc = 'Move window to the left/move tab left in treetab'),

  Key([mod4, 'shift'], 'l',
    lazy.layout.shuffle_right(),
    lazy.layout.move_right().when(layout = ['treetab']),
    desc = 'Move window to the right/move tab right in treetab'),

  Key([mod4, 'shift'], 'j',
    lazy.layout.shuffle_down(),
    lazy.layout.section_down().when(layout = ['treetab']),
    desc = 'Move window down/move down a section in treetab'),

  Key([mod4, 'shift'], 'k',
    lazy.layout.shuffle_up(),
    lazy.layout.section_up().when(layout = ['treetab']),
    desc = 'Move window up/move up a section in treetab'),

  # Grow windows. If current window is on the edge of screen and direction
  # will be to screen edge - window would shrink.
  Key([mod4, 'control'], 'h', lazy.layout.grow_left(),  desc = 'Grow window to left'),
  Key([mod4, 'control'], 'l', lazy.layout.grow_right(), desc = 'Grow window to right'),
  Key([mod4, 'control'], 'j', lazy.layout.grow_down(),  desc = 'Grow window to down'),
  Key([mod4, 'control'], 'k', lazy.layout.grow_up(),    desc = 'Grow window to up'),

  ## Key([mod4, 'shift', 'control'], 'h', lazy.layout.swap_column_left(),  desc = 'Swap Column left'),
  ## Key([mod4, 'shift', 'control'], 'l', lazy.layout.swap_column_right(), desc = 'Swap Column right'),

  Key([mod4], 'Up',    lazy.window.move_floating(0, -10), desc = 'Move floating window to up'),
  Key([mod4], 'Down',  lazy.window.move_floating(0, 10),  desc = 'Move floating window to down'),
  Key([mod4], 'Left',  lazy.window.move_floating(-10, 0), desc = 'Move floating window to left'),
  Key([mod4], 'Right', lazy.window.move_floating(10, 0),  desc = 'Move floating window to right'),

  Key([mod4, 'shift'], 'Up',   lazy.window.resize_floating(0, 10),  desc = 'Resize floating window to bottom, large'),
  Key([mod4, 'shift'], 'Down', lazy.window.resize_floating(0, -10), desc = 'Resize floating window to bottom, small'),
  Key([mod4, 'shift'], 'Left', lazy.window.resize_floating(-5, 0),  desc = 'Resize floating window to right, small'),
  Key([mod4, 'shift'], 'Right', lazy.window.resize_floating(5, 0),  desc = 'Resize floating window to right, large'),

  # Toggle between split and unsplit sides of stack.
  # Split = all windows displayed
  # Unsplit = 1 window displayed, like Max layout, but still with
  # multiple stack panes
  Key([mod4, 'shift'], 'Return', lazy.layout.toggle_split(), desc = 'Toggle between split and unsplit sides of stack'),
  # Toggle between different layouts as defined below

  Key([mod4], 'n', lazy.layout.normalize(),         desc = 'Reset all window sizes'),
  Key([mod4], 'm', lazy.layout.maximize(),          desc = 'Maximize window sizes'),
  Key([mod4], 'f', lazy.window.toggle_fullscreen(), desc = 'Toggle fullscreen on the focused window'),
  Key([mod4], 't', lazy.window.toggle_floating(),   desc = 'Toggle floating on the focused window'),

  Key([mod4, 'control'], 'r', lazy.reload_config(), desc = 'Reload the config'),
  Key([mod4], 'r', lazy.spawncmd(),                 desc = 'Spawn a command using a prompt widget'),
  # Key([mod4, 'control'], 'q', lazy.shutdown(),      desc = 'Shutdown Qtile, logout'),
  Key([mod4], 'q', lazy.function(show_power_menu),  desc = 'Popup Power Menu'),
  Key([mod4],            'w', lazy.window.kill(),   desc = 'Kill focused window'),

  Key([mod4, 'control'], 'a', lazy.run_extension(dmenu_window),   desc = 'Dmenu All Tasks'),
  Key([mod4, 'control'], 'd', lazy.run_extension(dmenu_normal),   desc = 'Dmenu Run Normal'),
  Key([mod4, 'control'], 'm', lazy.run_extension(dmenu_power),    desc = 'Dmenu Power Menu'),
  Key([mod4, 'control'], 't', lazy.run_extension(dmenu_terminal), desc = 'Dmenu All Terminal'),
  #
  Key([mod4], 'Return', lazy.spawn('kitty'), desc = 'Launch kitty'),
  # Key([mod4], 'Return', lazy.spawn('brave') if self.qtile.current_group == "2" else lazy.spawn('kitty')),
  Key([mod4], 'space',  lazy.layout.next(),  desc = 'Move normal window focus to other window'),
  Key([mod4], 'Tab',    lazy.next_layout(),  desc = 'Toggle between layouts'),

  Key([mod4, 'shift'  ], 'space', lazy.function(focus_next_floating), desc = 'Move floating window focus to other window'),
  # Key([mod4, 'control'], 'b',     lazy.function(toggle_bar),          desc = 'Toggle bottom bar'),

  # NOTE: Multiple monitor?
  # Key([mod4], 'o', lazy.to_screen(0), desc = 'To Main Screen'),
  # Key([mod4], 'p', lazy.to_screen(1), desc = 'To Sub Screen'),
  Key([mod4], 'period', lazy.next_screen(), desc = 'Next monitor'),


  # Key([], 'Print',
  #   lazy.spawn("scrot -z -p 'EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png' -e ' mv $f ~/Pictures/'"),
  #   desc = 'Print screen'
  # ),

  # Key([mod4, mod1], 'p',
  #   lazy.spawn("scrot -z -p 'EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png' -e ' mv $f ~/Pictures/'"),
  #   desc = 'Print screen now'),

  # `my_scrot_now` is `command scrot -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([mod4, 'control'], 'p', lazy.spawn("fish -c 'my_scrot_now'"),  desc = 'Print screen now'),
  # `my_scrot_wait` is `command scrot -c -d 10 -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([mod4, 'control'], 'i', lazy.spawn("fish -c 'my_scrot_wait'"), desc = 'Print screen after 10 sec'),

  # Key([mod4, 'shift'], 'q', lazy.function(show_power_menu), desc = 'Popup Power Menu'),

  KeyChord([mod4], 'z', [
      # TODO: brave --incognito
      # TODO: My customized gen-keybinging-img does not hook mod+z, shift+b
      Key([], 'a', lazy.spawn('alacritty'),   desc = 'Run Alacritty'),
      Key([], 'b', lazy.spawn('brave'),       desc = 'Run Brave'),
      Key([], 'c', lazy.spawn('claws-mail'),  desc = 'Run Claws mail'),
      Key([], 'g', lazy.spawn('gimp'),        desc = 'Run Gimp'),
      Key([], 'h', lazy.spawn('brave --incognito'), desc = 'Run Brave private'),
      Key([], 'k', lazy.spawn('keepassxc'),   desc = 'Run KeepassXC'),
      Key([], 'l', lazy.spawn('libreoffice'), desc = 'Run LibreOffice'),
      Key([], 'm', lazy.spawn('mousepad'),    desc = 'Run Mousepad'),
      Key([], 'n', lazy.spawn('notable'),     desc = 'Run Notable'),
      Key([], 's', lazy.spawn('flatpak run com.valvesoftware.Steam'), desc = 'Run Steam'),
      Key([], 't', lazy.spawn('thunar'),      desc = 'Run Thunar'),
      Key([], 'v', lazy.spawn('vlc'),         desc = 'Run VLC'),
    ],
    mode = True,
    # timeout = 3, # NOTE: This does not use?
    name = 'Applications',
  ),


  KeyChord([mod4], 'x', [
      Key([], 'a', lazy.group['scratchpad'].dropdown_toggle('alacritty'), desc = 'Scratchpad Alacritty'),
      Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('mousepad'),  desc = 'Scratchpad Mousepad'),
      Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('notable'),   desc = 'Scratchpad Notable'),
    ],
    mode = True,
    name = 'Scratchpad',
  ),


  # This is test.
  Key([mod4], "F2", lazy.spawn("vlc")),
]


##

