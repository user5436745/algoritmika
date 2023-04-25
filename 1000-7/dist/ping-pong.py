from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed        

class Ball(GameSprite):
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y

#окно
win_width = 700
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('trava.jpg'), (win_width, win_height))

#надо
clock = time.Clock()
FPS = 60

speed_x = 5
speed_y = 5


roketka1 = Player('ufo.png', 10, 250, 30, 150, 8)
roketka2 = Player('asteroid.png', 670, 250, 30, 150, 8)

ball = Ball('galaxy.jpg', 350, 250, 30, 30, 3)

font.init()
font1 = font.SysFont('Times New Roman', 45, 10, 1)
lose100 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose200 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))

#цикл
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0,0))
        
        roketka1.update_l()
        roketka1.reset()

        roketka2.update_r()
        roketka2.reset()
        
        ball.reset()
        ball.update()

        if ball.rect.y > win_height-30 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(roketka1, ball) or sprite.collide_rect(roketka2, ball):
            speed_x *= -1

        if ball.rect.x < -30:
            finish = True
            window.blit(lose100, (200, 200))

        if ball.rect.x >= 730:
            finish = True
            window.blit(lose200, (200, 200))

        display.update()
        clock.tick(FPS)