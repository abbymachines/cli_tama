import time
import random
import threading
from tama import Tama
from inputimeout import inputimeout, TimeoutOccurred
# import sys

pet = Tama(health=0)
pet.set_body()
pet.set_name()

LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'

def dummy_pet(count):
  if count == 0:
    return "🐛"
  elif count == 1:
    return "🐛 ❤️"
  elif count == 2:
    return "🐛 ❤️ ❤️"
  elif count == 3:
    return "🐛 ❤️ ❤️ ❤️"
  elif count == 4:
    return "🐛 ❤️ ❤️ ❤️ ❤️"

def clear_display(lines):
  for i in range(lines):
    print(LINE_UP, end=LINE_CLEAR)

def clock():
  # counter = 0
  
  while True:
    time.sleep(1)
    
    print(f"{pet.format_output()} \n {time.asctime()}")
    clear_display(lines=2)

def wait_for_input():
  try:
      something = inputimeout(prompt='', timeout=5)
      if something:
        pet.feed()
        clear_display(lines=1)
  except TimeoutOccurred:
      pet.go_hungry()
      clear_display(lines=1)

def pet_lifecycle():
  while pet.is_alive:
    wait_for_input()
    
    if pet.health < 0:
      print(f"{pet.name} died :(")
      pet.is_alive = False

if __name__=="__main__":
  t1 = threading.Thread(target=pet_lifecycle)
  t2 = threading.Thread(target=clock)
  
  t1.start()
  t2.start()
  
  t2.join()
  
  print("Done!")
