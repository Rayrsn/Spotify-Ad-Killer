# Spotify Ad Killer

### <h2 align="center"> <i> <b> A Python script which automatically kills spotify ads</b> </i> </h2>
### <h4 align="center"> <b> Currently in testing phase.</b> </h4>

<br>
<hr>
<br>

## Disclaimer 
<h3> This is for testing purposes ONLY! </h3>
<h4> I don't know if anyone else has done this before. if they have, their script is probably better than mine.

## How does it work?
It checks for window name changes and it'll exit spotify and relaunch it when spotify is playing "Advertisement".

## Why does it work
There's this known bug which let's you skip ads if you exit spotify entirely and relaunch it.

## Installing Dependencies 
1. Make sure you have Python 3 installed.
2. Run `python -m pip install -r requirements.txt`.

## Setting up and Running the script
1. Replace the `"SpotifyDir"` value with the directory of your Spotify executable.
2. Exit Spotify entirely or just pause the music.
3. Open the directory in your preferred terminal.
4. Run `python main.py`.

## Making an executable (.exe file)
1. Install Pyinstaller `pip install pyinstaller`.
2. Open the script directory in your preferred terminal.
3. Run this line of code `pyinstaller --icon=icon.ico --onefile --hidden-import "pynput.keyboard._win32" --hidden-import "pynput.mouse._win32" main.py`
4. Wait for the program to finish compiling the executable.
5. Your file is located in `dist` directory.
* You can replace any spotify shortcut with this file. (But remember to change the `"SpotifyDir"` value.)

## Warning
* There is a limitation however, some ads don't change the window title to "Advertisement". I might design a system which detects those too but I'm lazy atm.

## To-Do List
- [ ] Fix the limitation.

## Questions
### If yall have any questions or just wanna talk, add me on [Discord](https://rayr.ml/LinkInBio) or use my username Rayr#6709 (this might change so it's better to just use the link)

