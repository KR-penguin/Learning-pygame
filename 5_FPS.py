import pygame


pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

# FPS
clock = pygame.time.Clock()

background = pygame.image.load("./image/Test_Background.png")

background_X_pos = 0
background_Y_pos = 0

character = pygame.image.load("./image/character.png")

character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1] 

character_X_pos = screen_width / 2 - character_width / 2 
character_Y_pos = screen_height - character_height       


to_X = 0
to_Y = 0

# 캐릭터 이동 속도
character_speed = 0.6

running = True

while running:
    dt = clock.tick(60) # 게임화면에 초당 프레임 수를 설정
    # print("dt : {0}".format(dt))
    # print("fps : " + str(clock.get_fps()))

# 스프라이트가 1초 동안 100 만큼 이동해야 한다고 가정
# 10 fps : 1초에 10번 동작 -> 1번에 10만큼 이동해야 함
# 20 fps : 2초에 20번 동작 -> 1번에 5만큼 이동해야 함

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a: 
                to_X -= character_speed
            elif event.key == pygame.K_d: 
                to_X += character_speed
            elif event.key == pygame.K_w: 
                to_Y -= character_speed
            elif event.key == pygame.K_s: 
                to_Y += character_speed
            if event.key == pygame.K_l:
                running = False

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_X = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_Y = 0

    character_X_pos += to_X * dt
    character_Y_pos += to_Y * dt

    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > screen_width - character_width:
        character_X_pos = screen_width - character_width

    if character_Y_pos < 0:
        character_Y_pos = 0
    elif character_Y_pos > screen_height - character_height:
        character_Y_pos = screen_height - character_height


    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))

    pygame.display.update() 

pygame.quit()