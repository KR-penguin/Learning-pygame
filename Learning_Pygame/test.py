import pygame

pygame.init()


screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

background = pygame.image.load("D:/vsc python/pygame/image/Test_Background.png")

background_X_pos = 0
background_Y_pos = 0

character = pygame.image.load("D:/vsc python/pygame/image/character.png")

character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1] 

character_X_pos = screen_width / 2 - character_width / 2 
character_Y_pos = screen_height - character_height       

# 이동할 좌표
to_X = 0
to_Y = 0

running = True

delay = 100
interval = 50
pygame.key.set_repeat(delay, interval)

while running:
    
    to_X *= 0.9
    to_Y *= 0.9

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: #키보드를 눌렀을 때 press
            if event.key == pygame.K_a: # a 키를 눌렀을 때
                to_X += -5
            elif event.key == pygame.K_d: # d 키를 눌렀을 때
                to_X += 5
            elif event.key == pygame.K_w: # w 키를 눌렀을 때
                to_Y += -5
            elif event.key == pygame.K_s: # s 키를 눌렀을 때
                to_Y += 5
     
    character_X_pos += to_X
    character_Y_pos += to_Y
    
    screen.blit(background, (background_X_pos, background_Y_pos))
    screen.blit(character, (character_X_pos, character_Y_pos))

    pygame.display.update() 

pygame.quit()