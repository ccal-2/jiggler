TEAMS MOUSE JIGGLER (jiggler.py)
================================

A lightweight, automated Python utility designed to prevent communication platforms like Microsoft Teams, Slack, or Zoom from shifting your status to "Away" while you are stepped away from your workstation. 

The script works by fetching your current cursor position, shifting it slightly to the right, and instantly returning it to its origin point at a customizable interval. This behavior effectively simulates micro-user activity without disrupting your setup or cluttering your screen with significant cursor drift.


FEATURES
--------
- Status Preservation: Keeps communication apps active by simulating continuous manual input.
- Micro-Movements: Moves the cursor by only 10 pixels and returns it immediately within 0.1 seconds, minimizing interference if you interact with the computer.
- Resource Efficient: Uses standard time delays to ensure minimal CPU and RAM usage.
- Graceful Termination: Intercepts standard termination signals to close cleanly without raising unhandled traceback exceptions.


HOW IT WORKS: FLOW ARCHITECTURE
--------------------------------
The following block outlines the operational logic of the script's core execution loop:

[ Start Script ]
       │
       ▼
[ Print Initialization Message ]
       │
┌──────┴────────────────────────┐
│  while True: Infinite Loop   │◄────────────────────────┐
└──────┬────────────────────────┘                        │
       │                                                 │
       ▼                                                 │
[ Fetch Current Mouse Coordinates (x, y) ]                │
       │                                                 │
       ▼                                                 │
[ Move Cursor to Accent Position (x + 10, y) ]           │
       │                                                 │
       ▼                                                 │
[ Pause for 0.1 Seconds ]                                │
       │                                                 │
       ▼                                                 │
[ Return Cursor to Original Coordinates (x, y) ]          │
       │                                                 │
       ▼                                                 │
[ Pause for Configured INTERVAL (5 Seconds) ]            │
       │                                                 │
       └─────────────────────────────────────────────────┘
       │
  (User presses Ctrl+C)
       │
       ▼
[ Catch KeyboardInterrupt ]
       │
       ▼
[ Print "Script stopped." ]
       │
       ▼
  [ End Script ]


CODE BREAKDOWN
--------------
import pyautogui
import time

INTERVAL = 5  # Configured interval in seconds

try:
    print("Keeping Teams active. Press stop to end.")
    while True:
        x, y = pyautogui.position()  # Records base coordinates
        pyautogui.moveTo(x + 10, y)  # Jiggles 10 pixels right
        time.sleep(0.1)               # Holds for visibility
        pyautogui.moveTo(x, y)       # Returns to origin
        time.sleep(INTERVAL)         # Internal loop cooling delay
except KeyboardInterrupt:
    print("Script stopped.")


REQUIREMENTS AND INSTALLATION
-----------------------------
Prerequisites:
This script requires Python 3.x and the pyautogui library, which interacts directly with your operating system's display server to track and manipulate hardware events.

Installation Steps:
1. Clone or Download the Script
   Save the Python script as jiggler.py in your local directory.

2. Install Dependencies
   Install the required pyautogui library using pip:
   pip install pyautogui

   *Note for Linux Users: Depending on your desktop environment, you may need to install additional dependency packages for screen management (such as scrot or Tkinter frameworks) as prompted by pyautogui.


USAGE
-----
To launch the utility, open your system terminal or command prompt, navigate to the directory containing your file, and execute:

python jiggler.py

Stopping the Script:
To terminate the execution loop cleanly, focus the active terminal window running the script and press:
- Ctrl + C (Windows/Linux/macOS)

The program will catch the interrupt signal, output "Script stopped.", and release system control smoothly.


CONFIGURATION
-------------
You can easily adjust how frequently the script runs by modifying the INTERVAL constant at the top of the file:

INTERVAL = 5  # Change this value to your preferred delay in seconds

- Lower intervals (e.g., 5 to 30) offer real-time assurance against aggressive status timeouts.
- Higher intervals (e.g., 60 to 120) consume fewer overall system resources and are less noticeable during split-attention tasks.


DISCLAIMER
----------
This utility is intended for personal productivity and status management purposes. Be mindful of your organization's internal IT policies and remote work monitoring guidelines regarding the use of automation scripts.
