import time
import random
import threading
from tama import Tama
from inputimeout import inputimeout, TimeoutOccurred

def print_cube(num):
  print("Cube: {}" .format(num * num * num))

def print_square(num):
  print("Square: {}" .format(num * num))

if __name__=="__main__":
  t1 = threading.Thread(target=print_square, args=(10,))
  t2 = threading.Thread(target=print_cube, args=(10,))

# t1 = threading.Thread(target, args)
# t2 = threading.Thread(target, args)

  t1.start()
  t2.start()

  t1.join()
  t2.join()

print("Done!")

pet = Tama(health=0)
pet.set_body()
pet.set_name()

def wait_for_input():
  try:
      something = inputimeout(prompt='press any key to feed', timeout=5)
      if something:
        pet.feed()
  except TimeoutOccurred:
      pet.go_hungry()

while pet.is_alive:
  wait_for_input()

  if pet.health < 0:
    print(f"{pet.name} died :(")
    pet.is_alive = False
