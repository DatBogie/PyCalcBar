# PyCalcBar
Simple Qt bar that shows the result of Python math expressions, written in Python.
<br>Yes, I know `eval()` is bad or whatever. Fight me. (Actually please don't―you'd probably win.)

> [!Note]
> This app is intended for use in tiling WMs à la hyprland or i3wm.
> Therefore, binaries are only provided for Linux.

# Building from Source
If you want to use this outside of Linux for some reason, this section is for you.

> [!Important]
> This app requires Python to be installed.
<br>On Linux, please install either `wl-clipboard` (Wayland) or `xclip` (X11), depending on your compositor.
> This guide uses `git`. Please install/initialize it if it isn't already.

1. Clone Repo
<br>Simply run:
```
git clone https://github.com/DatBogie/PyCalcBar && cd PyCalcBar
```

<br>2. Venv
<br>Simply run:
```
python3 -m venv .venv && pip3 install -r requirements.txt
```

<bR>3. Build
<br>If on Linux, simply run:
```
./build-linux.sh
```
Otherwise...
<br>**If on macOS, run:**
```
pyinstaller main.py --onefile --noconsole --argv-emulation
```
**If on Windows, run:**
```
pyinstaller main.py --onefile --noconsole --argv-emulation
```
