import pygame
import os
from time import sleep

class MainHero:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= 4
        if keys[pygame.K_d]:
            self.hitbox.x += 4
        if keys[pygame.K_s]:
            self.hitbox.y += 4
        if keys[pygame.K_a]:
            self.hitbox.x -= 4
    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

class Enemy:
    def __init__(self, x, y, sprite_name, shiruna, vusota, speed):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.speed = speed
        self.hitbox.x = x
        self.hitbox.y = y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hitbox.y -= 4
        if keys[pygame.K_RIGHT]:
            self.hitbox.x += 4
        if keys[pygame.K_DOWN]:
            self.hitbox.y += 4
        if keys[pygame.K_LEFT]:
            self.hitbox.x -= 4

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

class Mission:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))


class Wall:
    def __init__(self, x, y, color, shiruna, vusota):
        self.hitbox = pygame.Rect(x, y, shiruna, vusota)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self, window):
         pygame.draw.rect(window, self.color, self.hitbox)

class Enemy_bot(Enemy):
    def movement(self):
        self.hitbox.x += self.speed
        if self.hitbox.x > 400:
            self.speed *= -1
        if self.hitbox.x < 232:
            self.speed *= -1



pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_obj, text_rect)


Mission = Mission(228, 355, "Mission.png", 65, 65)

background = pygame.image.load("background2.png")
background = pygame.transform.scale(background, [500, 500])

Hero = MainHero(55, 428,"sprite1.png", 50, 50)
enemy = Enemy_bot(300, 300,"sprite2.png", 50, 50, 1)


walls = []
walls.append(Wall(10, 50, [255, 0, 0], 100, 15))
walls.append(Wall(13, 66, [255, 0, 0], 15, 100))
walls.append(Wall(13, 255, [255, 0, 0], 15, 100))
walls.append(Wall(13, 160, [255, 0, 0], 15, 100))
walls.append(Wall(116, 230, [255, 0, 0], 15, 100))
walls.append(Wall(116, 270, [255, 0, 0], 15, 100))
walls.append(Wall(116, 330, [255, 0, 0], 15, 100))
walls.append(Wall(116, 360, [255, 0, 0], 15, 100))
walls.append(Wall(116, 137, [255, 0, 0], 15, 100))
walls.append(Wall(13, 66, [255, 0, 0], 15, 100))
walls.append(Wall(216, 140, [255, 0, 0], 100, 15))
walls.append(Wall(123, 140, [255, 0, 0], 100, 15))
walls.append(Wall(201, 50, [255, 0, 0], 100, 15))
walls.append(Wall(109, 50, [255, 0, 0], 100, 15))
walls.append(Wall(300, 50, [255, 0, 0], 100, 15))
walls.append(Wall(320, 50, [255, 0, 0], 100, 15))
walls.append(Wall(13, 350, [255, 0, 0], 15, 100))
walls.append(Wall(405, 65, [255, 0, 0], 15, 100))
walls.append(Wall(405, 165, [255, 0, 0], 15, 100))
walls.append(Wall(310, 249, [255, 0, 0], 100, 15))
walls.append(Wall(208, 254, [255, 0, 0], 15, 100))
walls.append(Wall(210, 249, [255, 0, 0], 100, 15))
walls.append(Wall(208, 334, [255, 0, 0], 15, 100))
walls.append(Wall(116, 457, [255, 0, 0], 15, 100))
walls.append(Wall(13, 449, [255, 0, 0], 15, 100))
walls.append(Wall(223, 420, [255, 0, 0], 100, 15))
walls.append(Wall(323, 420, [255, 0, 0], 100, 15))
walls.append(Wall(410, 355, [255, 0, 0], 15, 80))

game = True


main_game = pygame.mixer.Sound('jungles.ogg')
main_game.play()

while game:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    #оновлення
    Hero.movement()
    enemy.movement()

    #відмалювання
    window.fill((114, 141, 177))
    window.blit(background, (0, 0))
    Hero.draw(window)
    enemy.draw(window)
    Mission.draw(window)

    for wall in walls:
        if wall.hitbox.colliderect(Hero.hitbox):
            draw_text("You lose!!!", pygame.font.Font(None, 36), BLACK, window, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()
            lose = pygame.mixer.Sound('kick.ogg')
            lose.play()
            sleep(3)
            game = False
    if enemy.hitbox.colliderect(Hero.hitbox):
        draw_text("You lose!!!", pygame.font.Font(None, 36), BLACK, window, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        lose2 = pygame.mixer.Sound('kick.ogg')
        lose2.play()
        sleep(3)
        game = False
    if Hero.hitbox.colliderect(Mission.hitbox):
        draw_text("You win!!!", pygame.font.Font(None, 36), BLUE, window, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        win = pygame.mixer.Sound('money.ogg')
        win.play()
        sleep(3)
        game = False

    for wall in walls:
        wall.draw(window)

    pygame.display.flip()
    fps.tick(60)