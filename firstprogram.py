import os
# Functions and Recurssion
# n = int(input("Enter the number:"))

# def facts(n):
#   fact=1
#   for val in range(1, n+1, 1):
#     fact = fact * val
#   print(fact)
#   return fact

# facts(n)
# facts(5)
# facts(10)

# def cal_sum(a, b):
#    print(a + b) 
#    return a + b

# cal_sum(13,5)

# def print_hello():
#   print("Hello")


# print_hello()
# print_hello()
# print_hello()
# print_hello()

# list = [1,2,3,4,5,6,6,7,8,8,7,66,55]

# def cal_len(a):
#    print(len(a))
#    return 1

# def elem(a):
#   for val in range(0, len(a), 1):
#     print(a[val])

#   return 1

# n = int(input("Enter the number:"))

# def cal_fact(n):
#   fact  = 1
#   i=1
#   while(i < n+1):
#     fact = fact * i
#     i +=1
#   print(fact)
#   return 1

# def usdTOinr(n):
#    print(n * 90.20)
#    return n * 90.20 
# usdTOinr(n)

# print("Starting the program....")

# def show(n):
#   if(n == 0 ):
#     return 
#   print(n)
#   show(n-1) 

# def factorial(n):
#   if(n == 0 or n == 1):
#     return 1 
#   return factorial(n-1)*n
# print("Factorial :",factorial(7))

# n = int(input("Enter the number:"))

# def cal_sum(n):
#   if(n==0):
#     return 0
#   return n+cal_sum(n-1)

# print("Sum:", cal_sum(n))

# list = ["ayush", "arya"]


# def idx_list(n, list):
#   print("Index:", n, "List:", list)
#   if(n == 0):
#     print(list[n])
#     return list[n]
#   print(list[n])
#   idx_list(n-1, list)

# n = len(list) - 1

# idx_list(n, list)



# print("Ending....")

# f = open("demo.txt", "w")
# f.write("I am planning for masters")
# f.close()


# f= open("demo.txt", "r")
# data =f.read()
# print(data)

# with open("demo.txt" ,"r") as f :
#   data = f.read()
#   print(data)

# with open("demo.txt", "a") as f :
#   f.write("This is India")
#   f.close()

# with open("demo.txt" ,"r") as f :
#    data = f.read()
#    print(data)

# with open("demo.txt", "w") as f :
#   f.write("Hi everyone\n")
#   f.write("we are learning File I/O\n")
#   f.write("using Java\n")
#   f.write("I like programming in Java")
#   f.close()
# with  open("demo.txt", "r") as f :
#   data = f.read()
#   new_data = data.replace("Java", "Python")
#   print(new_data)
#   if(data.find("learning") != -1):
#     print("Found")
# class Student:
#    def __init__(self, fullname, lastname, marks):
#       print("Adding new Student in Databases....")
#       self.Firstname = fullname 
#       self.Lastname  = lastname
#       self.marks = marks
#       print("Added Successfully")
# s1 = Student("Ayush", "Ghole", 99) 
# print("Student:",s1.Firstname, s1.Lastname, "with marks:" , s1.marks)

# s2 = Student("Arya", "Ghole",  98)
# print("Student:", s2.Firstname, s2.Lastname,"with marks:", s2.marks)

class Student:
  def __init__(self, name, chemMks, mathMks, phyMks):
    self.name = name
    self.chemMarks = chemMks
    self.mathsMks = mathMks
    self.phyMks = phyMks
    print("Added Successfully")


s1 = Student("Ayush", 89, 98, 88)

def cal_avg(chemMks, mathsMks,  phyMks):
   return (chemMks + mathsMks + phyMks)/3

print(cal_avg(s1.chemMarks, s1.mathsMks, s1.phyMks))   