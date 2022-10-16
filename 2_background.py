import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game")

# 배경 이미지 불러오기

background = pygame.image.load("D:/vsc python/pygame/image/Test_Background.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # screen.fill((0, 0, 255)) # RGB 값으로 채우기 가능
    screen.blit(background, (0, 0)) # 배경 그리기
    pygame.display.update() # 배경화면 다시그리기 (*중요! 없으면 배경이 나타나지 않음)

pygame.quit()   