import random

WIDTH = 800
HEIGHT = 600
GUTTER = 0

directions = [(1, 1), (-1, -1), (0.67, 1), (1, .67), (-.67, 1), (-1, .67)]

rocks = []
for n in range(random.randint(3, 6)):
    rock = Actor("rock")
    rock.pos = random.randint(GUTTER, WIDTH-GUTTER), random.randint(GUTTER, HEIGHT-GUTTER)
    rock.direction = random.choice(directions)
    rocks.append(rock)

def update():
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

        other_rocks = [r for r in rocks if r is not rock]
        index = rock.collidelist(other_rocks)
        if index != -1:
            collider = other_rocks[index]
            cx, cy = collider.direction
            ex = dx * cx
            ey = dy * cy
            rock.direction = ex, ey
            rock.x += 2 * ex
            rock.y += 2 * ey

def draw():
    screen.clear()
    for rock in rocks:
        rock.draw()
