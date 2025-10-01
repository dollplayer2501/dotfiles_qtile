# Installation


## Current Approach

I use EndeavourOS. However, as of fall 2025—and even earlier—Qtile is not available as an option during the initial clean installation under the window manager or desktop environment selection. For this reason, I have been setting up Qtile using the following steps:

1. Choose and install Xfce4 on EndeavourOS.
2. Install `Qtile` and `qtile-extras` using `yay`.
3. Launch Xfce4 modules via `./scripts/autostart.sh`.

If you look at `./modules/screens_bar__main.py`, you’ll notice traces of trial and error. For example, running certain widgets requires installing additional packages, and I’ve documented these points to make it somewhat clear.


## Future Plans

1. Transition from Xfce4 to i3WM  
When I first set up this environment, my Linux skills were limited, so I relied entirely on Xfce4 modules for system configuration and management. Now that my skills have improved, I believe I can manage with i3WM, which EndeavourOS officially supports.  
(Incidentally, I also use EndeavourOS with i3WM separately.)

2. Unify installation sources  
Currently, Qtile is installed from the `extra` repository via `yay`, while `qtile-extras` comes from `AUR`—a somewhat inconsistent setup. In the future, I plan to either unify everything via AUR or install directly via `git clone`, but this is still undecided.

3. Wayland support is undecided  
This is probably still a long way off. If it happens, I intend to build my environment based on Sway.


## Multiple desktop environments and window managers

When you start Qtile with a misconfigured `./config.py`, it usually falls back to the default configuration—at least in the case of minor mistakes, such as typos. However, if the error involves introducing something new (for example, defining a new class in Python or adding a new widget in Qtile), the startup process may fail entirely, and Qtile will not launch at all. I plan to experiment more with such custom implementations in the future.

Considering this risk, it is important to have an alternative window manager available so that you can still log in and fix issues when Qtile refuses to start. For this reason, I did not install Qtile on a system without any desktop environment. Instead, I currently run Qtile alongside Xfce4, and in the future I plan to use i3WM as a fallback environment as well.


<!-- -->
