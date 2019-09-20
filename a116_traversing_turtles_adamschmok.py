#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  sets coordinate variables
startx = 0
starty = 0

#goes right 45 and forward 50 for each turtle
for t in my_turtles:
    t.speed(1)
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(45)     
    t.forward(50)

#	adds 50 to the start coordinates
    startx = startx + 50
    starty = starty + 50

wn = trtl.Screen()
wn.mainloop()