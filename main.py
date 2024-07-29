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

# timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 220)
timer_turtle.color("blue")
game_time = 20

# start button
start_button_image_path = "startbutton.gif"
screen.addshape(start_button_image_path)

start_button = turtle.Turtle()
start_button.shape(start_button_image_path)
start_button.penup()
start_button.goto(0, 50)


def update_scoreboard():
    global scoreboard_score
    scoreboard.clear()
    scoreboard.write(f"Score: {scoreboard_score}", align="center", font=("Arial", 24, "normal"))

# update the timer
def update_timer():
    global game_time
    timer_turtle.clear()
    timer_turtle.write(f"Time: {game_time}s", align="center", font=("Arial", 24, "normal"))
    if game_time > 0:
        game_time -= 1
        screen.ontimer(update_timer, 1000)
    else:
        end_game()

# game over
def end_game():
    mole.hideturtle()
    scoreboard.clear()
    timer_turtle.clear()
    scoreboard.goto(0, 0)
    scoreboard.write(f"Game Over! Final Score: {scoreboard_score}", align="center", font=("Arial", 24, "normal"))


# Function to move the mole to a random position
def teleport_mole():
    x = random.randint(-280, 280)  # Random x-coordinate within screen bounds
    y = random.randint(-280, 230)  # Random y-coordinate within screen bounds
    mole.goto(x, y)
    screen.ontimer(teleport_mole, 200)

def mole_clicked(x, y):
    global scoreboard_score
    scoreboard_score += 1
    update_scoreboard()


def start_game(x, y):
    global game_time, scoreboard_score
    game_time = 20
    scoreboard_score = 0
    update_scoreboard()
    update_timer()
    teleport_mole()
    start_button.hideturtle()
    mole.showturtle()
    mole.onclick(mole_clicked)



start_button.onclick(start_game)


turtle.mainloop()
