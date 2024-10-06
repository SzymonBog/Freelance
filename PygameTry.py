import math

import pygame
import os
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 200)

bulletHitSound = pygame.mixer.Sound(os.path.join('Assets/Explosion.mp3'))
bulletFireSound =pygame.mixer.Sound(os.path.join('Assets/Laser.mp3'))

healthFont = pygame.font.SysFont('comicsans', 40)
winnerFont = pygame.font.SysFont('comicsans', 100)

fps = 60
vel = 5
bulletVel = 7
maxBullets = 3
asteroidVel = 4

spaceShipWidth, spaceShipHeight = 55, 40
asteroidWidth, asteroidHeight = 40, 40

asteroidHit = pygame.USEREVENT + 1
redHit = pygame.USEREVENT + 2


asteroidImage = pygame.image.load(os.path.join('Assets', 'asteroid.png'))
asteroid = pygame.transform.rotate(pygame.transform.scale(asteroidImage, (asteroidWidth, asteroidHeight)), 90)

redSpaceshipImage = pygame.image.load(os.path.join('Assets', 'redShipSquare.png'))
redSpaceship = pygame.transform.rotate(pygame.transform.scale(redSpaceshipImage, (spaceShipWidth, spaceShipHeight)), 270)


def drawWindow(red, redBullets, redHealth, asteroids, angle):
    WIN.fill(BLUE)

    redHealthText = healthFont.render("Health: " + str(redHealth), 1, WHITE)
    WIN.blit(redHealthText, (10, 10))

    rotated_red_spaceship = pygame.transform.rotate(redSpaceship, angle)
    red_center = redSpaceship.get_rect(center=redSpaceship.get_rect(topleft=(red.x, red.y)).center)

    WIN.blit(rotated_red_spaceship, red_center.topleft)
    WIN.blit(asteroid, (300, 300))

    for bullet in redBullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()


def handleYellowMovement(keysPressed, yellow):  # asteroid
    if keysPressed[pygame.K_a] and yellow.x - vel > 0:  # LEFT
        yellow.x -= vel
    if keysPressed[pygame.K_d] and yellow.x + vel + yellow.width < WIDTH:  # RIGHT
        yellow.x += vel
    if keysPressed[pygame.K_w] and yellow.y - vel > 0:  # UP
        yellow.y -= vel
    if keysPressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 5:  # DOWN
        yellow.y += vel


def handleRedMovement(keysPressed, red, angle):
    if keysPressed[pygame.K_LEFT]: # and red.x - vel > 0:  # LEFT
        angle += 5
    if keysPressed[pygame.K_RIGHT]: # and red.x + vel + red.width < WIDTH:  # RIGHT
        angle -= 5
    if keysPressed[pygame.K_UP]: # and red.y - vel > 0:  # UP
        red.x -= vel * math.cos(math.radians(angle))
        red.y += vel * math.sin(math.radians(angle))
    if keysPressed[pygame.K_DOWN]: # and red.y + vel + red.height < HEIGHT - 5:  # DOWN
        red.x += vel * math.cos(math.radians(angle))
        red.y -= vel * math.sin(math.radians(angle))
    return angle


def handleBullets(redBullets, red, asteroids):
    for astreoid in asteroids:
        astreoid.x += asteroidVel
        if red.colliderect(astreoid):
            pygame.event.post(pygame.event.Event(redHit))
            asteroids.remove(astreoid)

    for bullet in redBullets:
        bullet.x -= bulletVel
        for astreoid in asteroids:
            if bullet.colliderect(astreoid):
                pygame.event.post(pygame.event.Event(asteroidHit))
                redBullets.remove(bullet)
                asteroids.remove(astreoid)
                break


        #elif bullet.x > WIDTH:
         #   yellowBullets.remove(bullet)

    """for bullet in redBullets:
        bullet.x -= bulletVel
        if asteroid.colliderect(bullet):
            pygame.event.post(pygame.event.Event(asteroidHit))
            redBullets.remove(bullet)
        elif bullet.x < 0:
            redBullets.remove(bullet)"""


def main():
    angle = 90
    red = pygame.Rect(700, 300, spaceShipWidth, spaceShipHeight)
    redBullets = []
    redHealth = 1

    asteroids = []
    for i in range(5):
        asteroid = pygame.Rect(300, 300, asteroidWidth, spaceShipHeight)
        asteroids.append(asteroid)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # and len(yellowBullets) < maxBullets:
                    bullet = pygame.Rect(red.x, red.y, 10, 10)
                    redBullets.append(bullet)
                    bulletFireSound.play()

        keysPressed = pygame.key.get_pressed()

        angle = handleRedMovement(keysPressed, red, angle)

        handleBullets(redBullets, red, asteroids)

        drawWindow(red, redBullets, redHealth, asteroids, angle)


if __name__ == "__main__":
    main()
