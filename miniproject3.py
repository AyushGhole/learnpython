print("Welcome to my computer project")

playing = input("Do you want to play? ")

points = 0


if(playing.lower() == "yes"):
  print("----Start Playing----")
else:
   print("----Game Ended----")
   quit()

question1 = input("What does CPU stands for ? ")
if(question1.lower() == "central processing unit"):
   print("Correct Answer")
   points += 5
   
else:
   print("Oops!! Incorrect answer")
   points -= 5

question2 = input("What does GPU stands for ? ")
if(question2.lower() == "graphical processing unit"):
   print("Correct Answer")
   points += 5
else:
   print("Oops!! Incorrect answer")
   points -= 5

question3 = input("What does RAM stands for ? ")
if(question3.lower() == "random access memory" ):
   print("Correct Answer")
   points += 5
else:
   print("Oops!! Incorrect answer")
   points -= 5



print("You Scored : " , points)
print("----Game Ended----")