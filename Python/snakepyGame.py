#define a python function which is a classic snake game
#display playing field using pygame library

import pygame
import random

#initialize pygame
pygame.init()

#define colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#define display window size
display_width = 800
display_height = 600

#define display window
gameDisplay = pygame.display.set_mode((display_width, display_height))

#define display window title
pygame.display.set_caption('Snake')

#define display window clock
clock = pygame.time.Clock()

#define snake blocksize  

block_size = 20

#define snake speed
FPS = 15

#define font size
font = pygame.font.SysFont(None, 25)

#define snake function
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])

#define message function
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

#define game quit and program exit
def gameExit():
    pygame.quit()
    quit()

#game function
def gameLoop():
    gameExit = False
    gameOver = False

    #define initial x and y position of snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    #define initial move direction
    lead_x_change = 0
    lead_y_change = 0

    #define snake list to contain snake blocks
    snakeList = []
    snakeLength = 1

    #define random apple
    randomAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    randomAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            #if key is pressed
            if event.type == pygame.KEYDOWN:
                #if key is left arrow
                if event.key == pygame.K_LEFT:
                    #if key is pressed, change x direction of snake
                    lead_x_change = -block_size
                    #change y direction of snake to zero
                    lead_y_change = 0
                #if key is up arrow
                elif event.key == pygame.K_UP:
                    #if key is pressed, change y direction of snake
                    lead_y_change = -block_size
                    #change x direction of snake to zero
                    lead_x_change = 0
                #if key is right arrow
                elif event.key == pygame.K_RIGHT:
                    #if key is pressed, change x direction of snake
                    lead_x_change = block_size
                    #change y direction of snake to zero
                    lead_y_change = 0
                #if key is down arrow
                elif event.key == pygame.K_DOWN:
                    #if key is pressed, change y direction of snake
                    lead_y_change = block_size
                    #change x direction of snake to zero
                    lead_x_change = 0

            #if key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0

        #if snake hits boundary, game over
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        #change position of snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        #set game background as white
        gameDisplay.fill(white)

        #display apple
        pygame.draw.rect(gameDisplay, red, [randomAppleX, randomAppleY, block_size, block_size])

        #add each snake block to snakeList
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #create length of snake
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #game over if snake hits itself
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        #call snake function to create snake on screen
        snake(block_size, snakeList)

        #update display
        pygame.display.update()

        #define random location for apple
        randomAppleX = round(random.randrange(0, display_width - block_size) / block_size) * block_size
        randomAppleY = round(random.randrange(0, display_height - block_size) / block_size) * block_size

        #set new fps
        clock.tick(FPS)

    #quit game if gameExit is true
    gameExit = True
    pygame.quit()
    quit()

gameLoop()