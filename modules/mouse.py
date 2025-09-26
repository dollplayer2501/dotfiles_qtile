"""
Mouse
=====

https://docs.qtile.org/en/stable/manual/config/mouse.html
"""

from libqtile.config import Click, Drag
from libqtile.lazy import lazy
#
from modules.variables import MOD4, SHIFT


mouse = [
  # Left button
  Drag([MOD4], 'Button1',
    lazy.window.set_position_floating(), start = lazy.window.get_position(),
    # desc = 'Move in Mouse',
  ),
  # Center button
  Click([MOD4], 'Button2',
    lazy.window.bring_to_front(),
    # desc = 'Front in Mouse',
  ),
  Click([MOD4, SHIFT], 'Button2',
    lazy.window.move_down(),
    # desc = 'Bottom in Mouse',
  ),
  # Right button
  Drag([MOD4], 'Button3',
    lazy.window.set_size_floating(), start = lazy.window.get_size(),
    # desc = 'Resize in Mouse',
  ),
]


##

