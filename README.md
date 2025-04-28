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
> On Linux, please install either `wl-clipboard` (Wayland) or `xclip` (X11), depending on your compositor.
> This guide uses `git`. Please install/initialize it if it's not already.

1. Clone Repo
Simply run:
```
git clone https://github.com/DatBogie/PyCalcBar && cd PyCalcBar
```

2. Venv
Simply run:
```
python3 -m venv .venv && pip3 install -r requirements.txt
```

3. Build
If on Linux, simply run:
```
./build-linux.sh
```
Otherwise:
	If on macOS, run:
```
pyinstaller main.py --onefile --noconsole --argv-emulation
```
	Else, run:
```
pyinstaller main.py --onefile --noconsole --argv-emulation
```
