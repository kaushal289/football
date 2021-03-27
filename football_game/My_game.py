import pygame

# inilitiaze the pygame.
pygame.init()
clock = pygame.time.Clock()
# creating the screen.
screen = pygame.display.set_mode((800, 600))
# Putting Background image.
background = pygame.image.load("court.png")
# Caption and icon
pygame.display.set_caption("Football")
icon = pygame.image.load('football-ball.png')
pygame.display.set_icon(icon)
# For creating the ball.
ballImg = pygame.image.load('football.png')
ballX = 384
ballY = 520
ballX_change = 20  # speed of ball.
ballY_change = 20
ball_state = 'ready'  # Ready-We cant see the ball
enter = False
press = False
# arrow
arrow = pygame.image.load('arrow.png')
arrow_rect = arrow.get_rect(center=(420, 520))
angle = 0
angle_change = 1
angle_change_x = 0

# For making the rectangular box.
input_rect = pygame.Rect(340, 210, 140, 32)  # 200,200 is the coordinate and 140,32 i sthe height and width of the box.
color = pygame.Color(100, 100, 100)
active = True
# text box
base_font = pygame.font.Font(None, 32)
user_text = ""
# For making the rectangular box in goal post.
input_rects = pygame.Rect(400, 300, 80, 25)  # 200,200 is the coordinate and 140,32 i sthe height and width of the box.
actives = True
# text box
base_fonts = pygame.font.Font(None, 32)
user_texts = 'apple'



def texts(x, y):
    screen.blit(user_texts, (x, y))


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
        # for pointing in the text box.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        # checks if any button is pressed.
        if event.type == pygame.KEYDOWN:
            if active == True:
                # for bakspace to delete the letter.
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode

        # FOR PRINTING THE TEXT OF USER.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                user_text = ""
                enter = True
                # for shooting the ball.
        if event.type == pygame.KEYDOWN:
            if enter == True:
                if event.key == pygame.K_SPACE:
                    press = True
                    angle_change_x = angle
        if event.type == pygame.KEYDOWN:
            if press == True:
                if event.key == pygame.K_SPACE:
                    shoot_ball(ballX, ballY)

    # to draw the rectangle text box.
    pygame.draw.rect(screen, color, input_rect, 2)
    # for text box and render it.
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))  # x+5 and y+5 to print in middle of text box.
    # to draw the rectangle text box in goal post.
    pygame.draw.rect(screen, color, input_rects, 1)
    # for text box in goal post to render.
    text_surfaces = base_fonts.render(user_texts, True, (255, 255, 255))
    screen.blit(text_surfaces, (input_rects.x + 10, input_rects.y + 5))

    # For arrow to rotate.
    angle = angle_change + angle
    if angle == 60:
        angle_change -= 1
    elif angle == -60:
        angle_change += 1
    arrow_rotated, arrow_rotated_rect = rotate(arrow, angle)
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

    screen.blit(arrow_rotated, arrow_rotated_rect)
    ball(ballX, ballY)

    # spped of arrow rotation.
    clock.tick(70)
    pygame.display.update()
