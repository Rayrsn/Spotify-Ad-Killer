# Spotify Ad Killer

### <h2 align="center"> <i> <b> A Python script which automatically kills/blocks Spotify ads*</b> </i> </h2>
### <h4 align="center"> <b> ~~Currently in testing phase.~~</b> </h4>
### <h4 align="center"> <b> Stable </b> </h4>

<br>
* Only works on Windows
<hr>
<br>

## Disclaimer 
<h3> This is for testing purposes ONLY! </h3>
<h4> I don't know if anyone else has done this before. if they have, their script is probably better than mine.

## How does it work?
It checks for window name changes and it'll exit Spotify and relaunch it when Spotify  is playing anything that doesn't have "-" in the name.
(Every song on Spotify has that in the name)

## Why does it work
There's this known bug which let's you skip ads if you exit Spotify entirely and relaunch it.

## Installing Dependencies 
1. Make sure you have Python 3 installed.
2. First you have to install [VSCode Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)
3. Then extract the repository and open a terminal in that directory.
4. Run `python -m pip install -r requirements.txt` in the same directory.
5. And finally run `pip install --only-binary :all: psutil`

## Setting up and Running the script
1. Replace the `"SpotifyDir"` value with the directory of your Spotify executable.
2. Exit Spotify entirely (Ctrl + Shift + Q) or just pause the music.
3. Open the directory in your preferred terminal.
4. Run `python main.py`.

## Making an executable (.exe file)
1. Install Pyinstaller `pip install pyinstaller`.
2. Open the script directory in your preferred terminal.
3. Run this line of code `pyinstaller --icon=icon.ico --onefile --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" main.py`
4. Wait for the program to finish compiling the executable.
5. Your file is located in `dist` directory.
* You can replace any Spotify shortcut with this file. (But remember to change the `"SpotifyDir"` value.)
* If the executable exits with "Python38.dll not found" error, move the included Python38.dll to the directory.

  
## Warning
* ~~There is a limitation however, some ads don't change the window title to "Advertisement". I might design a system which detects those too but I'm lazy atm.~~
  
**The mentioned bug is fixed.**

## To-Do List
- [x] Fix the limitation.

## Questions
### If yall have any questions or just wanna talk, add me on [Discord](https://rayr.ml/LinkInBio) or use my username Rayr#6709 (this might change so it's better to just use the link)
