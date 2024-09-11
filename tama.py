import time

class Tama():

  def __init__(self, health=0, is_alive=True, name="", body="🥚"):
    self.health = health
    self.is_alive = is_alive
    self.name = name
    self.body = body

  heart_icons = ["🤍🤍🤍🤍", "🩷 🤍🤍🤍", "🩷 🩷 🤍🤍", "🩷 🩷 🩷 🤍", "🩷 🩷 🩷 🩷 "]

  pet_icons = {"1": "🪱", "2": "🐓", "3": "🦔"}

  def set_body(self):
    body_choice = input(
        f"Choose pet type (type in number). Options: {self.pet_icons} ")

    if body_choice in self.pet_icons:
      self.body = self.pet_icons[body_choice]
    else:
      body_choice = input(
          f"Invalid input. Choose from one of the following options: {self.pet_icons} "
      )

  def print_health(self, additional_message=""):
    if self.health == -1:
      print(f"{self.body} {self.heart_icons[0]}  oh no")
    else:
      print(f"{self.body}  {self.heart_icons[self.health]} {additional_message}" )

  def set_name(self):
    self.name = input("Set name: ")

  def feed(self):
    if self.health < 4:
      self.health += 1
      self.print_health(f"{self.name} says 'Yum!'")
    else:
      self.print_health(f"{self.name} is already full ^_^")

  def go_hungry(self):
    if self.health >= 0:
      self.health -= 1
      self.print_health("*stomach gurgles*")
