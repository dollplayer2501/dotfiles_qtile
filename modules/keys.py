"""
Keys
====

https://docs.qtile.org/en/stable/manual/config/keys.html
"""

import os
#
from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord
#
from modules.variables import MOD4, CONTROL, SHIFT, TAB, SPACE, RETURN, UP, DOWN, LEFT, RIGHT
from modules.popup import show_power_menu
from modules.functions import focus_next_floating, spawn_by_group


keys = [
  # A list of available commands that can be bound to keys can be found
  # at https://docs.qtile.org/en/latest/manual/config/lazy.html


  # Switch between windows
  Key([MOD4], 'h', lazy.layout.left(),  desc = 'Move focus to left'),
  Key([MOD4], 'l', lazy.layout.right(), desc = 'Move focus to right'),
  Key([MOD4], 'j', lazy.layout.down(),  desc = 'Move focus down'),
  Key([MOD4], 'k', lazy.layout.up(),    desc = 'Move focus up'),


  # Move windows between left/right columns or move up/down in current stack.
  # Moving out of range in Columns layout will create new column.

  # INFO: .config/qtile · Derek Taylor / Dotfiles · GitLab
  # https://gitlab.com/dwt1/dotfiles/-/tree/master/.config/qtile?ref_type=heads
  Key([MOD4, SHIFT], 'h',
    lazy.layout.shuffle_left(),
    lazy.layout.move_left().when(layout = ['treetab']),
    desc = 'Move window to the left/move tab left in treetab'),
  Key([MOD4, SHIFT], 'l',
    lazy.layout.shuffle_right(),
    lazy.layout.move_right().when(layout = ['treetab']),
    desc = 'Move window to the right/move tab right in treetab'),
  Key([MOD4, SHIFT], 'j',
    lazy.layout.shuffle_down(),
    lazy.layout.section_down().when(layout = ['treetab']),
    desc = 'Move window down/move down a section in treetab'),
  Key([MOD4, SHIFT], 'k',
    lazy.layout.shuffle_up(),
    lazy.layout.section_up().when(layout = ['treetab']),
    desc = 'Move window up/move up a section in treetab'),


  # Grow windows. If current window is on the edge of screen and direction
  # will be to screen edge - window would shrink.
  Key([MOD4, CONTROL], 'h', lazy.layout.grow_left(),  desc = 'Grow window to left'),
  Key([MOD4, CONTROL], 'l', lazy.layout.grow_right(), desc = 'Grow window to right'),
  Key([MOD4, CONTROL], 'j', lazy.layout.grow_down(),  desc = 'Grow window to down'),
  Key([MOD4, CONTROL], 'k', lazy.layout.grow_up(),    desc = 'Grow window to up'),


  ## Key([mod4, SHIFT, CONTROL], 'h', lazy.layout.swap_column_left(),  desc = 'Swap Column left'),
  ## Key([mod4, SHIFT, CONTROL], 'l', lazy.layout.swap_column_right(), desc = 'Swap Column right'),


  Key([MOD4], UP,    lazy.window.move_floating(0, -10), desc = 'Move floating window to up'),
  Key([MOD4], DOWN,  lazy.window.move_floating(0, 10),  desc = 'Move floating window to down'),
  Key([MOD4], LEFT,  lazy.window.move_floating(-10, 0), desc = 'Move floating window to left'),
  Key([MOD4], RIGHT, lazy.window.move_floating(10, 0),  desc = 'Move floating window to right'),


  Key([MOD4, SHIFT], UP,    lazy.window.resize_floating(0, 10),  desc = 'Resize floating window to bottom, large'),
  Key([MOD4, SHIFT], DOWN,  lazy.window.resize_floating(0, -10), desc = 'Resize floating window to bottom, small'),
  Key([MOD4, SHIFT], LEFT,  lazy.window.resize_floating(-5, 0),  desc = 'Resize floating window to right, small'),
  Key([MOD4, SHIFT], RIGHT, lazy.window.resize_floating(5, 0),   desc = 'Resize floating window to right, large'),


  # Toggle between split and unsplit sides of stack.
  # Split = all windows displayed
  # Unsplit = 1 window displayed, like Max layout, but still with
  # multiple stack panes
  Key([MOD4, SHIFT], RETURN, lazy.layout.toggle_split(), desc = 'Toggle between split and unsplit sides of stack'),


  Key([MOD4], 'n', lazy.layout.normalize(),         desc = 'Reset all window sizes'),
  Key([MOD4], 'm', lazy.layout.maximize(),          desc = 'Maximize window sizes'),
  Key([MOD4], 'f', lazy.window.toggle_fullscreen(), desc = 'Toggle fullscreen on the focused window'),
  Key([MOD4], 't', lazy.window.toggle_floating(),   desc = 'Toggle floating on the focused window'),
  Key([MOD4], 'w', lazy.window.kill(),              desc = 'Kill focused window'),
  Key([MOD4], 'q', lazy.function(show_power_menu),  desc = 'Popup Power Menu'),
  Key([MOD4], 'b', lazy.hide_show_bar(position = 'bottom'), desc = 'Toggle bottom bar'),


  Key([MOD4],          'r', lazy.spawncmd(),      desc = 'Spawn a command using a prompt widget'),
  Key([MOD4, CONTROL], 'r', lazy.reload_config(), desc = 'Reload the config'),


  Key([MOD4], TAB,    lazy.next_layout(),            desc = 'Toggle between layouts'),
  Key([MOD4], SPACE,  lazy.layout.next(),            desc = 'Move normal window focus to other window'),
  Key([MOD4], RETURN, lazy.function(spawn_by_group), desc = 'Spawn app by group, kitty, brave, thunar'),
  Key([MOD4, SHIFT], SPACE, lazy.function(focus_next_floating), desc = 'Move floating window focus to other window'),


  Key([MOD4], 'period', lazy.next_screen(), desc = 'Toggle monitor, if 2 monitors'),


  # Key([], 'Print',
  #   lazy.spawn("scrot -z -p 'EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png' -e ' mv $f ~/Pictures/'"),
  #   desc = 'Print screen'
  # ),

  # `my_scrot_now` is `command scrot -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([MOD4, CONTROL], 'p', lazy.spawn("fish -c 'my_scrot_now'"),  desc = 'Print screen now'),
  # `my_scrot_wait` is `command scrot -c -d 10 -z -p "EndeavourOS_Qtile_%Y-%m-%d_%H-%M-%S.png" -e "mv \$f ~/Pictures/"`
  Key([MOD4, CONTROL], 'i', lazy.spawn("fish -c 'my_scrot_wait'"), desc = 'Print screen after 10 sec'),


  KeyChord([MOD4], 'z', [
      # TODO: brave --incognito
      # TODO: My customized gen-keybinging-img does not hook mod+z, shift+b
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
    mode = False,
    # timeout = 3, # NOTE: This does not use?
    name = 'Applications',
  ),


  KeyChord([MOD4], 'x', [
      Key([], 'm', lazy.group['scratchpad'].dropdown_toggle('mousepad'), desc = 'Scratchpad Mousepad'),
      Key([], 'n', lazy.group['scratchpad'].dropdown_toggle('notable'),  desc = 'Scratchpad Notable'),
    ],
    mode = False,
    name = 'Scratchpad',
  ),


  KeyChord([MOD4], 'c', [
      # NOTE: When running anything other than Kitty, pressing Mod4+Return launches xfce4-terminal.
      # NOTE: The reason is unknown.
      Key([], 'a', lazy.spawn('alacritty'),      desc = 'Run Alacritty'),
      Key([], 'g', lazy.spawn('ghostty'),        desc = 'Run Ghostty'),
      Key([], 'k', lazy.spawn('kitty'),          desc = 'Run Kitty'),
      Key([], 'w', lazy.spawn('wezterm'),        desc = 'Run Wezterm'),
      Key([], 'x', lazy.spawn('xfce4-terminal'), desc = 'Run Xfce4-terminal'),
    ],
    mode = False,
    name = 'Terminal',
  ),


  # This is test.
  Key([MOD4], "F2", lazy.spawn("vlc")),
]


##

