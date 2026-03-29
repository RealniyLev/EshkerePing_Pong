from pygame import *
display.set_caption("PingPong")
window = display.set_mode((700, 500))
background = transform.scale(image.load('background.jpg'), (700, 500))
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ball = GameSprite("ball.jpg", 350,250, 25,25, 3)
rocket_left = GameSprite("rocketka.png", 0, 3, 50, 100, 3)
rocket_right = GameSprite("rocketka.png", 650, 398, 50, 100, 3)

clock = time.Clock()
game = True
while game:
    keys = key.get_pressed()
    for e in event.get():
        
        if e.type == QUIT:
            game = False 
        if keys[K_ESCAPE]:
            game=False 
    if keys[K_s]:
        rocket_left.rect.y += 10
    if keys[K_w]:
        rocket_left.rect.y -= 10
    if keys[K_UP]:
        if rocket_right.rect.y >= 0:
            rocket_right.rect.y -= 10 
    if keys[K_DOWN]:
        rocket_right.rect.y += 10
    window.blit(background, (0,0))
    ball.reset()
    rocket_left.reset()
    rocket_right.reset()
    clock.tick(60)
    display.update()