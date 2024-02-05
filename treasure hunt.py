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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction=input("there's a three directional way in front of you, which way do you want to go?(LEFT OR RIGHT)")
direction_=direction.lower()
if direction_=="forward":
  fruit=input("you came across a gorilla,there are two options,either you feed him banana or apple,which one do you choose?")
  froot=fruit.lower()
  if froot=="banana":
    print("you are a good person,you won the game")
  else:
    print("GAME OVER\nyou are a bad person,gorilla killed you") 
elif(direction_=="left"):
  medium=input("you came across a river🌊,you can either swim or wait for a boat.what would you choose??swim or wait")
  madium=medium.lower()
  if medium=="wait":
    print("You reached to the bank safely,now go ahead😁\nyou reached to the ultimate death question💀☠☠")
    query=input("if you have an option to kill a child and get a lakh rupees or adopt the child and get nothing?,kill or adopt")
    qory=query.lower()
    if query==kill:
      print("GAME OVER\nyou are a bad person,you were punished in hellfire")
    else:
      print("you are a good person,you won the game")
  else:
    print("GAME OVER\nyou were eaten by a crocodile🐊🐊")
elif(direction_=="right"):
  dowhat=input("you bumped into a wall,you can either dig or go back to the start.what would you choose?""dig or go back")
  dowhhat=dowhat.lower()
  if dowhat=="dig":
    print("you died buried into the ground💀")
  else:
    print("play again")
else:
  print("invalid way to go")

  


