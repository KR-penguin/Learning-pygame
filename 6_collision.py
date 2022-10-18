import pygame
import random

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

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


enemy = pygame.image.load("./image/enemy.png")

enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 

enemy_X_pos = screen_width / 2 - enemy_width / 2 
enemy_Y_pos = screen_height / 2 - enemy_height / 2   

to_X = 0
to_Y = 0

enemy_to_X = 0
enemy_to_Y = 0

character_speed = 0.6

running = True

enemy_direction_decision = 0

while running:
    dt = clock.tick(60) 


    if enemy_direction_decision == 30:
        enemy_to_X = random.uniform(-0.6, 0.6)
        enemy_to_Y = random.uniform(-0.6, 0.6)
        enemy_direction_decision = 0
    else:
        enemy_direction_decision += 1

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


    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > screen_width - character_width:
        character_X_pos = screen_width - character_width

    if character_Y_pos < 0:
        character_Y_pos = 0
    elif character_Y_pos > screen_height - character_height:
        character_Y_pos = screen_height - character_height



    if enemy_X_pos < 0:
        enemy_X_pos = 0
    elif enemy_X_pos > screen_width - enemy_width:
        enemy_X_pos = screen_width - enemy_width

    if enemy_Y_pos < 0:
        enemy_Y_pos = 0
    elif enemy_Y_pos > screen_height - enemy_height:
        enemy_Y_pos = screen_height - enemy_height


    # 충돌 처리를 위한 rect 정보 업데이트

    character_rect = character.get_rect()
    character_rect.left = character_X_pos
    character_rect.top = character_Y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_X_pos
    enemy_rect.top = enemy_Y_pos

    # 충동 확인

    if character_rect.colliderect(enemy_rect):
        print("Game over!")
        running = False

    enemy_X_pos += enemy_to_X * dt
    enemy_Y_pos += enemy_to_Y * dt

    character_X_pos += to_X * dt
    character_Y_pos += to_Y * dt

    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))
    screen.blit(enemy, (enemy_X_pos, enemy_Y_pos))

    pygame.display.update() 

pygame.quit()