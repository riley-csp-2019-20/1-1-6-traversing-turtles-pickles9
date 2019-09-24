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
  color = turtle_colors.pop()
  t.pencolor(color)
  t.fillcolor(color)
  my_turtles.append(t)

#  sets coordinate variables
startx = 0
starty = 0
count = 1
#goes right 45 and forward 50 for each turtle
for t in my_turtles:
    t.speed(1)
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(45 * count)     
    t.forward(50)
    startx = t.xcor()
    starty = t.ycor()
    count += 1

wn = trtl.Screen()
wn.mainloop()