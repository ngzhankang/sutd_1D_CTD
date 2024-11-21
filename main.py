from card import *

# import turtle

# screen = turtle.Screen()

# # image = r"(path).gif"

# # screen.addshape(image)
# # turtle.shape(image)

# turtle.done()

# module_taken = input("module taken")
# if module_taken == "Physical World" or "PW":
#     Mod = Module("10.015", module_taken, "12")

grade_dict = {"A+":5.3, "A":5.0, "A-":4.5, "B+":4.0, "B":3.5, "B-":3.0, "C+":2.5, "C":2.0, "C-":1.5, "D":1.0, "F":0.0}
grade = input("grade achieved")

total_credit = (grade_dict[grade]*12) + (grade_dict[grade]*12) + (grade_dict[grade]*12) + (grade_dict[grade]*12)
GPA = total_credit/(4*12)
print("Your GPA for this term is" , GPA)