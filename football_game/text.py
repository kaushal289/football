# For making the rectangular box.
input_rect = pygame.Rect(340, 210, 140, 32)  # 200,200 is the coordinate and 140,32 i sthe height and width of the box.
color = pygame.Color(100, 100, 100)
active = True

# for pointing in the text box.

# checks if any button is pressed.

# FOR PRINTING THE TEXT OF USER.
if event.key == pygame.K_KP_ENTER:
    user_text = ""
    enter = True
 if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

if event.type == pygame.KEYDOWN:
    if active == True:
        # for bakspace to delete the letter.
        if event.key == pygame.K_BACKSPACE:
            user_text = user_text[0:-1]
        else:
            user_text += event.unicode
  # to draw the rectangle text box.
    pygame.draw.rect(screen, color, input_rect, 2)
    # for text box and render it.
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))  # x+5 and y+5 to print in middle of text box.