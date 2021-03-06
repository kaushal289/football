import pygame
import math
from pygame import mixer

# initialize the pygame
pygame.init()
clock = pygame.time.Clock()
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
# Creating the ball.
ballImg = pygame.image.load('football.png')
ballX = 384
ballY = 520
playerX_change = 0
ball_state = 'ready'  ######not changed
# gloves adding
targetImg = pygame.image.load('crosshair.png')
targetX = 300
targetY = 350
targetX_change = 1
targetY_change = 50
# arrow
arrowImg = pygame.image.load('arrow.png')
arrow_rect = arrowImg.get_rect(center=(420, 520))
angle = 0
angle_change = 1
angle_change_x = 0

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX = 350
textY = 150

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 60)
again_font = pygame.font.Font('freesansbold.ttf', 40)

touch=0
def ball(ballX, ballY):
    screen.blit(ballImg, (ballX, ballY))
    touch = 0
    ball_state = 'shoot'
    if ballY <= 200:
        touch += 1
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

surface=0
# for rotating
def rotate(surface,angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle, 1)
    rotated_rect = rotated_surface.get_rect(center=(410, 540))
    return rotated_surface, rotated_rect


def game_over_text():
    score = font.render('Score:' + str(score_value), True, (25, 255, 255))
    screen.blit(score, (300, 100))
    over_text = over_font.render("GaMe OvEr!!!!", True, (25, 255, 225))
    screen.blit(over_text, (180, 250))
    again_text = again_font.render("PRESS ENTER TO PLAY AGAIN", True, (10, 200, 250))
    screen.blit(again_text, (110, 400))
    if touch > 2:
        screen.fill((105, 0, 0))
        game_over_text()
        pygame.mixer.stop()

def target(targetX,targetY):
    screen.blit(targetImg, (targetX, targetY))
    if targetX <= 250:
        targetX_change = 2
        targetY += targetY_change
    elif targetX >= 500:
        targetX_change = -2
        targetY -= targetY_change

press = True
def shoot_ball(x, y):
    global ball_state
    ball_state = "shoot"
    screen.blit(ballImg, (x, y))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            press = True
            angle_change_x = angle



def iscollision(targetX, targetY, ballX, ballY):
    distance = math.sqrt((math.pow(targetX - ballX, 2)) + (math.pow(targetY - ballY, 2)))
    if distance < 32:
        return True
    else:
        return False
    collision =iscollision(targetX, targetY, ballX, ballY)
    if collision:
        ball_sound = mixer.Sound('impact.mp3')
        ball_sound.play()
        ballX = 384
        ballY = 520
        ball_state = 'ready'
        score_value += 1




# game loop
start = True
while start:
    # background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    target(targetX,targetY)
    ball(ballX,ballY)
    shoot_ball(ballX,ballY)
    iscollision(targetX, targetY, ballX, ballY)
    game_over_text()
    clock.tick(70)
    pygame.display.update()