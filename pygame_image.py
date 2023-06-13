import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = [bg_img, pg.transform.flip(bg_img, True, False)]*2
    bird3_img = pg.image.load("ex01/fig/3.png")
    bird3_img = pg.transform.flip(bird3_img, True, False)
    bird3_imgs = [bird3_img, pg.transform.rotozoom(bird3_img, 10, 1.0)]
    num = [j for j in range(100)]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        i = tmr%1600
        for x in range(4):
            screen.blit(bg_img2[x], [1600*x-i,0])
        if num[tmr%100]%100 > 50:   
            screen.blit(bird3_imgs[0], [300, 200])
        else:
            screen.blit(bird3_imgs[1], [300,200]) 
        
       
        pg.display.update()
        tmr += 1        
        clock.tick(100)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()