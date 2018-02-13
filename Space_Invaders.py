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
    def __init__(self, image_name, Offence):
        super().__init__()
        self.image = pygame.image.load(image_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.score = Offence

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
ALIENS_FORMATION = {
    'resources\images\InvaderA.png': [220, 60], 
    'resources\images\InvaderB.png': [225, 100], 
    'resources\images\InvaderC.png': [220, 140]
    }

pygame.init()

pygame.mouse.set_visible ( False ) 
screen = pygame.display.set_mode(DIMENSIONS)
all_aliens = pygame.sprite.Group()
all_offence = pygame.sprite.Group()
player_goup = pygame.sprite.Group()
target_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()

for v in ALIENS_FORMATION.items():
    alien = Alien(v[0], -10)
    alien.rect.x = v[1][0]
    alien.rect.y = v[1][1]
    all_aliens.add(alien)

player = PlayerShip()
player.rect.x = 285
player.rect.y = 300
player_goup.add(player)

shot = Shot()
shot.rect = player.rect
shot_group.add(shot)

keys_pressed = { pygame.K_w: False, pygame.K_a: False, pygame.K_s: False, pygame.K_d: False, pygame.K_space: False }

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

    if keys_pressed[pygame.K_a]:
        Move.move_left(player)
    elif keys_pressed[pygame.K_d]:
        Move.move_right(player)
    elif keys_pressed[pygame.K_SPACE]:
        Move.move_up(shot)

    aliens_hit_list = pygame.sprite.spritecollide(player, all_aliens, True)
    for alien in aliens_hit_list:
        player.score += alien.score
        alien.kill()
    
    #if football:
        #football.update()


    screen.fill(WHITE)

    all_aliens.draw(screen)
    all_offence.draw(screen)
    player_goup.draw(screen)
    target_group.draw(screen)

    score_label = score_font.render("Score: {}".format(player.score), 1, WHITE)
    screen.blit(score_label, ((DIMENSIONS[0] / 2) - score_label.get_rect().width / 2, 10))

    pygame.display.flip()
