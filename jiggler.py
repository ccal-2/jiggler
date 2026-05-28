import pyautogui
import time

# Set the interval (in seconds) for how often you want to move the mouse
INTERVAL = 5  # Move the mouse every 5 seconds

try:
    print("Keeping Teams active. Press stop to end.")
    while True:
           # Get the current mouse position
        x, y = pyautogui.position()
        
        # Move the mouse slightly
        pyautogui.moveTo(x + 10, y)
        time.sleep(0.1)
        pyautogui.moveTo(x, y)

        # Wait for the interval
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("Script stopped.")
