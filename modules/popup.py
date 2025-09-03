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
from modules.variables import (
  font_set,
  mod4,
)
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

  popupImage_common_settings = {
    'pos_y': 0.1,
    'width': 0.1,
    'height': 0.5,
    'colour': Theme_Colors['LightBlue'].replace('#', ''),
    'mask': True,
    'highlight': Theme_Colors['Oreange'],
  }

  popupText_common_settings = {
    'pos_y': 0.7,
    'width': 0.2,
    'height': 0.2,
    'h_align': 'center',
    'font': font_set['main'],
    'fontsize': 20,
    'foreground_highlighted': Theme_Colors['Oreange'],
    'foreground': Theme_Colors['LightBlue'],
    'highlight': Theme_Colors['Oreange'],
  }

  controls = [
    # 1. Screensaver
    PopupImage(
      pos_x = 0.15,
      filename = '~/.config/qtile/icons/svgrepo-com-zzz.svg',
      mouse_callbacks = {
        'Button1': lazy.spawn('xfce4-screensaver-command --activate')
      },
      **popupImage_common_settings,
    ),
    # 2. Logout
    PopupImage(
      pos_x = 0.35,
      filename = '~/.config/qtile/icons/svgrepo-com-exit-point.svg',
      mouse_callbacks = {
        'Button1': lazy.shutdown()
      },
      **popupImage_common_settings,
    ),
    # 3. Power off
    PopupImage(
      pos_x = 0.55,
      filename = '~/.config/qtile/icons/svgrepo-com-power.svg',
      mouse_callbacks = {
        'Button1': lazy.spawn('systemctl reboot')
      },
      **popupImage_common_settings,
    ),
    # 4. Reboot
    PopupImage(
      pos_x = 0.75,
      filename = '~/.config/qtile/icons/svgrepo-com-restart.svg',
      mouse_callbacks = {
        'Button1': lazy.shutdown(),
      },
      **popupImage_common_settings,
    ),

    # 1. Screensaver
    PopupText(
      pos_x = 0.10,
      text = 'Sleep',
      **popupText_common_settings,
    ),
    # 2. Logout
    PopupText(
      pos_x = 0.30,
      text = 'Logout',
      **popupText_common_settings,
    ),
    # 3. Power off
    PopupText(
      pos_x = 0.50,
      text = 'Power off',
      **popupText_common_settings,
    ),
    # 4. Reboot
    PopupText(
      pos_x = 0.70,
      text = 'Reboot',
      **popupText_common_settings,
    ),
  ]

  layout = PopupRelativeLayout(
    qtile,
    width = 1000,
    height = 200,
    controls = controls,
    background = ''.join([ Theme_Colors['DarkBlue_lighten'], '88' ]),
    initial_focus = 1,
  )

  layout.show(centered = True)



keys.extend([
  Key([mod4, 'shift'], 'g', lazy.function(show_graphs),     desc = 'Popup show'),
  Key([mod4, 'shift'], 'f', lazy.function(hide_graphs),     desc = 'Popup hide'),
  Key([mod4, 'shift'], 'q', lazy.function(show_power_menu), desc = 'Power Menu'),
])


##

