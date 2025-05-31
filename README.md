> [!NOTE]
> Regarding the installation procedure for Qtile and Qtile-extras itself,  
> I first install Xfce4 in EndeavourOS, then install Qtile and Qtile-extras with `yay`, and then configure the various environments.  
> For this reason, various daemons use those of Xfce4.  
> In other words, I'm not using [EndeavourOS-Community-Editions/qtile](https://github.com/EndeavourOS-Community-Editions/qtile).

> [!WARNING]
> This configuration is adapted to my personal needs, so it is not recommended to use it directly.  
> I suggest forking the repository and modifying it according to your preferences.


> [!NOTE]
> As of late May 2025, I am adding a multi-monitor setup.  
> I'm still adjusting and don't always use multiple screens though.  
> <a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/EndeavourOS_Qtile_2025-05-23_19-52-39.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/EndeavourOS_Qtile_2025-05-23_19-52-39.png" width=600 /></a>


## About:

This is just a simple Qtile configuration files.  
Due to my lack of skills, I am simply "using Qtile".  
Even so, I enjoy using it every day!

I split the Qtile configuration files, and the template is [EndeavourOS-Community-Editions/qtile: setup](https://github.com/EndeavourOS-Community-Editions/qtile)...the current files are not split, though.


## Screenshots:

Regarding the color scheme, I am not using any famous one.  
I am using the color scheme used by Xfce4 and Xfce4-terminal in EndeavourOS, please refer to `./modules/Theme_Colors_EndeavourOS_Xfce4.py`.  
For information on the fonts, terminal used, please refer to `./modules/variables.py`.

### TreeTab Layout

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/01..TreeTabLayout..EndeavourOS_Qtile_2025-03-10_15-43-29.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/01..TreeTabLayout..EndeavourOS_Qtile_2025-03-10_15-43-29.png" width=300 /></a>

Currently, I often have more than three terminals open, so I use TreeTab Layout a lot, insted of VerticalTile Layout.  
However, I can't use functions such as moving between sections in TreeTab...I don't have the skills to do so and don't know how to write key bindings.

### VerticalTile Layout

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/02..VerticalTileLayout..01..single..EndeavourOS_Qtile_2025-03-10_15-44-34.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/02..VerticalTileLayout..01..single..EndeavourOS_Qtile_2025-03-10_15-44-34.png" width=300 /></a> <a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/02..VerticalTileLayout..02..many..EndeavourOS_Qtile_2025-03-10_15-44-54.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/02..VerticalTileLayout..02..many..EndeavourOS_Qtile_2025-03-10_15-44-54.png" width=300 /></a>

### Max Layout

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/03..MaxLayout..EndeavourOS_Qtile_2025-03-10_15-45-31.png">
<img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/03..MaxLayout..EndeavourOS_Qtile_2025-03-10_15-45-31.png" width=300 /></a>

### Floating, not Layout, but status, environment

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/04..floatlayout..EndeavourOS_Qtile_2025-03-10_16-35-39.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/04..floatlayout..EndeavourOS_Qtile_2025-03-10_16-35-39.png" width=300 /></a>

### ScratchPad DropDown

I don't know, but is it possible to share one terminal for both normal use and ScratchPad DropDown?  
In my case, I mainly use Kitty and use Alacritty for ScratchPad DropDown.

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/06..DropDown..EndeavourOS_Qtile_2025-03-11_07-57-55.png">
<img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/06..DropDown..EndeavourOS_Qtile_2025-03-11_07-57-55.png" width=300></a>


## My main usage:

The applications and built-in Layouts with Workspace, I use in this environment are as follows:

1. Workspace1: Kitty Terminal  
TreeTab, Max, VerticalTile layout.
2. Workspace2: Code OSS  
Max layout.
3. Workspace3: Brave Web Browser  
Max layout.
4. Another Workspace  
TreeTab, Max layout.

It looks like you might be able to choose which layouts to use for each workspace, but I don't have the skills to implement that.


## Additional information:

### Keyboard launcher is dmenu

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/05..dmenu..EndeavourOS_Qtile_2025-03-10_16-31-26.png"><img src="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/05..dmenu..EndeavourOS_Qtile_2025-03-10_16-31-26.png" width=300></a>

### Built-in Widgets

The date says "2025/R7" because it is the Japanese era name currently in use, "Reiwa/令和".  
And I created icons of [CurrentLayoutIcon](https://docs.qtile.org/en/latest/manual/ref/widgets.html#currentlayouticon) using `./scripts/convert_color_layout_icons.sh`.

<a href="https://github.com/dollplayer2501/dollplayer2501/blob/main/screenshot..qtile/_EndeavourOS_Qtile_2025-03-08_02-08-46_short.png">
<img src ="https://raw.githubusercontent.com/dollplayer2501/dollplayer2501/refs/heads/main/screenshot..qtile/_EndeavourOS_Qtile_2025-03-08_02-08-46_short.png" width=600></a>

### I'm making "Keybindings in images" available for use

Maybe because I installed it with `yay`, I'm not in an environment where I can use [Keybindings in images](https://docs.qtile.org/en/latest/manual/commands/keybindings.html).
However, I have forced it, `gen-keybinding-img` to work.
For example, I created `./bin/` and symbolically linked `/usr/bin/qtile` to it.
However, `KeyChord` doesn't seem to work effectively.




