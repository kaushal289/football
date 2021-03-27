import pygame
import math
from pygame import mixer

# initialize the pygame
pygame.init()
# creating the screen.
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('court.png')
# background sound
mixer.music.load('music.mp3')
mixer.music.play(-1)
# Caption and icon
pygame.display.set_caption("Football")
icon = pygame.image.load('football.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('football.png')
playerX = 70
playerY = 550
playerX_change = 0
# gloves adding
gloveImg = pygame.image.load('crosshair.png')
gloveX = 300
gloveY = 350
gloveX_change = 1
gloveY_change = 50
# arrow
arrowImg = pygame.image.load('arrow.png')
arrowX = 55
arrowY = 500
arrowX_change = 0
# ball
ballImg = pygame.image.load('football.png')
ballX = 0
ballY = 480
ballX_change = 0
ballY_change = 10
ball_state = "ready"
# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX = 350
textY = 150

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 80)


def show_score(x, y):
    score = font.render('Score:' + str(score_value), True, (25, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


def game_over_text():
    over_text = over_font.render("GaMe OvEr!!!!", True, (25, 255, 225))
    screen.blit(over_text, (130, 250))


def glove(x, y):
    screen.blit(gloveImg, (x, y))


def shoot_ball(x, y):
    global ball_state
    ball_state = "shoot"
    screen.blit(ballImg, (x + 0, y + 40))


def iscollision(gloveX, gloveY, ballX, ballY):
    distance = math.sqrt((math.pow(gloveX - ballX, 2)) + (math.pow(gloveY - ballY, 2)))
    if distance < 35:
        return True
    else:
        return False


def arrow(x, y):
    screen.blit(arrowImg, (x, y))


space = 0
# game loop

running = True
while running:
    # background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its any thing.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            if event.key == pygame.K_SPACE:

                if ball_state == "ready":
                    ball_sound = mixer.Sound('kick.mp3')
                    ball_sound.play()
                    space = space + 1
                    # gets the current x coordinates of the ball.
                    ballX = playerX
                    shoot_ball(334, 520)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arrowX_change = -3
            if event.key == pygame.K_RIGHT:
                arrowX_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                arrowX_change = 0
    angle = +1
    arrowX += arrowX_change
    playerX += playerX_change

    if playerX <= 165:
        playerX = 165
    elif playerX >= 600:
        playerX = 600
    if arrowX <= 150:
        arrowX = 150
    elif arrowX >= 585:
        arrowX = 585
    gloveX += gloveX_change
    player(playerX, playerY)
    # for glove
    if space - score_value > 4:
        game_over_text()

    if gloveX <= 250:
        gloveX_change = 2
        gloveY += gloveY_change
    elif gloveX >= 500:
        gloveX_change = -2
        gloveY -= gloveY_change
    # ball movement
    if ballY <= 250:
        ballY = 480
        ball_state = "ready"
    if ball_state == "shoot":
        shoot_ball(ballX, ballY)
        ballY -= ballY_change
        # collision
    collision = iscollision(gloveX, gloveY, ballX, ballY)
    if collision:
        ball_sound = mixer.Sound('impact.mp3')
        ball_sound.play()
        ballY = 480
        ball_state = 'ready'
        score_value += 1

    glove(gloveX, gloveY)
    arrow(arrowX, arrowY)
    show_score(textX, textY)
    pygame.display.update()
