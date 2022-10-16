import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

background = pygame.image.load("../image/Test_Background.png")

background_X_pos = 0
background_Y_pos = 0

character = pygame.image.load("../image/character.png")

character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1] 

character_X_pos = screen_width / 2 - character_width / 2 
character_Y_pos = screen_height - character_height       

# 이동할 좌표
to_X = 0
to_Y = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키보드를 눌렀을 때 press
            if event.key == pygame.K_a: # a 키를 눌렀을 때
                to_X -= 1
            elif event.key == pygame.K_d: # d 키를 눌렀을 때
                to_X += 1
            elif event.key == pygame.K_w: # w 키를 눌렀을 때
                to_Y -= 1
            elif event.key == pygame.K_s: # s 키를 눌렀을 때
                to_Y += 1

        if event.type == pygame.KEYUP: # 키보드를 때면 멈춤
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_X = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_Y = 0

    character_X_pos += to_X
    character_Y_pos += to_Y     

    # 가로 경계값 처리

    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > screen_width - character_width:
        character_X_pos = screen_width - character_width

    # 세로 경계값 처리

    if character_Y_pos < 0:
        character_Y_pos = 0
    elif character_Y_pos > screen_height - character_height:
        character_Y_pos = screen_height - character_height


    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))

    pygame.display.update() 

pygame.quit()