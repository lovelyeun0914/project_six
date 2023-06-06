import time

import pyautogui as pyautogui
import pygame

# 초기화
pygame.init()

# screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

O_IMAGE_SIZE = 100
X_IMAGE_SIZE = 100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("오빠 나 어디가 달라졌어?")
clock = pygame.time.Clock()

# 이미지 로딩 및 크기 변경
people_image = pygame.image.load("img/wrong_picture.png")
people_image = pygame.transform.scale(people_image, (1000, 800))

o_image = pygame.image.load("img/check.png")
o_image = pygame.transform.scale(o_image, (O_IMAGE_SIZE, O_IMAGE_SIZE))
x_image = pygame.image.load("img/xxx.png")
x_image = pygame.transform.scale(x_image, (X_IMAGE_SIZE, X_IMAGE_SIZE))
complete_img = pygame.image.load("img/complete_btn.png")
complete_img = pygame.transform.scale(complete_img, (200, 200))
complete2_img = pygame.image.load("img/complete_btn2.png")
complete2_img = pygame.transform.scale(complete2_img, (200, 200))
what_text_img = pygame.image.load("img/what_text.png")
what_text_img = pygame.transform.scale(what_text_img, (100, 100))

pos = []

draw_right_list = [[570, 258, False], [539, 453, False]]


class button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                action()
        else:
            screen.blit(img_in, (x, y))


def next_stage():
    test = True
    while test:
        pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the function and continue execution
        screen.fill((255, 255, 255))
        # 작업한 스크린의 내용을 갱신하기
        pygame.display.flip()
        # fps 설정, while 구문안에 넣는다.
        clock.tick(5)


def next_stage_confirm():
    test = True
    if len(pos) < 2:
        screen.blit(what_text_img, [50, 50])
        pygame.display.flip()
        time.sleep(2)
        # delay = 2000  # 이미지를 표시할 시간 (밀리초 단위)
        # pygame.time.delay(delay)

    else:
        next_stage()


def draw_right_check(list, m_x, m_y):
    i = 0

    for chk_list in list:
        print(chk_list)
        if (chk_list[0] - 30) < m_x < (chk_list[0] + 30) \
                and (chk_list[1] - 10) < m_y < (chk_list[1] + 10):
            if not chk_list[2]:
                chk_list[2] = True
                pos.append([o_image, m_x - (O_IMAGE_SIZE / 2), m_y - (O_IMAGE_SIZE / 2)])
                return True
    return False


def mini_game():
    # 마우스 클릭 배열
    wrong_0 = 0
    wrong_1 = 0
    playing = True

    while playing:

        screen.fill((255, 255, 255))
        screen.blit(people_image, [0, 0])
        complete_btn = button(complete_img, 730, 580, 310, 300, complete2_img, 730, 580, next_stage_confirm)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                is_draw_right = draw_right_check(draw_right_list, mouse_x, mouse_y)
                if not is_draw_right:
                    screen.blit(x_image, [mouse_x - (X_IMAGE_SIZE / 2), mouse_y - (X_IMAGE_SIZE / 2)])

            if event.type == pygame.QUIT:
                pygame.quit()

        for mousepos in pos:
            screen.blit(mousepos[0], [mousepos[1], mousepos[2]])

        # 작업한 스크린의 내용을 갱신하기
        pygame.display.flip()
        # fps 설정, while 구문안에 넣는다.
        clock.tick(5)


mini_game()
