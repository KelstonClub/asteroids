WIDTH = 800
HEIGHT = 600

import math
spaceship = Actor("falcon")
print(spaceship.size)
spaceship.center = WIDTH/2, HEIGHT/2

spaceship.speed = 4
spaceship.angle = 0
spaceship.direction = 0, -1

#def on_key_down(key):
#    if key == keys.left:
#        pass
#    elif key == keys.right:
#        pass
#    elif key == keys.space:
#        pass

def on_key_up(key):
    pass

def update():
    dx, dy = spaceship.direction
    spaceship.move_ip(spaceship.speed * dx, spaceship.speed * dy)
    if keyboard.left:
        spaceship.angle += 8

        if spaceship.angle >= 360:
            spaceship.angle = 0
    if keyboard.right:
        spaceship.angle -= 8
        if spaceship.angle < 0:
            spaceship.angle = 360 + spaceship.angle
    spacex = math.sin(math.radians(spaceship.angle))
    spacey = math.cos(math.radians(spaceship.angle))
    print(spaceship.angle)
    print(int(spacex), int(spacey))
    spaceship.direction = -spacex, -spacey


    pass

def draw():
    screen.clear()
    spaceship.draw()
    pass

