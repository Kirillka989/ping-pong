from pygame import *
scr = display.set_mode((700,500))
display.set_caption("ping - pong")
fon = transform.scale(image.load("m.jpg"), (700,500))

class  GameSprite(sprite.Sprite):
    def __init__(self, picimage, sx,sy):
        super().__init__()
        self.image = transform.scale(image.load(picimage),(65,65))
        self.rect = self.image.get_rect()
        self.rect.x = sx
        self.rect.y = sy
    def reset(self):
        scr.blit(self.image, (self.rect.x,self.rect.y))


game = True
clock = time.Clock()
FPS = 60
ball = GameSprite("ping.jpg",450,450) 
dx = 5
dy = 3



class GameSprite2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -=5
        if keys_pressed[K_DOWN]:
            self.rect.y +=5
        
raketka = GameSprite2("rakenka.jpg", 100, 400)

while game:
    scr.blit(fon, (0 , 0))
    ball.rect.x += dx
    ball.rect.y -= dy
    if ball.rect.x > 650:
        dx *= -1
    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.x < 0:
        dx *= -1
    if ball.rect.y > 450:
        dy *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False


    ball.reset()
    raketka.reset()
    raketka.update()
    
    display.update() 
    clock.tick(FPS)
