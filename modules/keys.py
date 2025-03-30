#
# INFO: Here are my rules:
#  Mod4 + Control:            Systematic control of Qtile
#  Mod4 + Mod1/Alt:           Application Launcher
#  Mod4 + Mod1/Alt + Control: Qtile's Scratchpad
#
# TODO: Some commands may not be accepted depending on the layout.
# These will be written to the error log.
#

#
import os
#
from libqtile import bar, extension, hook, layout, qtile
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
#
from modules.variables import mod1, mod4, terminal_main, terminal_sub1, terminal_sub8, terminal_sub9, terminal_guess, terminal_gpu
from modules.dmenu import dmenu_normal, dmenu_power, dmenu_terminal, dmenu_window


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
  Key([mod4, 'control'], 'h', lazy.layout.grow_left(),  desc = 'Grow window to the left'),
  Key([mod4, 'control'], 'l', lazy.layout.grow_right(), desc = 'Grow window to the right'),
  Key([mod4, 'control'], 'j', lazy.layout.grow_down(),  desc = 'Grow window down'),
  Key([mod4, 'control'], 'k', lazy.layout.grow_up(),    desc = 'Grow window up'),

  ## Key([mod4, 'shift', 'control'], 'h', lazy.layout.swap_column_left(),  desc = 'Swap Column left'),
  ## Key([mod4, 'shift', 'control'], 'l', lazy.layout.swap_column_right(), desc = 'Swap Column right'),

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
  Key([mod4, 'shift'],   'r', lazy.spawncmd(),      desc = 'Spawn a command using a prompt widget'),
  Key([mod4, 'control'], 'q', lazy.shutdown(),      desc = 'Shutdown Qtile, logout'),
  Key([mod4],            'w', lazy.window.kill(),   desc = 'Kill focused window'),

  Key([mod4],            'r', lazy.run_extension(dmenu_normal),   desc = 'Dmenu Run Normal'),
  Key([mod4, 'control'], 'a', lazy.run_extension(dmenu_window),   desc = 'Dmenu All Tasks'),
  Key([mod4, 'control'], 'p', lazy.run_extension(dmenu_power),    desc = 'Dmenu Power Menu'),
  Key([mod4, 'control'], 't', lazy.run_extension(dmenu_terminal), desc = 'Dmenu All Terminal'),

  Key([mod4], 'Return', lazy.spawn(terminal_main),  desc = 'Launch terminal'),
  # Key([mod4], 'Return', lazy.spawn('brave') if self.qtile.current_group == "2" else lazy.spawn(terminal_main)),
  Key([mod4], 'space',  lazy.layout.next(),         desc = 'Move window focus to other window'),
  Key([mod4], 'Tab',    lazy.next_layout(),         desc = 'Toggle between layouts'),


  # Key([], 'Print',
  #   lazy.spawn("scrot -z -p 'EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png' -e ' mv $f ~/Pictures/'"),
  #   desc = 'Print screen'
  # ),

  # Key([mod4, mod1], 'p',
  #   lazy.spawn("scrot -z -p 'EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png' -e ' mv $f ~/Pictures/'"),
  #   desc = 'Print screen now'),

  # `my_scrot_now` is `command scrot -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([mod4, mod1], 'p', lazy.spawn("fish -c 'my_scrot_now'"),  desc = 'Print screen now'),
  # `my_scrot_wait` is `command scrot -c -d 10 -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([mod4, mod1], 'i', lazy.spawn("fish -c 'my_scrot_wait'"), desc = 'Print screen after 10 sec'),

  # Key([mod4, mod1], 'p',
  #   lazy.function(lambda: os.system("fish -c 'my_scrot_now'")),
  #   desc = 'Print screen now'),
  # Key([mod], "f", lazy.function(lambda: os.system("fish -c 'my_function'")))

  Key([mod4, mod1], 'b', lazy.spawn('brave'),                  desc = 'Run Brave'),
  Key([mod4, mod1], 'c', lazy.spawn('claws-mail'),             desc = 'Run Claws mail'),
  Key([mod4, mod1], 'g', lazy.spawn('gimp'),                   desc = 'Run Gimp'),
  Key([mod4, mod1], 'k', lazy.spawn('keepassxc'),              desc = 'Run KeepassXC'),
  Key([mod4, mod1], 'l', lazy.spawn('libreoffice'),            desc = 'Run LibreOffice'),
  Key([mod4, mod1], 'm', lazy.spawn('mousepad'),               desc = 'Run Mousepad'),
  Key([mod4, mod1], 'n', lazy.spawn('notable'),                desc = 'Run Notable'),
  Key([mod4, mod1], 't', lazy.spawn('thunar'),                 desc = 'Run Thunar'),
  Key([mod4, mod1], 'v', lazy.spawn('vlc'),                    desc = 'Run VLC'),
  Key([mod4, mod1], 'x', lazy.spawn('xfce4-settings-manager'), desc = 'Run Xfce4 settings'),

  ## INFO: Not reflected in gen-keybinding-img?
  ## KeyChord([mod4], 'z', [
  ##     Key([], 'b', lazy.spawn('brave'),     desc = 'Launch Brave'),
  ##     Key([], 'k', lazy.spawn('keepassxc'), desc = 'Launch KeepassXC'),
  ## ]),
]


##

