from PIL import Image
import turtle

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
turtle.shape(resized_image_path)

# scoreboard
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 250)  # Position the scoreboard at the top of the screen
scoreboard.color("red")
scoreboard.write("Score: 0", align="center", font=("Arial", 24, "normal"))

turtle.mainloop()
