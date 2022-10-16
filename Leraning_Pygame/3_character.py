import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

background = pygame.image.load("./image/Test_Background.png")

# 스프라이트(오브젝트) 불러오기

character = pygame.image.load("./image/character.png")

character_size = character.get_rect().size # 스프라이트 크기 가져오기 [0]은 가로, [1]은 세로크기
character_width = character_size[0] # 가로크기로 초기화
character_height = character_size[1] # 세로크기로 초기화

character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로 크기의 절반 크기에 x좌표 설정
character_y_pos = screen_height - character_height       # 화면 세로 크기로 y좌표 설정 
# 캐릭터가 중앙 아래 위치

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() 

pygame.quit()   