# Ideatron
![ideatron-small](https://user-images.githubusercontent.com/75689188/232279433-379836da-76ba-40fd-953e-2c2f1b8797a0.png)

Ideatron is a game idea generator made in Python. Initially made on the Scratch platform without a name (it was called just Game Idea Generator), the app was remade as a Python application by electrovoyage.#9148 in 2023. This application aims to be any game dev's tool of choice to pick game ideas.
## Features
* Game idea generation!
* Saving results to a file
* Exporting all generatable options to a file
* An about page
* A very basic GUI
* Modifying the lists
* Saving and loading the lists
## Building the application
To build the app, you will need:
* Tkinter
* PIL (pillow)
* Webbrowser
* os
* sys
* datetime
* random
* PyInstaller (to build an exe)
### Steps to build the app
* Clone or download this repository to a folder
* Open the command prompt
* Go to the folder where `ideatron.py` is located
* Run `py -m PyInstaller --noconsole --icon=media/ideatron.ico --noconfig ideatron.py`
* Copy `media/` to `dist/Ideatron/media/`
* Go to `[ideatron.py folder]/dist/Ideatron`
* Run `ideatron.exe`
#### Automatic building
In the repo there is a batch file called `build.bat`. Download the repo and run the script. It will automatically build everything for you, including copying the `media/` folder.
