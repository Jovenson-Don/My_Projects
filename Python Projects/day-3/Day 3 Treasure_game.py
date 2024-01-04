print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
straight = input("To start do you want to go left, right, or straight?\n")
if straight.lower() == ('straight'):
  cave = input("Good choice! Which option will you choose? Cave or boat?\n")
  if cave.lower() == ('cave'):
    red = input("Another good choice! No idea who's on that boat. Now its gets harder...which color door? green, yellow, red?\n")
    if red.lower() == ('red'):
        gun = input("Are you cheating? Another great choice! A giant bear is guarding the treasure. How you taking it down? sowrd, gun, grenade?\n")
        if gun.lower() == ('gun'):
          print("Winner winner chicken dinner! You won the battle and treasure!")
        elif gun.lower() == ('sword'):
          print("Game over! That bear not letting you get close!")
        else:
          print("Game over! When have you ever seen a grenade in a cave?")
    elif red.lower() == ('yellow'):
        print("You just got shot. Game over!")
    else:
        print("Just got eaten alive. You thought money was here?")
  else:
    print("Game over! Who gets on a random boat?")
else:
  print("Game over bot! Try again")