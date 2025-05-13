# qtile widget uptime - Brave Search
# https://search.brave.com/search?q=qtile+widget+uptime&source=desktop&summary=1&conversation=716dd33d3729359648fa3d

 import psutil
 import time
 def get_uptime():
   return time.strftime('%H:%M:%S', time.gmtime(psutil.boot_time()))

from libqtile.widget import base

class Uptime(base.ThreadPoolText):
  defaults = [
    ("update_interval", 1.0, "Update interval for the uptime widget"),
  ]

  def __init__(self, **config):
    base.ThreadPoolText.__init__(self, "", **config)
    self.add_defaults(Uptime.defaults)

  def poll(self):
    return get_uptime()
# Uptime(),

# from libqtile import widget
# from libqtile.lazy import lazy

# class MyWidget(widget.base._TextBox):
#   defaults = [
#     ("update_interval", 60, "Update interval in seconds."),
#   ]
#
#   def __init__(self, **config):
#     super().__init__("", **config)
#     self.add_defaults(MyWidget.defaults)
#     self.update()
#     self.timeout_add(self.update_interval, self.update)
#
#   def update(self):
#     self.text = "Updated Text"
#     self.bar.draw()
