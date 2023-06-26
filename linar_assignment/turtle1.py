import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("pink")

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.fillcolor("red")
my_turtle.pensize(3)

# Draw the heart shape
my_turtle.begin_fill()
my_turtle.left(50)
my_turtle.forward(133)
my_turtle.circle(50, 200)
my_turtle.right(140)
my_turtle.circle(50, 200)
my_turtle.forward(133)
my_turtle.end_fill()

# Position the turtle to write "I love you"
my_turtle.penup()
my_turtle.goto(0, -50)
my_turtle.pendown()

# Write "I love you" in the middle of the heart
my_turtle.color("white")
my_turtle.write("I love you", align="center", font=("Arial", 20, "bold"))

# Hide the turtle
my_turtle.hideturtle()

# Exit on click
turtle.done()
