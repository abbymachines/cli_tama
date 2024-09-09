import time
import random
from tama import Tama
from inputimeout import inputimeout, TimeoutOccurred

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
