# Importing
import pygame
import random
import math
from pygame import mixer

# Ship's Speed
speed_s = 10

# Ship's lives
ship_lives = 3

# Alien speed
speed_a = 3

# Bullet speed
speed_b = 20

# Wall-e
image = '1-MLOGb4V-pwtwDT-lnohTFg.bmp'

# Smoke
image1 = 'pngs/smoke.png'
image1_0 = pygame.image.load(image1)

# Initialize
pygame.init()

# Screen size
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load('Space-Invaders-Pygame-master/background.png')

# Background music
mixer.music.load('Songs/normal-music.wav')
mixer.music.play(-1)

# Winner background
w_background = pygame.image.load('pngs/pages/Untitled.png')

# Icon for game
icon = pygame.image.load('pngs/joystick.png')

# Ship
ship = pygame.image.load('pngs/ships/spaceship.png')

# Aliens
Alien_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 7
for i in range(number_of_enemies):
    # Alien Image
    Alien_image.append(pygame.image.load('pngs/enemys/ship.png'))
    # The aliens' random starting point
    enemyX.append(random.randint(0, 735))
    enemyY.append(50)
    # Defining the alien's moving points
    enemyX_change.append(speed_a)
    enemyY_change.append(40)

# The bullet
bullet_image = pygame.image.load('pngs/bullet.png')

# The main game area's that are covered
pygame.display.set_caption('©🌌Space Master☄©')
pygame.display.set_icon(icon)

# The player's starting point
playerX = 370
playerY = 480

# The bullets' starting point
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = speed_b
bullet_state = 'ready'

# Running
running = True

# Score
score_value = 0
font = pygame.font.Font('Fonts/GOUDYSTO.ttf', 20)
textX = 10
textY = 10

# You win
you_win = pygame.image.load('pngs/pages/Untitled.png')

# Smoke coordinate's
smokeX = 0
smokeY = 0


def smoke(x, y):
    g = playerX + 5
    smokeX = g
    smokeY = playerY
    screen.blit(image1_0, (x, y))


def choose():
    pass


def show_you_win():
    screen.blit(you_win, 0, 0)
    '''for event in pygame.event:
        if event.key == pygame.K_r:'''


# Score display
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Player
def player(x, y):
    screen.blit(ship, (x, y))


# Enemy
def alien(x, y, i):
    screen.blit(Alien_image[i], (x, y))


# Firing bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x + 16, y + 10))


def ifCollision(enemeyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemeyX - playerY, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 67:
        return True
    else:
        return False


# Collision detection
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 40:
        return True
    else:
        return False


# Defining the player's moving points
playerX_change = 0
playerY_change = 0

# Main loop
while running:
    # Color:     R, G, B
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background, (0, 0))

    # The player
    player(playerX, playerY)
    player(735, 2.5)
    player(665, 2.5)
    player(595, 2.5)
    # Events responding to 'key' messages
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        # If keystroke is pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = speed_s
                smoke(smokeX, smokeY)
                print("PRESSED RIGHT")

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -speed_s
                smoke(smokeX, smokeY)
                print("PRESSED LEFT")

            if event.key == pygame.K_q:
                quit()

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -speed_s
                smoke(smokeX, smokeY)
                print("PRESSED UP")

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = speed_s
                smoke(smokeX, smokeY)
                print("PRESSED DOWN")

            if event.key == pygame.K_c:
                print(f"X = {playerX}, Y = {playerY}")

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('Space-Invaders-Pygame-master/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    print("FIRED BULLET")

            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.key == pygame.K_o:
                print(f"This is the score: {score_value}")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                smoke(smokeX, smokeY)
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                smoke(smokeX, smokeY)
                playerY_change = 0

            if event.key == pygame.K_a or event.key == pygame.K_d:
                smoke(smokeX, smokeY)
                playerX_change = 0

            if event.key == pygame.K_w or event.key == pygame.K_s:
                smoke(smokeX, smokeY)
                playerY_change = 0

    # Player movements

    playerY += playerY_change
    playerX += playerX_change
    # Boundaries

    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    if playerY <= 2.5:
        exit()
        print('You win')

    if playerY >= 535:
        playerY = 535

    for i in range(number_of_enemies):
        # Aliens' movements
        enemyX[i] += enemyX_change[i]

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision with bullet
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('Space-Invaders-Pygame-master/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

            alien(enemyX[i], enemyY[i], i)

        elif playerY >= 836:
            playerY = 836

        # Collision with enemy
        ifcollison1 = ifCollision(enemyX[i], enemyY[i], playerX, playerY)
        if ifcollison1:
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = 50
            playerX = 370
            playerY = 480

        # The aliens
        alien(enemyX[i], enemyY[i], i)

    # Bullet firing
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(textX, textY)
    # Update screen
    pygame.display.update()

'''Created By Patrick Li©'''
