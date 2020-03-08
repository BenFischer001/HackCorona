# Needed to increment by seconds
import blocks
import charicters
import time
import pygame
import random

# Board Values Matrix
B = [['WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL', 'FD', 'FD', 'FD', 'WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'WL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'WL', 'WL'],
        ['WL', 'EX', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'QL', 'WL'],
        ['WL', 'EX', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'QL', 'WL'],
        ['WL', 'EX', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'QL', 'WL'],
        ['WL', 'WL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'WL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'CH', 'TB', 'CH', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'FL', 'CH', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL', 'RR', 'RR', 'RR', 'WL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'FL', 'WL'],
        ['WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL', 'WL']]
# Set of player values
P = ['P1','P2','P3','P4','P5']

completion = 0
prog = 1
incr = 0
measure1 = time.time()
measure2 = time.time()


# Display colors
wall,floor,chair,table = (224, 224, 209),(183, 183, 149),(153, 187, 255),(172, 115, 57)
# Sets the display
gameDisplay = pygame.display.set_mode((460,340))
# Size of each square
size = 20
# Board length and width
boardLength = 16
boardWidth = 22

all_sprites = pygame.sprite.Group()
P1 = charicters.player()
all_sprites.add(P1)
all_sprites.draw(gameDisplay)

i=0
while i <= boardLength:
        j = 0
        while j <= boardWidth:
                if B[i][j] == 'WL':
                    B[i][j] = blocks.wall()
                elif B[i][j] == 'FL':
                    B[i][j] = blocks.floor()
                elif B[i][j] == 'CH':
                    B[i][j] = blocks.chair()
                elif B[i][j] == 'TB':
                    B[i][j] = blocks.table()
                elif B[i][j] == 'FD':
                    B[i][j] = blocks.food()
                elif B[i][j] == 'RR':
                    B[i][j] = blocks.rr()
                elif B[i][j] == 'EX':
                    B[i][j] = blocks.expert()
                elif B[i][j] == 'QL':
                    B[i][j] = blocks.leave()
                j += 1
        i += 1

# Colors the board by the values in the matrix
i=0
while i <= boardLength:
        j = 0
        while j <= boardWidth:
            pygame.draw.rect(gameDisplay, B[i][j].color, [j * size, i * size, size, size])
            j += 1
        i += 1

# Updates the display for the colors
pygame.display.update()
# Sets the exit value as false
print(B[P1.x][P1.y].color)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if B[P1.y-1][P1.x].standable:
                    color = B[P1.y][P1.x].color
                    pygame.draw.rect(gameDisplay, color, [P1.x * 20, P1.y * 20, size, size])
                    P1.y -= 1
                    B[P1.y][P1.x].interact(P1)
                else:
                    B[P1.y-1][P1.x].interact(P1)
            elif event.key == pygame.K_DOWN:
                if B[P1.y+1][P1.x].standable:
                    color = B[P1.y][P1.x].color
                    pygame.draw.rect(gameDisplay, color, [P1.x * 20, P1.y * 20, size, size])
                    P1.y += 1
                    B[P1.y][P1.x].interact(P1)
                else:
                    B[P1.y+1][P1.x].interact(P1)
            elif event.key == pygame.K_RIGHT:
                if B[P1.y][P1.x+1].standable:
                    color = B[P1.y][P1.x].color
                    pygame.draw.rect(gameDisplay, color, [P1.x * 20, P1.y * 20, size, size])
                    P1.x += 1
                    B[P1.y][P1.x].interact(P1)
                else:
                    B[P1.y][P1.x+1].interact(P1)
            elif event.key == pygame.K_LEFT:
                if B[P1.y][P1.x-1].standable:
                    color = B[P1.y][P1.x].color
                    pygame.draw.rect(gameDisplay, color, [P1.x * 20, P1.y * 20, size, size])
                    P1.x -= 1
                    B[P1.y][P1.x].interact(P1)
                else:
                    B[P1.y][P1.x-1].interact(P1)
            P1.update()
        all_sprites.draw(gameDisplay)
        pygame.display.update()

    # Increments the completion bar while a character is on a chair position
    if B[P1.y][P1.x].name == 'chair' and measure2 - measure1 >= .2 and P1.hunger == 100 and P1.rr == 100 and P1.roadBlock == False:
        completion += 1
        measure1 = measure2
        measure2 = time.time()

        if completion % 10 == 0:
            situation = random.randint(0,16)
            print(situation)
            if situation == 16:
                P1.roadBlock = True
                P1.setColor((128, 0, 0))
                pygame.draw.rect(gameDisplay, (128, 0, 0), [P1.x * 20, P1.y * 20, size, size])
            elif situation > 11:
                P1.rr -= random.randint(10, 20)
                if P1.rr < 0:
                    P1.rr = 0
                P1.setColor((30,144,255))
                pygame.draw.rect(gameDisplay, (30,144,255), [P1.x * 20, P1.y * 20, size, size])
            elif situation >= 8:
                P1.hunger -= random.randint(10, 20)
                if P1.hunger < 0:
                    P1.hunger = 0
                P1.setColor((255, 140, 0))
                pygame.draw.rect(gameDisplay, (255, 140, 0), [P1.x * 20, P1.y * 20, size, size])

    else:
        measure2 = time.time()
    if completion > 100:
        pygame.init()
        white = (255, 255, 255)
        red = (230, 0, 0)
        display_surface = pygame.display.set_mode((460, 340))
        pygame.display.set_caption('Yippeeeeeee')
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('You Beat Coronavirus!', True, white, red)
        textRect = text.get_rect()
        textRect.center = (230, 170)
        while running:
            display_surface.fill(white)
            display_surface.blit(text, textRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    elif completion > 5.95 + incr:
        incr += 4.76
        prog += 1
    elif completion > 4.76 + incr:
        pygame.draw.rect(gameDisplay, (31, 31, 20), [prog * size, 0, size, size])
    elif completion > 3.57 + incr:
        pygame.draw.rect(gameDisplay, (61, 61, 41), [prog * size, 0, size, size])
    elif completion > 2.38 + incr:
        pygame.draw.rect(gameDisplay, (91, 91, 62), [prog * size, 0, size, size])
    elif completion > 1.19 + incr:
        pygame.draw.rect(gameDisplay, (152, 152, 103), [prog * size, 0, size, size])
    pygame.display.update()


    # check sneezes
    if P1.sneez == True:
        P1.sneez = False
        B[P1.y][P1.x].infectlvl += random.randint(0,P1.infeclvl)
        pygame.draw.rect(gameDisplay, (173,255,47), [P1.x * 20, P1.y * 20, size, size])
        pygame.draw.rect(gameDisplay, B[P1.y][P1.x].color, [P1.x * 20, P1.y * 20, size, size])

    if P1.out == True:
        pygame.draw.rect(gameDisplay, B[P1.y][P1.x].color, [P1.x * 20, P1.y * 20, size, size])
        P1.x = -1
        P1.y = -1
        P1.update()
        pygame.display.update()

    if P1.hunger == 100 and P1.rr == 100 and P1.roadBlock == False:
        P1.setColor((255, 0, 0))


i=0
while i <= boardLength:
        j = 0
        while j <= boardWidth:
            if B[i][j].infectlvl > 128:
                B[i][j].infectlvl = 128
            pygame.draw.rect(gameDisplay, (128-B[i][j].infectlvl, 128-B[i][j].infectlvl,128-B[i][j].infectlvl), [j * size, i * size, size, size])
            j += 1
        i += 1
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False