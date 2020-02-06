# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

# make it so if the player moves and hits a wall they lose 5 hp

def move(player, direction):
    x, y, hp = player
    xx, yy = direction
    if x + xx <= 9 and x + xx >= 0 and y + yy <= 9 and y + yy >= 0:
        x += xx
        y += yy
    else:
        hp -= 5
    return x, y, hp
