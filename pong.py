from pygame import *

bg_color = (200, 255, 255)
window_width = 600
window_height = 500
window = display.set_mode((window_width, window_height))
window.fill(bg_color)



class GameSprite(sprite.Sprite):
    def __init__(self, spriteimage, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(spriteimage), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, is_left_player=True, player_speed=4, width=50, height=150):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.is_left_player = is_left_player
    def move(self):
        if self.is_left_player:
            self.update_left()
        else:
            self.update_right()
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed





game = True
end = False
clock = time.Clock()
FPS = 60
ball_speed_x = 3 
ball_speed_y = 3

left_paddle = Player('paddle.jpg', 30, 200, True)
right_paddle = Player('paddle.jpg', 520, 200, False)
ball = GameSprite('ball.jpg', 200, 200)

font.init()
style = font.Font(None, 35)
lose1 = style.render('Left Player Loses!', True, (180, 0, 0))
lose2 = style.render('Right Player Loses!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not end:
        window.fill(bg_color)
        left_paddle.move()
        right_paddle.move()
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if sprite.collide_rect(left_paddle, ball) or sprite.collide_rect(right_paddle, ball):
            ball_speed_x *= -1
            ball_speed_y *= 1
        if ball.rect.y > window_height - 50 or ball.rect.y < 0:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (150, 200))
            game_over = True
        if ball.rect.x > window_width:
            finish = True
            window.blit(lose2, (150, 200))
            game_over = True
            
        left_paddle.reset()
        right_paddle.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
        

