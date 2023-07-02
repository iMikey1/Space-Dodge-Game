import pygame
import time
import random

pygame.init()
pygame.mixer.init()

screen_width = 960
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
Background = pygame.image.load("Images/Space Background.png")
pygame.display.set_caption("Space Dodge Game - 2023 Copyrighted by iMikey")
pygame.mixer.music.load("Musics/Chill Theme Song 1.mp3")
fontmain = pygame.font.SysFont("Dubai", 60, italic=False, bold=True)
fontsub = pygame.font.SysFont("Dubai", 55, italic=False, bold=True)
fontsub2 = pygame.font.SysFont("Dubai", 40, italic=False, bold=True)
fontsub3 = pygame.font.SysFont("Dubai", 25, italic=False, bold=True)
fontsub4 = pygame.font.SysFont("Dubai", 10, italic=False, bold=True)

title = fontmain.render("Space Dodge Game", True, (255, 255, 255))
statusText = fontsub.render("", True, (255, 255, 255))
scoreText = fontsub2.render("", True, (255, 255, 255))
ownerText = fontsub3.render("Originally by iMikey", True, (255, 255, 255))
helpText1 = fontsub3.render("Choose your difficulty", True, (255, 255, 255))
helpText2 = fontsub3.render("1 - Easy | 2 - Medium | 3 - Hard", True, (255, 255, 255))
copyrightText = fontsub4.render("2023 Copyrighted by iMikey", True, (255, 255, 255))
titlerect = title.get_rect()
statusTextrect = statusText.get_rect()
scoreTextrect = scoreText.get_rect()
ownerTextrect = ownerText.get_rect()
helpText1rect = helpText1.get_rect()
helpText2rect = helpText2.get_rect()
copyrightTextrect = copyrightText.get_rect()
titlerect.center = ((960//2, 300//2))
statusTextrect.center = ((960//2, 600//2))
scoreTextrect.center = ((200//2, 100//2))
ownerTextrect.center = ((960//2, 400//2))
helpText1rect.center = ((960//2, 475//2))
helpText2rect.center = ((960//2, 550/2))
copyrightTextrect.center = ((1790//2, 1170//2))

divisible10list = [10]

a = 10

for i in range(1, 100):
    a += 10
    divisible10list.append(a)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Asteroid1(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Asteroid2(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Asteroid3(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Asteroid4(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.display.get_surface().get_rect().center
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

def changeText(textName, Text, FontType, Color, TextRect, CenterWidth, CenterHeight):
    textName = FontType.render(Text, True, Color)
    TextRect = textName.get_rect()
    TextRect.center = (CenterWidth, CenterHeight)
    return textName, TextRect

asteroid1 = Asteroid1("Images/Asteroid.png")
asteroid1_x = 960
asteroid1_y = random.randint(70, 430)

asteroid2 = Asteroid2("Images/Asteroid.png")
asteroid2_x = 960
asteroid2_y = random.randint(70, 430)

asteroid3 = Asteroid3("Images/Asteroid.png")
asteroid3_x = 960
asteroid3_y = random.randint(70, 430)

asteroid4 = Asteroid4("Images/Asteroid.png")
asteroid4_x = 960
asteroid4_y = random.randint(70, 430)

spaceship = Spaceship("Images/Spaceship.png")
spaceship_x = 100
spaceship_y = spaceship.rect.y

def updateSpritesPosition():
    spaceship.update(spaceship_x, spaceship_y)
    asteroid1.update(asteroid1_x, asteroid1_y)
    asteroid2.update(asteroid2_x, asteroid2_y)
    asteroid3.update(asteroid3_x, asteroid3_y)
    asteroid4.update(asteroid4_x, asteroid4_y)

ready = 0
asteroid2_readyToGo = 0
asteroid3_readyToGo = 0
asteroid4_readytoGo = 0
score = 0
print("")
print("W/S UP/DOWN ARROWS KEYS - MOVEMENT")
print("M - MUTE MUSIC")
print("P - UNMUTE MUSIC")
print("ESC - STOP GAME")
print("Space Dodge Game - 2023 Copyrighted by iMikey")
print("")

run = False
intro = True
lvlChosen = 0

while intro == True:
    screen.fill((0, 0, 0))

    screen.blit(Background, (0, 0))
    screen.blit(title, titlerect)
    screen.blit(ownerText, ownerTextrect)
    screen.blit(copyrightText, copyrightTextrect)

    if not lvlChosen == 0:
        helpText1, helpText1rect = changeText(helpText1, "Click anywhere to play", fontsub4, (255, 255, 255), helpText1rect, (960//2), (450//2))
        screen.blit(helpText1, helpText1rect)
    elif lvlChosen == 0:
        screen.blit(helpText1, helpText1rect)
        screen.blit(helpText2, helpText2rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and lvlChosen == 0:
        lvlChosen = 1
    if keys[pygame.K_2] and lvlChosen == 0:
        lvlChosen = 2
    if keys[pygame.K_3] and lvlChosen == 0:
        lvlChosen = 3
    if pygame.mouse.get_pressed()[0] and not lvlChosen == 0:
        intro = False
        run = True

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

pygame.mixer.music.play()
MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)
pygame.mixer.music.set_volume(0.5)

if lvlChosen == 1:
    speed = 0.3
elif lvlChosen == 2:
    speed = 0.5
elif lvlChosen == 3:
    speed = 0.7

title, titlerect = changeText(title, "Space Dodge Game", fontmain, (255, 255, 255), titlerect, (960//2), (100//2))

while run == True:
    screen.fill((0, 0, 0))

    screen.blit(Background, (0, 0))
    screen.blit(spaceship.image, spaceship.rect)
    screen.blit(asteroid1.image, asteroid1.rect)
    screen.blit(asteroid2.image, asteroid2.rect)
    screen.blit(asteroid3.image, asteroid3.rect)
    screen.blit(asteroid4.image, asteroid4.rect)
    screen.blit(title, titlerect)
    screen.blit(scoreText, scoreTextrect)
    screen.blit(copyrightText, copyrightTextrect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        spaceship_y -= 0.5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        spaceship_y += 0.5
    if keys[pygame.K_ESCAPE]:
        exit()
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0)
    if keys[pygame.K_p]:
        pygame.mixer.music.set_volume(0.5)

    if spaceship_y > 500 or spaceship_y < 150:
        spaceship_y = 300
    if asteroid1_x < -120:
        asteroid1_x = 960
        asteroid1_y = random.randint(70, 430)
        score = score + 1
    if asteroid2_x < -120:
        asteroid2_x = 960
        asteorid2_y = random.randint(70, 430)
        score = score + 1
    if asteroid3_x < -120:
        asteroid3_x = 960
        asteroid3_y = random.randint(70, 430)
        score = score + 1
    if asteroid4_x < -120:
        asteroid4_x = 960
        asteroid4_y = random.randint(70, 430)
    if spaceship.rect.colliderect(asteroid1.rect) or spaceship.rect.colliderect(asteroid2.rect) or spaceship.rect.colliderect(asteroid3.rect) or spaceship.rect.colliderect(asteroid4.rect):
        if ready == 1:
            pygame.mixer.music.stop()
            statusText, statusTextrect = changeText(statusText, "You Lost", fontsub, (255, 0, 0), statusTextrect, (960//2), (600//2))
            screen.blit(statusText, statusTextrect)
            pygame.display.update()
            time.sleep(2)
            exit()
    if ready == 0:
        ready = 1
    if asteroid2_readyToGo == 0 and asteroid1_x <= 700:
        asteroid2_readyToGo = 1
    if asteroid3_readyToGo == 0 and asteroid2_x <= 700:
        asteroid3_readyToGo = 1
    if asteroid4_readytoGo == 0 and asteroid3_x <= 700:
        asteroid4_readytoGo = 1

    if asteroid3_readyToGo == 1:
        asteroid3_x -= speed
    if asteroid2_readyToGo == 1:
        asteroid2_x -= speed
    if asteroid4_readytoGo == 1:
        asteroid4_x -= speed
    asteroid1_x = asteroid1_x - speed

    updateSpritesPosition()
    if score in divisible10list:
        scoreText, scoreTextrect = changeText(scoreText, str(score), fontsub, (255, 255, 0), scoreTextrect, (200//2), (100//2))
    else:
        scoreText, scoreTextrect = changeText(scoreText, str(score), fontsub2, (255, 255, 0), scoreTextrect, (200//2), (100//2))
    pygame.display.update()

    time.sleep(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == MUSIC_END:
            pygame.mixer.music.play()
