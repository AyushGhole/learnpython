import random 


choice = random.choice(["rock", "paper", "scissor"])
score = 0
sysScore = 0

while True : 
  user_input= input("Enter your choice rock/paper/scissor : ")
  if(user_input.lower() == choice) : 
    print("You Won")
    score += 1
  else:
    print("Oops! You Lost.")
    sysScore += 1

