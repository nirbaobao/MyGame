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
enemy2_img = pygame.image.load(r'images\enemy2.png').convert_alpha()
enemy3_img = pygame.image.load(r'images\enemy3.png').convert_alpha()
enemy4_img = pygame.image.load(r'images\enemy4.png').convert_alpha()
enemy5_img = pygame.image.load(r'images\enemy5.png').convert_alpha()

# 设定参数
clock = pygame.time.Clock()
player = Player(plane_img,8,(200,600))
shoot_fre = 0
enemy_fre = 0
enemy_fre2 = 0
enemy2_hit = 0
pic_fre = 0
pic_fre2 = 0
enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
enemies2_down = pygame.sprite.Group()
running = True
score = 0
enemy_img_pack = [enemy3_img,enemy4_img,enemy5_img]

# 文字设置
font = pygame.font.SysFont('Calibri',30)
font2 = pygame.font.SysFont('Calibri',20)

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
        enemies2.empty()



# 敌人
    if enemy_fre % 40 == 0:
        enemy = Enemy(enemy_img_pack[random.randint(0,2)],random.randint(2,4),(random.randint(0,500),0))
        enemies.add(enemy)
    enemy_fre += 1
    if enemy_fre == 40:
        enemy_fre = 0


# 敌人2
    if enemy_fre2 % 200 == 0:
        enemy2 = Enemy(enemy2_img,1,(random.randint(0,480),0))
        enemies2.add(enemy2)
    enemy_fre2 += 1
    if enemy_fre2 == 200:
        enemy_fre2 = 0


# 敌人1击中
    for enemy in enemies:
        enemy.move()
        if pygame.sprite.collide_rect(enemy,player):
            enemy_down = Enemy(blow2_img,0,enemy.rect.midtop)
            enemies_down.add(enemy_down)
            enemies.remove(enemy)
            player.is_hit = True
        if enemy.rect.top > 766:
            enemies.remove(enemy)


# 敌人2击中
    for enemy2 in enemies2:
        enemy2.move()
        if pygame.sprite.collide_rect(enemy2,player):
            enemy2_down = Enemy(blow_img,0,enemy2.rect.midtop)
            enemies2_down.add(enemy2_down)
            enemies2.remove(enemy2)
            player.is_hit = True
        if enemy2.rect.top > 766:
            enemies2.remove(enemy2)

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
        for enemy2 in enemies2:
            if pygame.sprite.collide_rect(bullet,enemy2):
                enemy2_hit += 1
                player.bullets.remove(bullet)
            if enemy2_hit == 7:
                enemy_down2 = Enemy(blow_img,0,enemy2.rect.midtop)
                enemies2_down.add(enemy_down2)
                enemies2.remove(enemy2)
                enemy2_hit = 0
                if player.is_hit == False:
                    score += 1000
        if bullet.rect.bottom <0:
            player.bullets.remove(bullet)


# 敌机爆炸
    for enemy in enemies_down:
        if pic_fre % 20 == 0:
            enemies_down.remove(enemy)
            pic_fre = 0
        pic_fre += 1

    for enemy2 in enemies2_down:
        if pic_fre2 % 30 == 0:
            enemies2_down.remove(enemy2)
            pic_fre2 = 0
        pic_fre2 += 1

# 是否击中
    if player.is_hit == True:
        screen.blit(background,(0,0))
        screen.blit(blow_img,player.rect.topleft)
        die_text = font.render('Score:'+str(score),True,(225,68,21))
        restart_text = font2.render('Press SPACE to restart',True,(255,255,255))
        screen.blit(die_text,(210,400))
        screen.blit(restart_text,(180,440))
        screen.blit(die_img,(210,250))
    else:
        screen.blit(background,(0,0))
        player.bullets.draw(screen)
        enemies.draw(screen)
        enemies2.draw(screen)
        enemies_down.draw(screen)
        enemies2_down.draw(screen)
        screen.blit(player.img,player.rect.topleft)
        score_text = font.render('Score:'+str(score),True,(0,255,0))
        screen.blit(score_text,(0,0))

    pygame.display.update()



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
enemy2_img = pygame.image.load(r'images\enemy2.png').convert_alpha()
enemy3_img = pygame.image.load(r'images\enemy3.png').convert_alpha()
enemy4_img = pygame.image.load(r'images\enemy4.png').convert_alpha()
enemy5_img = pygame.image.load(r'images\enemy5.png').convert_alpha()

