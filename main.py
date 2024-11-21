from classes.module import *

import turtle

screen = turtle.Screen()

image = r"(path).gif"

screen.addshape(image)
turtle.shape(image)

turtle.done()

module_taken = input("module taken")
Mod = Module("module taken")

grade = input("grade achieved")
if grade == "A":
    gpa_score = 5.0
elif grade == "B":
    gpa_score = 3.5
elif grade == "C":
    gpa_score = 2.0
elif grade == "D":
    gpa_score = 1.0
elif grade == "F":
    gpa_score = 0.0