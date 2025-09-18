#
# Using widgets in a popup
#  https://qtile-extras.readthedocs.io/en/v0.27.0/manual/how_to/popup.html#using-widgets-in-a-popup
#

from libqtile import widget
from libqtile.lazy import lazy
#
from qtile_extras.popup import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)
#
from modules.variables import font_set
from theme_colors import Theme_Colors


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
    # TODO: Add restart of Qtile ?

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
        'Button1': lazy.spawn('systemctl poweroff')
      },
      **popupImage_common_settings,
    ),
    # 4. Reboot
    PopupImage(
      pos_x = 0.75,
      filename = '~/.config/qtile/icons/svgrepo-com-restart.svg',
      mouse_callbacks = {
        'Button1': lazy.spawn('systemctl reboot')
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


##

