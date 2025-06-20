#
#
#


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


# NOTE: This function does not work
# Toggle, show or hide bottom bar
# def toggle_bar(qtile):
#   screen = qtile.current_screen
#   bar = screen.bottom
#   if bar and hasattr(bar, 'window') and hasattr(bar.window, 'toggle'):
#     bar.window.toggle()


##
