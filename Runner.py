import pygame

class Main_Hero:
    def __init__(self, x, y, sprite_name, shiruna, vusota):
        self.image = pygame.image.load(sprite_name)
        self.image = pygame.transform.scale(self.image, [shiruna,vusota])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def movement(self):
        keys = pygame.key.get_pressed()

        
pygame.init()

background = pygame.transform.scale(pygame.image.load("background.png"), (500, 500))
Hero = Main_Hero(100, 100,"sprite1.png", 50, 50)
Enemy = Main_Hero(300, 300,"sprite2.png", 50, 50)


main_color = (100, 255, 231)

pygame.display.set_caption("Forrest Gump")
spr1 = pygame.transform.scale(pygame.image.load("sprite1.png"), (50, 50))
spr2 = pygame.transform.scale(pygame.image.load("sprite2.png"), (50, 50))

spr1_rect = spr1.get_rect()


spr2_rect = spr2.get_rect()


spr1_rect = pygame.Rect(spr1_rect.x, spr1_rect.y, 45, 45)
spr2_rect = pygame.Rect(spr2_rect.x, spr2_rect.y, 45, 45)

window = pygame.display.set_mode((500, 500))

fps = pygame.time.Clock()

game_over = False

def movement1(spr1, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            Hero.hitbox.y -= 15
        if event.key == pygame.K_s:
            Hero.hitbox.y += 15
        if event.key == pygame.K_d:
            Hero.hitbox.x += 15
        if event.key == pygame.K_a:
            Hero.hitbox.x -= 15

def movement2(spr2 ,event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_t:
            Enemy.hitbox.y -= 15
        if event.key == pygame.K_g:
            Enemy.hitbox.y += 15
        if event.key == pygame.K_h:
            Enemy.hitbox.x += 15
        if event.key == pygame.K_f:
            Enemy.hitbox.x -= 15



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        movement2(spr1, event)
        movement1(spr2, event)

    if spr1_rect.colliderect(spr2_rect):
        game_over = True


    if game_over == True:
        pygame.quit()

        
    window.fill(main_color)

    window.blit(background , (0, 0))
    window.blit(Hero, (Hero.hitbox.x, Hero.hitbox.y))
    window.blit(Enemy, (Enemy.hitbox.x, Enemy.hitbox.y))

    pygame.display.flip()
    fps.tick(60)


