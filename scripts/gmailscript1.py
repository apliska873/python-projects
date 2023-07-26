import webbrowser
import time
import os
import sys
import pyautogui as pag


url = "gmail.com"
email_to = "ajpliska873t.i@gmail.com"
subject = "test script"
msg = "This is a message that was totally not send by a python script."

# accessing webpage
webbrowser.open("url")
time.sleep(1)

for i in range(3):
      pag.moveTo(100, 100, duration=0.25)
      pag.moveTo(200, 100, duration=0.25)
      pag.moveTo(200, 200, duration=0.25)
      pag.moveTo(100, 200, duration=0.25)

pag.keyDown("w")
pag.keyUp("w")

pag.press("s")

# # the actual emailing part
# shell.SendKeys("c", 0)
# time.sleep(1)
# shell.SendKeys("email_to", 0)
# time.sleep(1)
# shell.SendKeys("{TAB}", 0)
# time.sleep(1)
# shell.SendKeys("{TAB}", 0)
# time.sleep(1)
# shell.SendKeys("subject", 0)
# time.sleep(1)
# shell.SendKeys("{TAB}", 0)
# time.sleep(1)
# shell.SendKeys("msg", 0)
# time.sleep(1)
# shell.SendKeys("{TAB}", 0)
# time.sleep(1)
# shell.SendKeys("{ENTER}", 0)