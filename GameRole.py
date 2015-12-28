# -*- coding: utf-8 -*-

import pygame

SCREEN_WIDTH = 530
SCREEN_HEIGHT = 766

# 子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,bullet_speed,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.speed = bullet_speed
        self.rect.midbottom = init_pos

    def move(self):
        self.rect.top -= self.speed


# 玩家
class Player(pygame.sprite.Sprite):
    def __init__(self,player_img,player_speed,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.img = player_img
        self.speed = player_speed
        self.rect = self.img.get_rect()
        self.rect.topleft = init_pos
        self.is_hit = False
        self.bullets = pygame.sprite.Group()
        self.img_index = 0

    def shoot(self,bullet_img):
        bullet = Bullet(bullet_img,10,self.rect.midtop)
        self.bullets.add(bullet)

    def moveup(self):
        if self.rect.top >0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def movedown(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = SCREEN_HEIGHT

    def moveleft(self):
        if self.rect.left >0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveright(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.right += self.speed
        else:
            self.rect.right = SCREEN_WIDTH


# 敌人
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_speed,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.speed = enemy_speed
        self.rect = self.image.get_rect()
        self.rect.midtop = init_pos
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed



