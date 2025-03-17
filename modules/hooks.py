#
# Hooks - Examples
#  https://docs.qtile.org/en/stable/manual/config/hooks.html
#
# Built-in Hooks
#  https://docs.qtile.org/en/stable/manual/ref/hooks.html
#

#
from libqtile import hook
# from libqtile import hook, qtile
# from libqtile.utils import send_notification
from libqtile.log_utils import logger
#
from modules.variables import autostart_sh, shutdown_sh
# from modules.groups import groups
#
import os
import subprocess


logger.setLevel('INFO')


@hook.subscribe.startup_once
def autostart():
  logger.info('Hook: startup_once')
  subprocess.call([autostart_sh])


@hook.subscribe.startup_complete
def run_every_startup():
  logger.info('Hook: startup_complete')
  # send_notification('qtile', 'Startup complete')
  # subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.shutdown
def autostart():
  subprocess.run([shutdown_sh])


@hook.subscribe.restart
def run_every_startup():
  logger.info('Hook: restart')
  # send_notification('qtile', 'Restarting...')


# def set_wallpaper_for_group(group_name):
#   wallpapers = {
#     '1': '/home/dollplayer/Pictures/WallPaper/01.jpg',
#     '2': '/home/dollplayer/Pictures/WallPaper/02.jpg',
#     '3': '/home/dollplayer/Pictures/WallPaper/03.jpg',
#     '4': '/home/dollplayer/Pictures/WallPaper/04.jpg',
#     '5': '/home/dollplayer/Pictures/WallPaper/05.jpg',
#     '9': '/home/dollplayer/Pictures/WallPaper/06.jpg',
#   }
#   wallpaper_path = wallpapers.get(group_name, default_wallpaper)
#   for screen in qtile.screens:
#     screen.cmd_set_wallpaper(wallpaper_path, 'fill')

# @hook.subscribe.group_window_added
# def change_wallpaper(groups):
#   set_wallpaper_for_group(groups.name)


##

