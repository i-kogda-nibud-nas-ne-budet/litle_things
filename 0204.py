import pygame
pygame.init()
back = (200, 200, 0) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)
clock = pygame.time.Clock()
#переменные, отвечающие за координаты платформы
racket_x = 200
racket_y = 330
#флаг окончания игры
game_over = False
#класс из предыдущего проекта
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
#класс для объектов-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
#создание мяча и платформы   
ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)
xx=10
yy=10
monsters=[]
for i in range(3):
    for j in range(8):
        monster = Picture('enemy.png',xx,yy,10,10)
        monsters.append(monster)
        xx+=60
    xx=10
    yy+=60
move_left=False
move_right=False
while not game_over:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            move_right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            move_right = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            move_left = True
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            move_left = False
    if move_right:
        platform.rect.x+=3
    if move_left:
        platform.rect.x-=3
    for m in monsters:
        m.draw()
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
