#
# Using widgets in a popup
#  https://qtile-extras.readthedocs.io/en/v0.27.0/manual/how_to/popup.html#using-widgets-in-a-popup
#

from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy
#
# from qtile_extras.popup.toolkit import (
#     PopupRelativeLayout,
#     PopupWidget,
#     PopupImage,
#     PopupText,
#     PopupRelative,
#   )
from qtile_extras.popup import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
#
from modules.keys import keys
from modules.variables import mod4
from theme_colors import Theme_Colors


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


#
# TODO: This is a study and it is currently unfinished.
#
def show_power_menu(qtile):
  controls = [
    PopupImage(
      filename = '~/.config/qtile/icons/reshot-icon-lock-E9JS4ARYUH.svg',
      pos_x = 0.15,
      pos_y = 0.1,
      width = 0.1,
      height = 0.5,
      mouse_callbacks = {
        'Button1': lazy.spawn('xfce4-screensaver-command --lock')
      }
    ),
    PopupImage(
      filename = '~/.config/qtile/icons/reshot-icon-sleep-7SLFANCXGJ.svg',
      pos_x = 0.45,
      pos_y = 0.1,
      width = 0.1,
      height = 0.5,
      mouse_callbacks = {
        'Button1': lazy.spawn('systemctl suspend')
      }
    ),
    PopupImage(
      filename = '~/.config/qtile/icons/reshot-icon-turn-off-CDSGQH63TN-d79a9.svg',
      pos_x = 0.75,
      pos_y = 0.1,
      width = 0.1,
      height = 0.5,
      highlight = 'A00000',
      mouse_callbacks = {
        'Button1': lazy.shutdown(),
      },
    ),
    PopupText(
      text = 'Lock',
      pos_x = 0.1,
      pos_y = 0.7,
      width = 0.2,
      height = 0.2,
      h_align = 'center',
    ),
    PopupText(
      text = 'Sleep',
      pos_x = 0.4,
      pos_y = 0.7,
      width = 0.2,
      height = 0.2,
      h_align = 'center',
    ),
    PopupText(
      text = 'Shutdown',
      pos_x = 0.7,
      pos_y = 0.7,
      width = 0.2,
      height = 0.2,
      h_align = 'center',
    ),
  ]

  layout = PopupRelativeLayout(
    qtile,
    width = 1000,
    height = 200,
    controls = controls,
    background = ''.join([ Theme_Colors['DarkBlue_default'], '44' ]),
    initial_focus = None,
  )

  layout.show(centered = True)



keys.extend([
  Key([mod4, 'shift'], 'g', lazy.function(show_graphs),     desc = 'Popup show'),
  Key([mod4, 'shift'], 'f', lazy.function(hide_graphs),     desc = 'Popup hide'),
  Key([mod4, 'shift'], 'q', lazy.function(show_power_menu), desc = 'Power Menu'),
])


##

