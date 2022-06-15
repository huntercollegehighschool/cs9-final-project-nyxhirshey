"""
Name(s): Catinca Balasov and Nyx Hirshbein
Name of Project: The Adventure of the Labyrinth
"""

def start():
  print("For years, you have been peparing for this journey. At last, you find yourself before the fabled labyrinth - it towers menacingly, made of a rich black stone. Three paths lie ahead of you - one, a barren and empty desert, one that goes into a rocky canyon, and one a foggy, muddy terrain. Which path do you choose?")
  choice = input("Enter 1 for path1, 2 for path2, or 3 for path3.")
  if choice == "1":
    path1()
  if choice == "2":
    path2()
  elif choice == "3":
    path3()

def path1():
  print("Traveling through the desert, you encounter a gate with a sphinx guarding it. The sphinx gives a riddle: What has four legs in the morning, two at noon, and three in the evening? Do you respond: a man, a chair or an octopus?")
  choice = input("Enter a for man, b for chair, or c for octopus.")
  if choice == "a":
    a()
  if choice == "b":
    b()
  elif choice == "c":
    c()
 
def a():
  print("Your journey continues past the sphinxes. After hours of continuing through the sandy desert, the terrain begins to turn cold and chilly. Eventually you’re brought into a frosty tundra, and behind the haze of the falling snow, you can make out two gates. The one on the right reads The Gate of Truth and the one on the left reads The Gate without Doors. Do you go to the right or the left?")
  choice = input("Enter x for right and enter y for left.")
  if choice == "x":
    x()
  elif choice == "y":
    y()
  
def b():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()
    
def c():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def x():
  print("The Gate of Truth shows you your inner self, and with that enlightened knowledge, you are transported to the Gate without Doors and you are able to open the knobless door with no difficulty. You made it!")

def y():
  print("You try to open the door in vain. By now, the other gate has disappeared, and the labyrinth closes around you. Stranded in the cold, you die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def path2():
  print("You are cold and weary. Traversing along the side of a cliff. Within the canyon below, you see three large giants made of rock, sitting and talking at a campfire. Do you: befriend them, fight them, or run away from them?")
  choice = input("Enter d to befriend, enter e to fight, or enter f to run.")
  if choice == "d":
    d()
  if choice == "e":
    e()
  elif choice == "f":
    f()
  
def d():
  print("You join the rock giants at their campfire. They tell you that there is a cave at the end of the canyon, and in that cave is a treasure. Do you: stay with the rock giants or go find the treasure?")
  choice = input("Enter w to stay or v to go.")
  if choice == "w":
    w()
  elif choice == "v":
    v()

def e():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def f():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def w():
  print("You have decided that the most important treasures are the friends you made along the way. However, you are in an unknown land and you cannot be supported by your new friends forever. You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def v():
  print("You continue along the path until you find a cave. Within that cave, is a dragon. The dragon introduces itself as Zym. They carry you from the cave, you see the labyrinth from the sky and uncover all of its secrets. You completed your journey!")
  

def path3():
  print("You make your way through the swamp with great difficulty. Your feet through the boggy water, the farther you walk, the harder it is to move. You are almost paralyzaed, and you are completely hopeless. Do you: go back the way you came, stop where you are, or continue going?")
  choice = input("Enter g to leave, h to stop, or i to continue.")
  if choice == "g":
    g()
  if choice == "h":
    h()
  elif choice == "i":
    i()

def g():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def h():
  print("You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

def i():
  print("Your strength is restored and your hope is regained. The fog clears, and on one side of you is a stone, with a sword sunk into it, and on the other side of you is a cabin. Do you: grab the hilt and pull the sword from the stone or do you decide that you wish to rest before pulling out the sword?")
  choice = input("Enter z to pull out the sword or q to rest before completing your journey.")
  if choice == "z":
    z()
  if choice == "q":
    q()

def z():
  print("You place your hand on the hilt of the sword, close your eyes, and pull. The sword slides out smoothly and gleams in the air. The spirit of the sword, Moonchild, awakens and proclaims you ruler of the labyrinth. You feel the power of the labyrinth and its former rulers be granted unto you. You are worthy! The labyrinth is yours!")


def q():
  print("You go into the cabin and find a feast laid out before you. You suddenly realize how tired and malnourished you are. You stuff your face with food and soon after, fall asleep curled up by the fire, telling yourself you’re merely treating yourself after an arduous journey. Unfortunately, you have succumbed to material pleasures, and so, your journey must be cut short. You never awaken from your slumber. You die. Restart?")
  choice = input("Enter R to restart your journey.")
  if choice == 'R':
    def R(): 
      start()

    start()

start()
