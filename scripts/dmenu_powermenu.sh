#!/usr/bin/bash
#
# a simple dmenu session script 
#
###

DMENU='dmenu -i -b -fn -xos4-terminus-medium-r-*--12-*-*-*-*-*-iso10646-1 -nb #000000 -nf #999999 -sb #000000 -sf #31658C'
choice=$(echo -e "logout\nshutdown\nreboot\nsuspend\nhibernate" | $DMENU)

case "$choice" in
  logout) i3-msg exit & ;;
  shutdown) sudo shutdown -h now & ;;
  reboot) sudo shutdown -r now & ;;
  suspend) sudo pm-suspend & ;;
  hibernate) sudo pm-hibernate & ;;
esac
