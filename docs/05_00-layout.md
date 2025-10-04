# Built-in Layouts


## Current Usage

The relationship between the currently used layout and workspace is shown below. Note that application and layout assignments other than those shown in the figure below have also been set, but they are omitted here.

<table>
  <tr><th>Screen</th><th>Group</th><th>label</th><th>Application</th><th>Layout</th></tr>
  <tr>
    <td rowspan="6">1</td>
    <td>1</td><td>1.terminal</td>
    <td>Kitty terminal</td>
    <td>TreeTab, VerticalTile</td>
  </tr>
  <tr>
    <td>2</td><td>2.code</td>
    <td>Code-oss</td>
    <td>Max</td>
  </tr>
  <tr>
    <td>3</td><td>3.web</td>
    <td>Brave-browser</td>
    <td>Max</td>
  </tr>
  <tr>
    <td>4</td><td>4.tool</td>
    <td>Thunar</td>
    <td>MonadWide, MonadTall</td>
  </tr>
  <tr>
    <td>5</td><td>5.misc</td>
    <td>Libreoffice</td>
    <td>Max</td>
  </tr>
  <tr>
    <td>9</td><td>9.null</td>
    <td>-</td>
    <td>Matrix</td>
  </tr>

  <tr>
    <td rowspan="2">2</td>
    <td>7</td><td>7.sub-1</td>
    <td>-</td>
    <td>Floating</td>
  </tr>
  <tr>
    <td>8</td><td>8.sub-2</td>
    <td>-</td>
    <td>Matrix</td>
  </tr>
</table>


## Layout Settings

I had two issues: I wanted to fix the layouts available on a workspace-by-workspace basis, and I wanted to use common settings. This wasn't possible with the existing [`./config.py`](../config.py) file alone. For this reason, I took the following steps:

- Layout settings are stored in [`./modules/layouts.py`](../modules/layouts.py)
- Settings for assigning layouts to workgroups are stored in [`./modules/groups.py`](../modules/groups.py)

As a side note, each screen has built-in widgets. These are also managed as separate files.


## Personal Impressions about tiling window manager

Here's what I currently do in a Qtile environment with a 1920x1080 resolution:

- Terminal work (no remote connections)
- Web browsing, including social media
- Program development using VS Code/Code OSS
- Gaming on Steam via Flatpak (very occasionally)

Basically, it's no exaggeration to say that there are almost no uses for tiling windows, as one might imagine with a "tiling window manager."


<!-- -->
