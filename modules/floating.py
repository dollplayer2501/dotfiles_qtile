#
# Floating, float_rules
#   https://docs.qtile.org/en/stable/manual/config/index.html of `floating_layout`
#

from libqtile import layout
from libqtile.config import Match
#
from theme_colors import Theme_Colors


# INFO: xprop | grep WM_CLASS
# Use 2nd argument

floating_layout = layout.Floating(
  border_width = 1,
  # NOTE: Will it take precedence over layout.Floating settings?
  border_focus = Theme_Colors['Green'],
  border_normal = Theme_Colors['Gray_1'],

  float_rules = [
    *layout.Floating.default_float_rules,

    Match(wm_class = 'Xfce4-settings-manager'),
    Match(wm_class = 'Xfce4-screensaver-configure.py'),
    Match(wm_class = 'Wrapper-2.0'),

    Match(wm_class = 'pavucontrol'),
    Match(wm_class = 'nm-connection-editor'),
    Match(wm_class = 'Blueman-manager'),
    Match(wm_class = 'Xfce4-about'),
    Match(wm_class = 'Ristretto'),

    # INFO: This is bad pattern
    #  Match(wm_class = 'Xfce4-terminal'),

    Match(wm_class = 'Virt-manager'),

    Match(wm_class = 'feh'),
    Match(wm_class = 'Parole'),
    Match(wm_class = 'steam'),
    Match(wm_class = 'vlc'),

    Match(wm_class = 'Yad'),

    Match(wm_class = 'alacritty'),
    Match(wm_class = 'wezterm'),
    ]
)


##

