#!/usr/bin/sh
#
# autostart.sh - Script called when Qtile starts
#
# See `@hook.subscribe.startup_once`, `def autostart()` in `./modules/hooks.py`.
#

echo '-- autostart.sh in  -- ' >> ~/.local/share/qtile/qtile.log


#
# Xfce4
# - /etc/xdg/autostart/
# - ~/.config/autostart/
# - /etc/xdg/xfce4/xinitrc
#

/usr/lib/at-spi-bus-launcher --launch-immediately &
#  AT-SPI D-Bus Bus
#   at-spi-dbus-bus.desktop

/usr/bin/xfsettingsd &
#  Xfce Settings Daemon
#   xfsettingsd.desktop

/usr/bin/xfce4-screensaver &
#  Screensaver
#   xscreensaver.desktop

sh -c "systemctl --user start xfce4-notifyd.service 2>/dev/null || exec /usr/lib/xfce4/notifyd/xfce4-notifyd" &
#  xfce4-notifyd.desktop
#   Xfce Notification Daemon
#     command line is `notify-send "abc"`
#     class is "Xfce4-notifyd"
#  NOTE: need `python-dbus-fast`


/usr/lib/xapps/xapp-sn-watcher &
#  xapp-sn-watcher.desktop
#   A service that provides the org.kde.StatusNotifierWatcher interface for XApps

/usr/bin/xdg-user-dirs-gtk-update &
#  user-dirs-update-gtk.desktop
#   User folders update

/usr/bin/xfce4-power-manager &
#  xfce4-power-manager.desktop
#   Power Manager

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
#  xfce-polkit-gnome-authentication-agent-1.desktop
#   PolicyKit Authentication Agent

/usr/bin/nm-applet &
#  nm-applet.desktop
#   NetworkManager Applet

/usr/bin/blueman-applet &
#  blueman, bluez
#  bluetooth.service

#
#
#

# xsetroot -cursor_name left_ptr & disowm


/usr/bin/fcitx5 &
/usr/bin/picom --daemon &
# sh ~/.config/conky/wonder_wall_03/start-quick.sh &

cp /dev/null /home/dollplayer/.local/share/syncthing.log
syncthing --no-browser --logfile="/home/dollplayer/.local/share/syncthing.log" > /dev/null &


# xfce4-terminal &


echo '-- autostart.sh out -- ' >> ~/.local/share/qtile/qtile.log


##
