import pygame as pg

class Window:
    def __init__(self):
        (numpass,numfail) = pg.init()
        print(f'Number of modules initialized successfully: {numpass}')
        print(f'Number of modules initialized failure: {numfail}')
        
        pg.display.set_caption('SolarSystem')
        pg.display.set_icon(pg.image.load('assets/earth.webp'))
        
        
    def create_window(self, width, height, color: tuple):
        running  = True

        screen = pg.display.set_mode((width, height), pg.RESIZABLE)
        
        x, y = screen.get_size()
        print(f'Window size: {x, y}')
                
        while running:  
            for event in pg.event.get():  
                if event.type == pg.QUIT:  
                    running = False
                    
            screen.fill(color)
            
            pg.draw.circle(screen, (0, 0, 0), (300, 200), 75)
            
            pg.display.flip()
            
        pg.quit()


