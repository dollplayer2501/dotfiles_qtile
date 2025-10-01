#!/usr/bin/sh
#
# shutdown.sh - Script called when Qtile starts
#
# See `@hook.subscribe.shutdown`, `def autostart()` in `./modules/hooks.py`.
#

cp /dev/null ~/.local/share/qtile/qtile.log

echo '-- shutdown.sh      -- ' >> ~/.local/share/qtile/qtile.log


##
