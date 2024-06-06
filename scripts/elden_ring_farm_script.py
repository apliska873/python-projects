from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time

time.sleep(5)
counter = 0

# Start the script sitting at the grace
while (True):
  # Leave grace
  press('q', 0.25)
  time.sleep(2)
  
  # Move forward
  press('w', 4.5)
  time.sleep(1)
  
  # Use ash of war of Sacred Relic Sword
  press('CTRL', 1)
  time.sleep(3)

  # Move backwards
  press('s', 4.77)

  time.sleep(1)
  
  # Sit at grace
  press('e', 0.25)
  
  counter += 1
  print("counter = " + str(counter))
  time.sleep(4)
  