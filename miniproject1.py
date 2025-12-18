import random

# Generate the random number
radomNum = random.randint(1, 100)

print("------Start-----")

# While loop
while True:
  userChoice = input("Guess the target or enter Q to quit the game:")
  if(userChoice == "Q"):
    break


# Typecast the entered number into the int format 
  userNum= int(userChoice) 
  if(userNum == radomNum ):
    print("Success: Correct Guess!")
    break
  elif(userNum < radomNum):
    print("Guess was small . Take a bigger guess")
  else:
    print("Guess was Big . Take a smaller guess")


print("------GAME OVER------") 



