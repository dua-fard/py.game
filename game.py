import random
import time

from pygame import mixer

import pygame

pygame.init()
assert pygame.get_init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car Race")
clock = pygame.time.Clock()
car_x = 350
car_y = 450
car_image = pygame.image.load('img/sportcar.png')
icon = pygame.image.load('img/car.png')
boom = pygame.image.load('img/boom.png')
pygame.display.set_icon(icon)
bg = pygame.image.load("img/backgr.png")
delta = 0
box_x, box_y, box_w, box_h = 0, 0, 0, 0

game_over = False


def draw_text(s):
    font = pygame.font.Font("freesansbold.ttf", 100)
    text = font.render(s, True, (255, 0, 0), )
    rect = text.get_rect()
    rect.center = (400, 200)
    display.blit(text, rect)


mixer.music.load('sound/321go.wav')
mixer.music.set_volume(0.7)
mixer.music.play()
time.sleep(0.5)
bgg = pygame.image.load("img/start.png")
s = ['3', '2', '1', 'GO!']
for i in range(len(s)):
    display.blit(bgg, (0, 0))
    draw_text(s[i])
    pygame.display.update()
    time.sleep(0.5)
pygame.mixer.init()
crash_sound = pygame.mixer.Sound('sound/car_sound.wav')
crash_sound.play()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta = -10
            if event.key == pygame.K_RIGHT:
                delta = 10
        if event.type == pygame.KEYUP:
            delta = 0

    if (box_x, box_y, box_w, box_h) == (0, 0, 0, 0) or box_y > 600:
        box_y = 0
        box_w = 50
        box_h = 50
        box_x = random.randrange(0, 800 - 30)
        box_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    box_y += 20

    car_x += delta

    display.blit(bg, (0, 0))
    pygame.draw.rect(display, box_color, (box_x, box_y, box_w, box_h))
    if not game_over:
        if car_x < 0:
            game_over = True

            car_x = 0
        if car_x > 800 - 99:
            game_over = True

            car_x = 800 - 99
        car_w = 99
        box_left = box_x
        box_right = box_x + box_w
        car_left = car_x
        car_right = car_x + car_w

        if box_y + box_h > car_y:
            if box_left < car_left < box_right or box_left < car_right < box_right:
                game_over = True
                display.blit(boom, (car_x - 100, car_y - 400))

        if game_over:
            draw_text("GAME OVER!!!")
            crash_sound.stop()
            mixer.music.load('sound/car-crash.wav')

            mixer.music.set_volume(0.7)
            mixer.music.play()

        display.blit(car_image, (car_x, car_y))
        pygame.display.update()
        clock.tick(60)
pygame.quit()
