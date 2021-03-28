import pygame
import math
from pygame import mixer
# initialize the pygame
pygame.init()
clock = pygame.time.Clock()
# creating the screen.
screen = pygame.display.set_mode((800, 600))
#welcome text.
def welcome():
    football_font = pygame.font.Font('freesansbold.ttf', 60)
    welcome_font = pygame.font.Font('freesansbold.ttf', 60)
    football_text = football_font.render("FOOTBALL", True, (25, 255, 225))
    welcome_text = welcome_font.render("Welcome to the game", True, (25, 255, 225))
    screen.blit(football_text, (220, 100))
    screen.blit(welcome_text, (100, 200))
def main_menu():
    click = False
    start = True
    startImg = pygame.image.load('start1.jpg')
    while start:
        screen.blit(startImg, (0, 0))
        welcome()
        mx,my=pygame.mouse.get_pos()
        click_button=pygame.Rect(290,300,200,50)
        if click_button.collidepoint((mx,my)):
            if click:
                game()
        click_font = pygame.font.Font('freesansbold.ttf', 50)
        pygame.draw.rect(screen,(0,0,0,),click_button)
        click_text = click_font.render("click", True, (25, 255, 225))
        screen.blit(click_text, (290, 300))
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               start=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    start=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        clock.tick(70)

def game():
    running = True
    background = pygame.image.load('court.png')
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
        pygame.display.update()
        clock.tick(70)
main_menu()