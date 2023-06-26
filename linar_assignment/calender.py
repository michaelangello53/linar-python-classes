"""import calendar
year=2023
month=5
print(calendar.month(year,month))"""


"""# Import turtle package
import turtle as turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('lightgreen')

	# Write the specified text in
	# specified font style and size
	pen.write("GeeksForGeeks", font=(
	"Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()"""




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
