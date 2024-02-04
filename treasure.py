print("Welcome to treasure and hunt!")

choice_dir=input("Which direction you want to go left or right? ").lower()
if choice_dir == "left":
  choice_action=input("There is a river. You want to wait or swim? ").lower()
  if choice_action == "wait":
    choice_door=input("There are doors which door do you want to try? Red, Yellow, Blue ").lower()
    if choice_door == "red":
      print("Game Over.")
    elif choice_door == "yellow":
      print("You Win!")
    elif choice_door == "blue":
      print("Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Game Over")
else :
  print("Game Over")

