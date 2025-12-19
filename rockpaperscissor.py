import random 


score = 0
sysScore = 0

while True : 
  user_input= input("Enter your choice rock/paper/scissor and q to quit : ")
  choice = random.choice(["rock", "paper", "scissor"])
  if(user_input.lower() == "q"):
    print("You scored:", score, "and system score:", sysScore)
    break
  else:
     if(user_input.lower() == choice) : 
       print("You Won")
       score += 1
     else:
       print("Oops! You Lost.")
       sysScore += 1


