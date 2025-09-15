#
# Mouse
#   https://docs.qtile.org/en/stable/manual/config/mouse.html
#

from libqtile.config import Click, Drag
from libqtile.lazy import lazy
#
from modules.variables import mod4


mouse = [
  # Left button
  Drag([mod4], 'Button1',
    lazy.window.set_position_floating(), start = lazy.window.get_position(),
    # desc = 'Move in Mouse',
  ),
  # Center button
  Click([mod4], 'Button2',
    lazy.window.bring_to_front(),
    # desc = 'Front in Mouse',
  ),
  Click([mod4, 'shift'], 'Button2',
    lazy.window.move_down(),
    # desc = 'Bottom in Mouse',
  ),
  # Right button
  Drag([mod4], 'Button3',
    lazy.window.set_size_floating(), start = lazy.window.get_size(),
    # desc = 'Resize in Mouse',
  ),
]


##

