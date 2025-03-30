#
# Using widgets in a popup
#  https://qtile-extras.readthedocs.io/en/v0.27.0/manual/how_to/popup.html#using-widgets-in-a-popup
#

from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy
#
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupWidget
#
from modules.keys import keys
from modules.variables import mod4


def show_graphs(qtile):
  global popup_graph

  # TODO: decoration this
  controls = [
    PopupWidget(
      widget = widget.CPUGraph(),
      width = 0.45,
      height = 0.45,
      pos_x = 0.05,
      pos_y = 0.05
    ),
    PopupWidget(
      widget = widget.NetGraph(),
      width = 0.45,
      height = 0.45,
      pos_x = 0.5,
      pos_y = 0.05
    ),
    PopupWidget(
      widget = widget.MemoryGraph(),
      width = 0.9,
      height = 0.45,
      pos_x = 0.05,
      pos_y = 0.5
    )
  ]

  popup_graph = PopupRelativeLayout(
    qtile,
    width = 1000,
    height = 200,
    controls = controls,
    background = "00000060",
    initial_focus = None,
    close_on_click = False
  )

  popup_graph.show(centered = True)

# TODO: toggle popup
# TODO: control z order ?
def hide_graphs(qtile):
  popup_graph.hide()


keys.extend([
  Key([mod4, 'shift'], 'g', lazy.function(show_graphs), desc = 'Popup show'),
  Key([mod4, 'shift'], 'f', lazy.function(hide_graphs), desc = 'Popup hide')
])


##

