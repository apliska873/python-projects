import webbrowser
import time
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

url = "gmail.com"
email_to = "ajpliska873t.i@gmail.com"
subject = "test script"
msg = "This is a message that was totally not send by a python script.\nteehee"

# accessing webpage
webbrowser.open("url")
time.sleep(9)

# the actual emailing part
shell.SendKeys("c", 0)
time.sleep(1)
shell.SendKeys("email_to", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("subject", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("msg", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{ENTER}", 0)