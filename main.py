import pygame
import csv
import random

def distort_text_once(l):
    distort_output_once = l
    random_x = random.randint(1, len(l) - 1)
    random_y = random.randint(1, len(l[1]) - 1)

    for temp in range(0, random_x):
        if distort_output_once[random_x][random_y] == 1:
            distort_output_once[random_x][random_y] = -1
        elif distort_output_once[random_x][random_y] == -1:
            distort_output_once[random_x][random_y] = 1

    return distort_output_once

def distort_text(d_character,distortion_scale):
    distort_output = d_character
    random_number = random.randint(1,distortion_scale)
    print("Approximate number of changes: ",random_number);
    for i in range(0,random_number):
        distort_output = distort_text_once(distort_output)
    return distort_output

def make_list(character):
    output = []
    for i in character:
        output = output + i

    return output

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
WIDTH = 20
HEIGHT = 20
 
MARGIN = 5

grid = []
for row in range(9):
    grid.append([])
    for column in range(7):
        grid[row].append(0)  # Append a cell

pygame.init()

WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Array Backed Grid")

done = False
clock = pygame.time.Clock()
a = [[-1 for i in range(0, 7)] for j in range(0, 9)]
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close

            for i in range(0, len(a)):
                for j in range(0, len(a[i])):
                    print(a[i][j], end='')
                print('\n', end='')

            for i in range(50):
                a = distort_text(a, 10)
                print(make_list(a))
                ###########    CHANGE FILEPATH HERE    ###############
                with open('D:\VIT-Academics\Academics V\Machine Learning\Assignment 2\dataset\\X.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(make_list(a))
                file.close()

            done = True 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            grid[row][column] = 1
            a[row][column] = 1
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(9):
        for column in range(7):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    clock.tick(60)
 
    pygame.display.flip()
 
pygame.quit()
