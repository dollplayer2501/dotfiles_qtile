"""
Hooks
=====

I don't really understand.
Although it's not directly related to this function, is it possible to write logs at any time?

Hooks - Examples
https://docs.qtile.org/en/stable/manual/config/hooks.html

Built-in Hooks
https://docs.qtile.org/en/stable/manual/ref/hooks.html
"""

# import os
import subprocess
#
from libqtile import hook, qtile, widget
from libqtile.utils import send_notification # NOTE: need `python-dbus-fast`
from libqtile.log_utils import logger
#
from modules.variables import autostart_sh, shutdown_sh


logger.setLevel('INFO')

groupbox1 = widget.GroupBox(visible_groups = ['1', '2', '3', '4', '5', '9'])
groupbox2 = widget.GroupBox(visible_groups = ['7', '8'])


@hook.subscribe.startup_once
def autostart():
  logger.info('Hook: startup_once! in')
  subprocess.call([autostart_sh])
  logger.info('Hook: startup_once! out')


@hook.subscribe.startup_complete
def run_every_startup():
  logger.info('Hook: startup_complete!')


@hook.subscribe.shutdown
def autostart():
  logger.info('Hook: shutdown!')
  subprocess.run([shutdown_sh])


@hook.subscribe.restart
def run_every_startup():
  # NOTE: This does not display?
  logger.info('Hook: restart')


@hook.subscribe.screens_reconfigured
async def _():
  if len(qtile.screens) > 1:
    groupbox1.visible_groups = ['1', '2', '3', '4', '5', '9']
  else:
    groupbox1.visible_groups = ['1', '2', '3', '4', '5', '7', '8', '9']
  if hasattr(groupbox1, 'bar'):
    groupbox1.bar.draw()


@hook.subscribe.enter_chord
def enter_chord(chord_name):
  # send_notification("qtile", "Started {chord_name} key chord.")
  pass

##

