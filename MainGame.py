# -*- coding: utf-8 -*-

from planeRole import *
from pygame.locals import *
from sys import exit
import random

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((530,766))
pygame.display.set_caption('Hitting Fly')

# 载入图片
background = pygame.image.load(r'images\background.png').convert()
plane_img =  pygame.image.load(r'images\plane1.png').convert_alpha()
enemy_img = pygame.image.load(r'images\enemy1.png').convert_alpha()
bullet_img = pygame.image.load(r'images\bullet.png').convert_alpha()
blow_img = pygame.image.load(r'images\blow.png').convert_alpha()
die_img = pygame.image.load(r'images\mudeng.png').convert_alpha()
blow2_img = pygame.image.load(r'images\blow2.png').convert_alpha()


# 设定参数
clock = pygame.time.Clock()
player = Player(plane_img,8,(200,600))
shoot_fre = 0
enemy_fre = 0
enemy_fre2 = 0
pic_fre = 0
enemies = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
running = True
score = 0

# 文字设置
font = pygame.font.SysFont('Arial',30)

# 主循环
while running:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()

# 按键控制
    p_keys = pygame.key.get_pressed()
    if player.is_hit == False:
        if p_keys[K_w] or p_keys[K_UP]:
            player.moveup()
        elif p_keys[K_a] or p_keys[K_LEFT]:
            player.moveleft()
        elif p_keys[K_s] or p_keys[K_DOWN]:
            player.movedown()
        elif p_keys[K_d] or p_keys[K_RIGHT]:
            player.moveright()
    if p_keys[K_SPACE]:
        player.is_hit = False
        score = 0
        enemies.empty()
        player.bullets.empty()



# 敌人
    if enemy_fre % 20 == 0:
        enemy = Enemy(enemy_img,random.randint(3,5),(random.randint(0,510),0))
        enemies.add(enemy)
    enemy_fre += 1
    if enemy_fre == 20:
        enemy_fre = 0


# 敌人超出屏幕移除
    for enemy in enemies:
        enemy.move()
        if pygame.sprite.collide_rect(enemy,player):
            enemy_down = Enemy(blow2_img,0,enemy.rect.midtop)
            enemies_down.add(enemy_down)
            enemies.remove(enemy)
            player.is_hit = True
        if enemy.rect.top > 766:
            enemies.remove(enemy)

# 射击
    if shoot_fre % 10 == 0:
        player.shoot(bullet_img)
    shoot_fre += 1
    if shoot_fre == 10:
        shoot_fre = 0


# 子弹超出屏幕移除
    for bullet in player.bullets:
        bullet.move()
        for enemy in enemies:
            if pygame.sprite.collide_rect(bullet,enemy):
                enemy_down = Enemy(blow2_img,0,enemy.rect.midtop)
                enemies_down.add(enemy_down)
                enemies.remove(enemy)
                player.bullets.remove(bullet)
                if player.is_hit == False:
                    score += 100
        if bullet.rect.bottom <0:
            player.bullets.remove(bullet)


# 敌机爆炸
    for enemy in enemies_down:
        if pic_fre % 20 == 0:
            enemies_down.remove(enemy)
        pic_fre += 1

# 是否击中
    if player.is_hit == True:
        screen.blit(background,(0,0))
        screen.blit(blow_img,player.rect.topleft)
        die_text = font.render('Score:'+str(score)+'    Press SPACE to restart',True,(225,68,21))
        screen.blit(die_text,(100,400))
        screen.blit(die_img,(200,250))
    else:
        screen.blit(background,(0,0))
        player.bullets.draw(screen)
        enemies.draw(screen)
        enemies_down.draw(screen)
        screen.blit(player.img,player.rect.topleft)
        score_text = font.render('Score:'+str(score),True,(0,255,0))
        screen.blit(score_text,(0,0))

    pygame.display.update()



