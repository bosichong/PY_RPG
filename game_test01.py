# codeing=utf-8

from PygameApp import *

# 一些常量

# 场景的宽高
WINDOWNWIDTH = 640
WINDOWNHEIGHT = 480
BOXSIZE = 40  # 方块的宽和高的尺寸
GAPSIZE = 10  # 方块之间的间隙
BOARDWIDTH = 10  # 游戏板 width 个数
BOARDHEIGHT = 7  # 游戏板 height 个数
# 游戏板的边距.
XARGIN = int((WINDOWNWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YARGIN = int((WINDOWNHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)


class TestMain(Scene):
    def __init__(self, display):
        super().__init__(display)
        self.id = 'Test'
        self.start = True
        self.tmpmps = list()  # 方块list
        for i in range(BOARDWIDTH):
            for j in range(BOARDHEIGHT):
                temprect = (XARGIN + i * (BOXSIZE + GAPSIZE), YARGIN + j * (BOXSIZE + GAPSIZE), 0, 0)
                tempcolor = WHITE
                self.tmpmps.append(MySprite(self.display, self.resolution, tempcolor, temprect))
        self.last_update = pygame.time.get_ticks()  # 计时
        self.k = 0  # 计数

        self.myimg = Myimg(self.display)

    def draw(self):
        self.display.fill(BLACK)
        for m in self.tmpmps[:self.k]:
            m.draw()
        self.myimg.draw()

    def update(self):

        # 间隔一定时间绘制一个方块
        now = pygame.time.get_ticks()
        if now - self.last_update > 2:
            if self.k < len(self.tmpmps):
                self.k += 1
                self.last_update = pygame.time.get_ticks()

        # 更新每一个小方块的动画
        for mp in self.tmpmps[:self.k]:
            mp.update()

        # self.myimg.update()


class MySprite(pygame.sprite.Sprite):
    def __init__(self, display, resolution, color, rect):
        pygame.sprite.Sprite.__init__(self)
        self.display = display  # 渲染器display
        self.resolution = resolution  # 游戏尺寸
        self.color = color  #
        self.rect = pygame.Rect(rect)  # 创建一个矩形
        self.last_update = pygame.time.get_ticks()  # 游戏开始时的计时

    def draw(self):

        pygame.draw.rect(self.display, self.color, self.rect)  # 绘制方块

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            if self.rect.width < BOXSIZE:
                self.rect.width += 10
                self.rect.height += 10
                self.last_update = pygame.time.get_ticks()


class Myimg(pygame.sprite.Sprite):
    def __init__(self, display):
        pygame.sprite.Sprite.__init__(self)
        self.display = display
        self.image = pygame.image.load('./images/bosi.png')  # 导入图片
        self.rect = self.image.get_rect()  # 返回一个rect对象
        self.rect.topleft = (random.randint(40, 590), random.randint(40, 430))  # 设置他的坐标
        self.last_update = pygame.time.get_ticks()  # 获取当前游戏动行的时间，这是一个整数，不明白可以打印看看
        # 移动速度
        self.speed_x = random.randint(1, 10)
        self.speed_y = random.randint(1, 10)
        self.image.set_alpha(100)  # 半透明

    def draw(self):
        self.display.blit(self.image, self.rect)

    def update(self):
        '''更新自己的坐标，如果放在精灵组中，调用组的update()函数，会自动调用本函数'''
        now = pygame.time.get_ticks()
        if now - self.last_update > 1:  # 通过这个时间差来做一些动画
            # self.rect.topleft = (random.randint(0,600),random.randint(0,440))#随机变化位置
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.last_update = now


def main():
    app = GameApp()
    appdisplay = app.display
    app.scenes.append(TestMain(appdisplay))
    app.run()


if __name__ == '__main__':

    main()
