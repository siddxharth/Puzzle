# Puzzle game by Siddharth (@siddxharth)

# Import packages
import pygame
import random

# Initialize Pygame module
pygame.init()

# Set Screen Icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Set Game Caption
pygame.display.set_caption("Puzzle")

# Set Screen Size
scr_size = (300, 300)
screen = pygame.display.set_mode(scr_size)

# Colors
WHITE = (255, 255, 255)
GREY = (230, 250, 230)
BLACK = (0, 0, 0)
BLUE = (55, 55, 200)

# Text
font = pygame.font.Font(pygame.font.get_default_font(), 20)

# Create a Tile class


class Tile():
    def __init__(self, x, y, val):
        self.loc_x = x
        self.loc_y = y
        self.val = val
        self.box = pygame.Rect(self.loc_x, self.loc_y, 100, 100)


# Create Tile objects
loc = {1: [0, 0], 2: [100, 0], 3: [200, 0], 4: [0, 100], 5: [100, 100],
       6: [200, 100], 7: [0, 200], 8: [100, 200], 9: [200, 200]}
tiles = []
for i in loc:
    t = Tile(loc[i][0], loc[i][1], i)
    tiles.append(t)
# Create empty tile
empty = loc[9]
emp_tile = Tile(empty[0], empty[1], -1)

# Swap Tiles
def swap():
    temp = i.box
    i.box = emp_tile.box
    emp_tile.box = temp

# Check for win situation


# Game Loop
run = True
screen.fill(GREY)
# print(loc)
for i in tiles:
    val = str(i.val)
    print("["+str(i.box[0])+","+str(i.box[1]) + "-" + val+']', end=", ")
print("\n")
while run:
    win = 0
    # Print Tiles
    for i in range(8):
        pygame.draw.rect(screen, BLUE, tiles[i].box)
        val_font = font.render(str(tiles[i].val), True, WHITE)
        screen.blit(val_font, (tiles[i].box.center))
    pygame.draw.rect(screen, GREY, emp_tile.box)

    # Check for events
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False
        # Check for win situation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print('checking for win')
        # On click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in tiles:
                    if i.box.collidepoint(event.pos):
                        # print(i.box, i.val)
                        if i.box.center[0] == emp_tile.box.center[0] and (i.box.center[1]-emp_tile.box.center[1] == 100 or emp_tile.box.center[1]-i.box.center[1] == 100):
                            if i.box.midtop == emp_tile.box.midbottom:
                                # print("Top swap")
                                swap()
                            elif i.box.midbottom == emp_tile.box.midtop:
                                # print("Bottom swap")
                                swap()
                        elif i.box.center[1] == emp_tile.box.center[1] and (i.box.center[0]-emp_tile.box.center[0] == 100 or emp_tile.box.center[0]-i.box.center[0] == 100):
                            if i.box.left == emp_tile.box.right:
                                # print("Left swap")
                                swap()
                            elif i.box.right == emp_tile.box.left:
                                # print("Right swap")
                                swap()
    pygame.display.flip()
for i in tiles:
    val = str(i.val)
    print("["+str(i.box[0])+","+str(i.box[1]) + "-" + val+']', end=", ")
