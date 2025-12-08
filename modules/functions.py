"""
Functions
=========

A group of functions that I may be using on my own.
Each individual function needs to be reviewed.

TODO: Adding Docstrings to individual functions?
"""

from libqtile.lazy import lazy
from libqtile import qtile


def focus_next_floating(qtile):
  group = qtile.current_group
  floating_windows = [w for w in group.windows if w.floating]
  if not floating_windows:
    return

  current = qtile.current_window
  if current in floating_windows:
    idx = floating_windows.index(current)
    next_idx = (idx + 1) % len(floating_windows)
  else:
    next_idx = 0

  floating_windows[next_idx].focus()


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


def spawn_by_group(qtile):
  group = qtile.current_group.name
  if '1' == group:
    qtile.spawn('/usr/bin/kitty')
  elif '3' == group:
    qtile.spawn('/usr/bin/firefox')
  elif '4' == group:
    qtile.spawn('/usr/bin/thunar')
  else:
    qtile.spawn('/usr/bin/kitty')


##
