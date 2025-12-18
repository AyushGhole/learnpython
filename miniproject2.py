import random
import string

charValues = string.ascii_letters + string.digits + string.punctuation

password_length = 12
val = random.choice(charValues)
# print(val)

password =""
for i in range(password_length):
   values = random.choice(charValues)
   password += values
   
print("Your randomly generated password:",password)