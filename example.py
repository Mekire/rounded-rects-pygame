import os
import sys
import pygame as pg

from roundrects import round_rect


class Control(object):
    def __init__(self,screen_size):
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        self.screen = pg.display.set_mode(screen_size)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.background = pg.image.load("diag_background.png").convert()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.background, (0,0))
        round_rect(self.screen, (50,20,400,200), (130,100,255,175),
                        30, 50, pg.Color("lightslateblue"))
        round_rect(self.screen, (20,235,100,200), pg.Color("red"), 10, 25)
        round_rect(self.screen, (140,250,175,100), pg.Color("black"), 30,
                        1, pg.Color("green"))
        round_rect(self.screen, (335,250,145,200), pg.Color("purple"), 30,
                        20, (255,255,0,150))

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    app = Control((500,500))
    app.main_loop()
    pg.quit()
    sys.exit()
