import time
import random
import threading
from tama import Tama
# from inputimeout import inputimeout, TimeoutOccurred
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
  counter = 0
  
  while True:
    time.sleep(1)
    
    if counter < 4:
      counter += 1
    else:
      counter = 0
    
    # print(LINE_UP, end=LINE_CLEAR)
    print(f"{dummy_pet(counter)} \n {time.asctime()} \n isn't that neat? :) \n BOO!")
    clear_display(lines=4)

def wait_for_input():
  try:
      something = inputimeout(prompt='', timeout=5)
      if something:
        pet.feed()
  except TimeoutOccurred:
      pet.go_hungry()

def pet_lifecycle():
  while pet.is_alive:
    wait_for_input()
    
    if pet.health < 0:
      print(f"{pet.name} died :(")
      pet.is_alive = False

if __name__=="__main__":
  # t1 = threading.Thread(target=pet_lifecycle)
  # t2 = threading.Thread(target=example_for_multithreading, args=([10]))
  t2 = threading.Thread(target=clock)
  
  # t1.start()
  # t1.join()
  t2.start()
  
  # t1.join()
  t2.join()
  
  print("Done!")

# pet_lifecycle()
