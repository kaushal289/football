import pygame
import math
from pygame import mixer

# inilitiaze the pygame.
pygame.init()
clock = pygame.time.Clock()
# creating the screen.
screen = pygame.display.set_mode((800, 600))
# Putting Background image.
background = pygame.image.load("court.png")
# Caption and icon
pygame.display.set_caption("Football")
icon = pygame.image.load('football.png')
pygame.display.set_icon(icon)
# For creating the ball.
ballImg = pygame.image.load('football.png')
ballX = 384
ballY = 520
ballX_change = 20  # speed of ball.
ballY_change = 20
ball_state = 'ready'  # Ready-We cant see the ball
press = False
# arrow
arrow = pygame.image.load('arrow.png')
arrow_rect = arrow.get_rect(center=(420, 520))
angle = 0
angle_change = 1
angle_change_x = 0


# text box
base_font = pygame.font.Font(None, 32)
user_text = ""

# gloves adding
targetImg = pygame.image.load('crosshair.png')
targetX = 300
targetY = 350
targetX_change = 1
targetY_change = 50

fun=False
def target(x, y):
    screen.blit(targetImg, (x, y))
# for showing ball on screen.
def ball(x, y):
    screen.blit(ballImg, (ballX, ballY))


# for rotating
def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(410, 540))
    return rotated_surface, rotated_rect


# to shoot ball
def shoot_ball(x, y):
    global ball_state
    ball_state = "shoot"
    screen.blit(ballImg, (x, y))

def iscollision(targetX, targetY, ballX, ballY):
    distance = math.sqrt((math.pow(targetX - ballX, 2)) + (math.pow(targetY - ballY, 2)))
    if distance < 27:
        return True
    else:
        return False

# For game loop.
start = "true"
while start:

    # RGB =Red,Green,,Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # for closing the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

# for shooting the ball.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                angle_change_x = angle

            if event.key == pygame.K_SPACE:
                    shoot_ball(ballX, ballY)




    # For arrow to rotate.
    angle = angle_change + angle
    if angle == 60:
        angle_change -= 1
    elif angle == -60:
        angle_change += 1
    arrow_rotated, arrow_rotated_rect = rotate(arrow, angle)

    collision = iscollision(targetX, targetY, ballX, ballY)
    targetX += targetX_change
    if collision:
        ball_sound = mixer.Sound('impact.mp3')
        ball_sound.play()
        ballY = 480
        ball_state = 'ready'
    if targetX <= 250:
        gloveX_change = 2
        targetY += targetY_change
    elif targetX >= 500:
        targetX_change = -2
        targetY -= targetY_change
    # ball movement
    if ballY <= 0:
        ballY = 520
        ballX = 385
        ball_state = 'ready'
    if ball_state == "shoot":
        shoot_ball(ballX, ballY)
        if angle_change_x <= -40 and angle_change_x >= -60:
            ballY -= 6
            ballX += 10
        elif angle_change_x <= -20 and angle_change_x >= -40:

            ballY -= 8.2
            ballX += 6
        elif angle_change_x <= -5 and angle_change_x >= -20:

            ballY -= 13
            ballX += 3
        elif angle_change_x <= 5 and angle_change_x >= -5:

            ballY -= 7
            ballX += 0

        elif angle_change_x <= 20 and angle_change_x >= 5:

            ballY -= 8
            ballX += -1
        elif angle_change_x <= 40 and angle_change_x >= 20:

            ballY -= 10
            ballX += -3
        else:

            ballY -= 6
            ballX += -5
    target(targetX, targetY)
    screen.blit(arrow_rotated, arrow_rotated_rect)
    ball(ballX, ballY)
    # spped of arrow rotation.
    clock.tick(70)
    pygame.display.update()
