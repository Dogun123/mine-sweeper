import pygame

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)


size = [400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mine Sweeper")

done=False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

    screen.fill(WHITE)

    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 5)
    pygame.draw.polygon(screen, GREEN, [[30, 150], [125, 100], [220, 150]], 0)
    pygame.draw.lines(screen, RED, False, [[50, 150], [50, 250], [200, 250], [200, 150]], 5)
    pygame.draw.rect(screen, BLACK, [75, 175, 75, 50], 5)
    pygame.draw.rect(screen, BLUE, [75, 175, 75, 50], 0)
    pygame.draw.line(screen, BLACK, [112, 175], [112, 225], 5)
    pygame.draw.line(screen, BLACK, [75, 200], [150, 200], 5)

    pygame.display.flip()
