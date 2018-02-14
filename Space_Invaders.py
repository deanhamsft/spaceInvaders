import pygame
import sys
import random
import time
import math

class Move():
    def __init__(self):
        pass

    def move_up(self):
        self.rect.y -= 1
        pass

    def move_down(self):
        self.rect.y += 1
        pass

    def move_left(self):
        self.rect.x -= 1
        pass

    def move_right(self):
        self.rect.x += 1
        pass

def load_image(name):
    image = pygame.image.load(name).convert_alpha()
    return image

class Fire_Path():
    def __init__(self):
        pass

    def artilery(self, playership):
        velx=math.cos(playership.rect.x) * 10
        vely=math.sin(playership.rect.y) * 10
        playership.rect.x += velx
        playership.rect.y += vely
        pass

class Alien(pygame.sprite.Sprite):
    def __init__(self, image_name1, image_name2, Value):
        super().__init__()
        self.images = []
        self.index = 0
        self.images.append(load_image(image_name1))
        self.images.append(load_image(image_name2))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.score = Value

    def Drop(self):
        self.rect.y += 10

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        if self.rect.x >= 630:
            MARCH_RIGHT == False
            self.Drop()
        elif self.rect.x <= 10:
            MARCH_RIGHT == True
            self.Drop()

        if MARCH_RIGHT == True:
            self.rect.x += 20
        else:
            self.rect.x -= 20

        time_to_wait = 100

        

class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources\images\ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0

class Shot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources\images\shotFriendly.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect = pos

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (640, 480)
RADS = 0
ALIENS_FORMATION = [
    ['resources\\images\\InvaderA.png', 'resources\\images\\InvaderA1.png', [220, 60]],
    ['resources\\images\\InvaderB.png', 'resources\\images\\InvaderB1.png', [225, 100]], 
    ['resources\\images\\InvaderC.png', 'resources\\images\\InvaderC1.png', [220, 140]]
]
SHOTS = []
MARCH_RIGHT = True
time_to_wait = 100

pygame.init()

pygame.mouse.set_visible ( False ) 
screen = pygame.display.set_mode(DIMENSIONS)
all_aliens = pygame.sprite.Group()
all_offence = pygame.sprite.Group()
player_goup = pygame.sprite.Group()
target_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()

for v in ALIENS_FORMATION:
    for i in range(5):
        alien = Alien(v[0], v[1], 10)
        alien.rect.x = v[2][0] + (50 * i)
        alien.rect.y = v[2][1]
        all_aliens.add(alien)

player = PlayerShip()
player.rect.x = 285
player.rect.y = 300
player_goup.add(player)



keys_pressed = { pygame.K_w: False, pygame.K_a: False, pygame.K_s: False, pygame.K_d: False, pygame.K_SPACE: True, pygame.K_RIGHT: False, pygame.K_LEFT: False }

score_font = pygame.font.SysFont("monospace", 15)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in keys_pressed:
                keys_pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            if event.key in keys_pressed:
                keys_pressed[event.key] = False

    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        Move.move_left(player)
    elif keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        Move.move_right(player)
    elif not keys_pressed[pygame.K_SPACE]:
        shot = Shot()
        shot.rect.x = player.rect.x + 25
        shot.rect.y = player.rect.y 
        shot_group.add(shot)
        keys_pressed[pygame.K_SPACE] = True

    for shot in shot_group:
        Move.move_up(shot)
        aliens_hit_list = pygame.sprite.spritecollide(shot, all_aliens, True)
        for alien in aliens_hit_list:
            player.score += alien.score
            alien.kill()
            shot.kill()

    for alien in all_aliens:
        if time_to_wait == 0:
            alien.update()

    time_to_wait -= 1

    screen.fill(WHITE)

    all_aliens.draw(screen)
    all_offence.draw(screen)
    player_goup.draw(screen)
    target_group.draw(screen)
    shot_group.draw(screen)

    score_label = score_font.render("Score: {}".format(player.score), 1, WHITE)
    screen.blit(score_label, ((DIMENSIONS[0] / 2) - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
