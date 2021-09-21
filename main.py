# Ready to build the snake game?

'''Activity 1: Create the turtle'''
#Uncomment the statements below and click Run

import turtle           #Step 1: Import turtle module
wn=turtle.Screen()      #Step 2: Create a window to draw turtles
babbage=turtle.Turtle() #Step 3: Create a turtle and give it a name
babbage.shape("turtle") #Step 4: Set the shape of the turtle

#What did you observe?

'''Activity 2: Set the movement function'''

# To move, set the speed and the angle to turn
# Uncomment the statements below and provide a value between 10 and 20

move_speed = 15
turn_angle = 20

# To respond to an input from the keyboard, let us write the functions
# Uncomment the statements below:
# The forward function is done for you. Do the same for backward(), left() and right() functions

def forward():
 babbage.forward(move_speed)

def backward():
 babbage.backward(move_speed)


# Similarly, write code for moving backward.

def left():
 babbage.left(turn_angle)

def right():
 babbage.right(turn_angle)

# Similarly, write code for turning right.






'''Activity 3: Bind the arrow keys to the function'''
# To respond to an input from the keyboard, the arrow key needs to be linked to the functions you created in Activity 2
# Uncomment the statements below to bind the arrow keys to the functions
# Forward key is done for you- replicate it for left,right and down keys

wn.onkey(forward,"Up")

wn.onkey(backward,"Down")

wn.onkey(left,"Left")

wn.onkey(right,"Right")

# The onkey() function calls the respective functions when the arrow keys are pressed

'''Activity 4: Get the turtle to listen'''
# The final step is to get the turtle to listen to the key presses.
# This is achieved using the listen() function
# Uncomment the statement below and click Run

wn.listen()

# Now use the arrow keys and get the turtle moving.

'''Awesome!! You are now controlling the turtle movement'''