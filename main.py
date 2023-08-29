import pygame
import ant as antClass
from time import time as epoh

pygame.init()

size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('')

clock = pygame.time.Clock()
fps = 40

ants = []
for i in range(50):
    ants += [(antClass.Ant(i + 125, size[1] - 12))]
    ants += [(antClass.Ant(i + 125, size[1] - 10))]
    ants += [(antClass.Ant(i + 125, size[1] - 8))]
    screen.set_at((i + 125, size[1] - 8), [255, 0, 0])

time = int(epoh())
frames = 0

fireplace = pygame.image.load('fireplace.png')
fireplace = pygame.transform.scale(fireplace, (300, 350))
screen.blit(fireplace, (0, 0))

mona_lisa = pygame.image.load('mona_lisa.jpg')
mona_lisa = pygame.transform.scale(mona_lisa, (50, 70))
screen.blit(mona_lisa, (210, 33))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()

    i = 0

    for ant in ants:
        if i < 50:
            screen.set_at((i + 125, size[1] - 8), [255, 0, 0])

        i += 1

        ant.update(screen)

    frames += 1

    if time != int(epoh()):
        pygame.display.set_caption('FPS {}'.format(frames))
        frames = 0
        time = int(epoh())

    pygame.display.update()
    clock.tick(fps)

