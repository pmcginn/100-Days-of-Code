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
print("Welcome to Adventure Island!\n")
print("Your mission is to find a way off the island without having too much adventure. Most adventure is bad\n"
      "for the body and the soul.\n")
first_move = input("Your path forward is blocked, and the ocean is behind you. There is a path through the woods\n"
                   "to your right, and a creek a ways off to your left. Would you like to walk left or\n"
                   "right? \n").upper()[:1]
if first_move == "L":
    second_move = input("You turn left and walk until you reach the creek. The water is dark, and the creek looks\n"
                        "oddly foreboding. What would you like to do: swim, or wait? \n").upper()[:1]
    if second_move == "W":
        third_move = input("You sit down and wait, pondering your next move. As you do, a school of vicious trout\n"
                           "swim past. Once they leave, so does the foreboding air about the creek.\n\nYou swim to "
                           "the other side, and continue on until you encounter three doors: Red, Yellow, and Blue.\n\n"
                           "You feel irresistibly drawn to opening one of these doors. Which one do you "
                           "pick? \n").upper()[:1]
        if third_move == "R":
            print("You fling open the red door, and for the briefest moment you consider why the knob was warm to the\n"
                  "touch. This thought is cut short by a massive backdraft that immediately envelopes you, leaving\n"
                  "only a smoking pile of your bones.")
        elif third_move == "B":
            print("You walk through the blue door and are greeted by a slobbering bulldog with a kind face. You bend\n"
                  "to pet him, and he leaps to your jugular and tears out your throat. The betrayal hurts almost as\n"
                  "much as the dying.")
        elif third_move == "Y":
            print("After much deliberation, you open the yellow door. It is an ugly color, but beyond it is a\n"
                  "beautiful sight. You can see your ship in the distance, and look forward to returning to your \n"
                  "family so you can tell them about the trout.")
        else:
            print("This was not a time to get creative. You are immediately struck by a thunderbolt despite the clear\n"
                  "sky. The gods have punished you for your impudence, and you die.")
    else:
        print("You attempt to swim across the small creek, but are attacked by a school of murderous "
              "trout. You die, soggy.")
else:
    print("You have fallen into a hole and broken your leg. You will die here, alone.")
