from PIL import Image
import turtle
import random

image_path = "MoleImage.png"
resized_image_path = "ResizedMoleImage.gif"

# open an image file
with Image.open(image_path) as img:
    img = img.resize((57, 70))
    # convert to gif
    img.save(resized_image_path, format='GIF')

# turtle screen
turtle_screen = turtle.Screen()
turtle_screen.setup(600, 600)
turtle_screen.screensize(600, 600)
turtle_screen.bgpic('GrassImage.png')

# add the resized image shape to the turtle screen
screen = turtle.Screen()
screen.addshape(resized_image_path)
mole = turtle.Turtle()
mole.shape(resized_image_path)
mole.penup()
mole.goto(0, 0)  # Initial position of the mole

# scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 250)  # Position the scoreboard at the top of the screen
scoreboard.color("red")
scoreboard.write("Score: 0", align="center", font=("Arial", 24, "normal"))
scoreboard_score = 0


def update_scoreboard():
    global scoreboard_score
    scoreboard.clear()
    scoreboard.write(f"Score: {scoreboard_score}", align="center", font=("Arial", 24, "normal"))

# Function to move the mole to a random position
def move_mole():
    x = random.randint(-280, 280)  # Random x-coordinate within screen bounds
    y = random.randint(-280, 230)  # Random y-coordinate within screen bounds
    mole.goto(x, y)


def mole_clicked(x, y):
    global scoreboard_score
    scoreboard_score += 1
    update_scoreboard()
    move_mole()

mole.onclick(mole_clicked)

update_scoreboard()

move_mole()

turtle.mainloop()
