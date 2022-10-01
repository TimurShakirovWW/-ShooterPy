from pygame import *
from random import randint
win_width = 500
window = display.set_mode((700, win_width))
display.set_caption("space")
background = transform.scale(image.load("REALspace.jpg"), (700, 500))
#clock = time.Clock()
#fps = 60
#clock.tick(fps)

game = True
finish = False
#mixer.init()
#mixer.music.load('space.ogg')
#fire1 = mixer.Sound('fire.ogg')
#mixer.music.play()
random1 = randint(100, 300)



p_s = 2
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet(GameSprite):
    def update(self):
        self.rect.y += -15
        if self.rect.y < 0:
            self.kill() 
        
    

class Player(GameSprite):
    def update(self): 
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x -= p_s - 8
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x += p_s - 8
    def fire(self):
        bullet1 = Bullet("bullet.png", player.rect.top, player.rect.centerx,5, 1, -15)
        bullets.add(bullet1)
lost = 0
monsters = sprite.Group()
bullets = sprite.Group()
font.init()
font = font.SysFont('Arial', 40)
ybityie2 = 0

    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        global lost
        if self.rect.y > 510:    
            self.rect.x = random1 = randint(80, 620)
            self.rect.y = 0
            lost += 1
            
player = Player("rocket.png", 300, 300, 100, 30, 10) 
for i in range(1, 6):
    enemy = Enemy("ufo.png",-40, randint(80, win_width - 80), 80, 50, randint(1, 5))
    monsters.add(enemy)


max_lost = 5
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                #fire1.play()
                player.fire()
    if finish != True:
        keys = key.get_pressed()
        window.blit(background, (0, 0))
        player.update()
        monsters.update()
        bullets.update() 
        player.reset()
        monsters.draw(window)
        bullets.draw(window)
        proshli = font.render("прошли мимо:" + str(lost), 1, (255, 255, 255))
        ybitye = font.render("убитые:" + str(ybityie2), True, (255, 255, 255))
        window.blit(proshli, (10, 50))
        window.blit(ybitye, (500, 50))
        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for i in sprites_list:
            ybityie2 += 1
            enemy = Enemy("ufo.png",-40, randint(80, win_width - 80), 80, 50, randint(1, 5))
            monsters.add(enemy)
        if sprite.spritecollide(player, monsters, False):
            finish = True 
        if sprite.spritecollide(player, monsters, False) or lost >= max_lost:
           finish = True 
           

        display.update()
    time.delay(50)
    
        