# 设定参数
clock = pygame.time.Clock()
player = Player(plane_img,8,(200,600))
shoot_fre = 0
enemy_fre = 0
enemy_fre2 = 0
enemy2_hit = 0
pic_fre = 0
pic_fre2 = 0
enemies = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
enemies2_down = pygame.sprite.Group()
running = True
score = 0
enemy_img_pack = [enemy3_img,enemy4_img,enemy5_img]

# 文字设置
font = pygame.font.SysFont('Calibri',30)
font2 = pygame.font.SysFont('Calibri',20)

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
        enemies2.empty()



# 敌人
    if enemy_fre % 40 == 0:
        enemy = Enemy(enemy_img_pack[random.randint(0,2)],random.randint(2,4),(random.randint(0,500),0))
        enemies.add(enemy)
    enemy_fre += 1
    if enemy_fre == 40:
        enemy_fre = 0


# 敌人2
    if enemy_fre2 % 200 == 0:
        enemy2 = Enemy(enemy2_img,1,(random.randint(0,480),0))
        enemies2.add(enemy2)
    enemy_fre2 += 1
    if enemy_fre2 == 200:
        enemy_fre2 = 0


# 敌人1击中
    for enemy in enemies:
        enemy.move()
        if pygame.sprite.collide_rect(enemy,player):
            enemy_down = Enemy(blow2_img,0,enemy.rect.midtop)
            enemies_down.add(enemy_down)
            enemies.remove(enemy)
            player.is_hit = True
        if enemy.rect.top > 766:
            enemies.remove(enemy)


# 敌人2击中
    for enemy2 in enemies2:
        enemy2.move()
        if pygame.sprite.collide_rect(enemy2,player):
            enemy2_down = Enemy(blow_img,0,enemy2.rect.midtop)
            enemies2_down.add(enemy2_down)
            enemies2.remove(enemy2)
            player.is_hit = True
        if enemy2.rect.top > 766:
            enemies2.remove(enemy2)

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
        for enemy2 in enemies2:
            if pygame.sprite.collide_rect(bullet,enemy2):
                enemy2_hit += 1
                player.bullets.remove(bullet)
            if enemy2_hit == 7:
                enemy_down2 = Enemy(blow_img,0,enemy2.rect.midtop)
                enemies2_down.add(enemy_down2)
                enemies2.remove(enemy2)
                enemy2_hit = 0
                if player.is_hit == False:
                    score += 1000
        if bullet.rect.bottom <0:
            player.bullets.remove(bullet)


# 敌机爆炸
    for enemy in enemies_down:
        if pic_fre % 20 == 0:
            enemies_down.remove(enemy)
            pic_fre = 0
        pic_fre += 1

    for enemy2 in enemies2_down:
        if pic_fre2 % 30 == 0:
            enemies2_down.remove(enemy2)
            pic_fre2 = 0
        pic_fre2 += 1

# 是否击中
    if player.is_hit == True:
        screen.blit(background,(0,0))
        screen.blit(blow_img,player.rect.topleft)
        die_text = font.render('Score:'+str(score),True,(225,68,21))
        restart_text = font2.render('Press SPACE to restart',True,(255,255,255))
        screen.blit(die_text,(210,400))
        screen.blit(restart_text,(180,440))
        screen.blit(die_img,(210,250))
    else:
        screen.blit(background,(0,0))
        player.bullets.draw(screen)
        enemies.draw(screen)
        enemies2.draw(screen)
        enemies_down.draw(screen)
        enemies2_down.draw(screen)
        screen.blit(player.img,player.rect.topleft)
        score_text = font.render('Score:'+str(score),True,(0,255,0))
        screen.blit(score_text,(0,0))

    pygame.display.update()



