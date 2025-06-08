#
# Floating, float_rules
#   https://docs.qtile.org/en/stable/manual/config/index.html of `floating_layout`
#

#
from libqtile import layout
from libqtile.config import Match
#
from modules.variables import terminal_sub1, terminal_sub8, terminal_sub9
#
from theme_colors import Theme_Colors


# INFO: xprop | grep WM_CLASS

floating_layout = layout.Floating(
  border_width = 1,
  border_focus = Theme_Colors['Green'],
  border_normal = Theme_Colors['LightBlue'],

  float_rules = [
    *layout.Floating.default_float_rules,

    Match(wm_class = 'Xfce4-settings-manager'),
    Match(wm_class = 'Xfce4-screensaver-configure.py'),
    # Match(wm_class = 'Xfce4-panel'),
    Match(wm_class = 'Wrapper-2.0'),

    Match(wm_class = 'pavucontrol'),
    Match(wm_class = 'nm-connection-editor'),
    Match(wm_class = 'Blueman-manager'),
    Match(wm_class = 'Xfce4-about'),
    Match(wm_class = 'Ristretto'),

    # INFO: This is bad pattern
    #  Match(wm_class = 'Xfce4-terminal'),

    # Match(wm_class = 'Mousepad'),
    # Match(wm_class = 'Thunar'),

    Match(wm_class = 'feh'),

    Match(wm_class = 'Virt-manager'),
      # Need to run with root user
      # - sudo systemctl enable --now libvirtd.service
      # - systemctl status libvirtd.service
      # - sudo virsh net-autostart default
      # - sudo virt-manager
      # Shared directory, This is guest
      # - sudo mount -t virtiofs Share_Points /home/dollplayer/Public/

    Match(wm_class = 'Parole'),
    Match(wm_class = 'vlc'),
      # Movie Player

    Match(wm_class = 'Yad'),
      # EOS-welcome
    # Match(wm_class = 'Claws-mail'),

    Match(wm_class = terminal_sub1),
    Match(wm_class = terminal_sub8),
    # Match(wm_class = terminal_sub9),

    # Match(wm_class="confirmreset"),  # gitk
    # Match(wm_class="makebranch"),  # gitk
    # Match(wm_class="maketag"),  # gitk
    # Match(wm_class="ssh-askpass"),  # ssh-askpass
    # Match(title="branchdialog"),  # gitk
    # Match(title="pinentry"),  # GPG key password entry
    ]
)


##

