import pygame
import sys
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player

def main():
    pygame.init()

    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroid = pygame.sprite.Group()

    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shot, updatable, drawable)

    clock= pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for aster in asteroid:
            for bullet in shot:
                if aster.collision(bullet):
                    aster.kill()
                    bullet.kill()
            if aster.collision(player):
                print("Game Over")
                sys.exit()
                

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
       
        
    


if __name__=="__main__":
    main()