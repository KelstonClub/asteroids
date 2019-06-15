import random

WIDTH = 800
HEIGHT = 600
GUTTER = 0

directions = [(0, 1), (1, 0), (1, 1)]

rocks = []
for n in range(random.randint(3, 6)):
    rock = Actor("rock")
    rock.pos = random.randint(GUTTER, WIDTH-GUTTER), random.randint(GUTTER, HEIGHT-GUTTER)
    rock.direction = random.choice(directions)
    rocks.append(rock)

def update():
    screen.clear()
    for rock in rocks:
        dx, dy = rock.direction
        rock.x += dx
        rock.y += dy
        if rock.right < GUTTER:
            rock.left = WIDTH - GUTTER
        elif rock.left > WIDTH - GUTTER:
            rock.right = GUTTER
        if rock.bottom < GUTTER:
            rock.top = HEIGHT - GUTTER
        elif rock.top > HEIGHT - GUTTER:
            rock.bottom = GUTTER

def draw():
    for rock in rocks:
        rock.draw()
