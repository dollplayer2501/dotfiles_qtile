#
#
#

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


##
