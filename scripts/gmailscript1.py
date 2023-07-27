import webbrowser
import time
import os
import sys
import pyautogui as pag

# mouse movement
"""for i in range(3):
      pag.moveTo(100, 100, duration=0.25)
      pag.moveTo(200, 100, duration=0.25)
      pag.moveTo(200, 200, duration=0.25)
      pag.moveTo(100, 200, duration=0.25)"""

print("sleeping")
time.sleep(5)

print("pressing W")
pag.keyDown("w")
time.sleep(5)
pag.keyUp("w")
print("pressing S")
pag.keyDown("s")
time.sleep(5)
pag.keyUp("s")
