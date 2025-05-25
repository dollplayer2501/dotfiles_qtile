#
# InteractiveCommandClient - Interfaces — Qtile 0.1.dev50+g8666bfc documentation
# https://docs.qtile.org/en/stable/manual/commands/interfaces.html#interactivecommandclient
#

from libqtile.command.client import InteractiveCommandClient

c = InteractiveCommandClient()
print(c.status())

info = c.widget["clock"].info()
print(info)

info = c.widget["windowtabs"].info()
print(info)

info = c.widget["clock"].screen.info()
print(info)

