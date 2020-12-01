import sys
import pygame
from math import floor
from random import randint

pygame.init()

WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

screen = pygame.display.set_mode([WIDTH*SIZE,HEIGHT*SIZE])

pygame.display.set_caption("Mine Sweeper")


FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field,x_pos,y_pos):

    count = 0
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos,ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count

def open_tile(field, x_pos, y_pos):

    global OPEN_COUNT       #global 전역변수 지정해야 함수 안에서 수정 가능
    if CHECKED[y_pos][x_pos]:      #list나 dictionary는 global 선언 안해도 함수 안에서 사용 가능
        return
    
    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos,ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not (xpos==x_pos and ypos==y_pos):
                    open_tile(field,xpos,ypos)


def main():

    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!",True,(0,255,255))
    message_over = largefont.render("GAME OVER!!",True,(0,255,255))

    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2,HEIGHT*SIZE/2)
    game_over = False

    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0,WIDTH-1), randint(0,HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

    while True:
        
        screen.fill([0,0,0])
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE, ypos*SIZE,SIZE,SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(screen,(192,192,192), rect)

                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(screen,(225,225,0),rect)
                
                elif tile == OPENED:
                    count = num_of_bomb(field,xpos,ypos)
                    if count > 0:
                        num_image = smallfont.render("{}".format(count),True,(255,255,0))
                        screen.blit(num_image,(xpos*SIZE+10, ypos*SIZE+10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # mousebuttondown and pygame.event.get().button==1 이면 마우스 왼쪽 버튼
                xpos = floor(event.pos[0]/SIZE)                               # pygame.event.get().button==3 이면 마우스 오른쪽 버튼
                ypos = floor(event.pos[1]/SIZE)                               # floor: 버림
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field, xpos, ypos)
        
        
        for index in range(0,WIDTH*SIZE,SIZE):
            pygame.draw.line(screen,BLACK,(index,0),(index,HEIGHT*SIZE))

        for index in range(0,HEIGHT*SIZE,SIZE):
            pygame.draw.line(screen,BLACK,(0,index),(WIDTH*SIZE,index))

        if OPEN_COUNT == WIDTH*HEIGHT - NUM_OF_BOMBS:
            screen.blit(message_clear, message_rect.topleft)
        elif game_over:
            screen.blit(message_over, message_rect.topleft)



        pygame.display.update()
        FPSCLOCK.tick(12)

if __name__ == '__main__':
    main()
