# Junior Code, made on 7-10-26

import pygame
import random as rd

pygame.init()

# VARIABLES
SpaceShipX = rd.randint(100,400)
SpaceShipY = 800

EnemyX1 = rd.randint(50,500)
EnemyY1 = rd.randint(50,500)

EnemyX2 = rd.randint(50,500)
EnemyY2 = rd.randint(50,500)

EnemyX3 = rd.randint(50,500)
EnemyY3 = rd.randint(50,500)

EnemyX4 = rd.randint(50,500)
EnemyY4 = rd.randint(50,500)

BulletX = SpaceShipX
BulletY = SpaceShipY

Fire = False

Screen = pygame.display.set_mode((600,900))
pygame.display.set_caption("SpaceShooters")
Clock = pygame.time.Clock()

Game = True
while Game:
    Screen.fill((0,0,0))
    SpaceShip = pygame.draw.rect(Screen,(255,255,255),(SpaceShipX,SpaceShipY,25,50))

    Enemy1 = pygame.draw.rect(Screen,(255,0,0),(EnemyX1,EnemyY1, 25,25))
    Enemy2 = pygame.draw.rect(Screen,(255,0,0),(EnemyX2,EnemyY2, 25,25))
    Enemy3 = pygame.draw.rect(Screen,(255,0,0),(EnemyX3,EnemyY3, 25,25))
    Enemy4 = pygame.draw.rect(Screen,(255,0,0),(EnemyX4,EnemyY4, 25,25))

    Bullet = 0

    BulletY += 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                SpaceShipX -= 10
            if event.key == pygame.K_d:
                SpaceShipX += 10
            if event.key == pygame.K_SPACE:
                Fire = True
    def Shoot():
        global Fire

        global Bullet

        global BulletX
        global BulletY

        global Enemy1
        global Enemy2
        global Enemy3
        global Enemy4

        global EnemyX1
        global EnemyY1
        global EnemyX2
        global EnemyY2
        global EnemyX3
        global EnemyY3
        global EnemyX4
        global EnemyY4

        if Fire == True:
            Bullet = pygame.draw.rect(Screen,(255,255,0),(BulletX,BulletY,15,25))
            BulletY -= 10
            if BulletY <= 0:
                Fire = False
                BulletX = SpaceShipX
                BulletY = SpaceShipY
            if Bullet.colliderect(Enemy1):
                EnemyX1 = rd.randint(50,500)
                EnemyY1 = rd.randint(50,500)
            elif Bullet.colliderect(Enemy2):
                EnemyX2 = rd.randint(50,500)
                EnemyY2 = rd.randint(50,450)
            elif Bullet.colliderect(Enemy3):
                EnemyX3 = rd.randint(50,500)
                EnemyY3 = rd.randint(50,500)
            elif Bullet.colliderect(Enemy4):
                EnemyX4 = rd.randint(50,500)
                EnemyY4 = rd.randint(50,500)     
    Shoot()
    Clock.tick(60)
    pygame.display.update()