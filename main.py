import time
import random
import threading
from tama import Tama
from inputimeout import inputimeout, TimeoutOccurred

pet = Tama(health=0)
pet.set_body()
pet.set_name()

def clock():
  # print(f"look at me! i love to process multiple threads simultaneously. yep {num}")
  # run_clock = True
  
  while True:
    time.sleep(1)
    print(f"{time.asctime()}")

def wait_for_input():
  try:
      something = inputimeout(prompt='press any key to feed', timeout=5)
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
  t1 = threading.Thread(target=pet_lifecycle)
  # t2 = threading.Thread(target=example_for_multithreading, args=([10]))
  t2 = threading.Thread(target=clock)
  
  t1.start()
  # t1.join()
  t2.start()
  
  t1.join()
  t2.join()
  
  print("Done!")

# pet_lifecycle()
