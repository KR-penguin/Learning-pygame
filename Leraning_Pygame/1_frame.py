from turtle import screensize
import pygame

pygame.init() # pygame 초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 480 # 화면 가로 크기
screen_height = 640 # 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # set_mode 함수로 화면 크기 설정

# 화면 제목(title) 설정

pygame.display.set_caption("Game") # 화면 제목 설정

# event loop

running = True # 게임이 진행중이다.

while running:
    for event in pygame.event.get(): # 어떤 event 가 발생하였는지 check
        if event.type == pygame.QUIT: # event 타입이 나가기라면 게임이 진행중이지 않을 것으로 초기화
            running = False

# pygame 종료

pygame.quit()