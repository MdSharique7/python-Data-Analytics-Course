import pgzrun

WIDTH = 640
# A box with 50,50 as x,y coordinates, (100,100) as width and height
box = Rect((50,50),(100,100))
box2 = Rect((150,150),(100,100))
def draw():
    screen.fill('white') # white background
    screen.draw.filled_rect(box,'red') # Red box
    screen.draw.filled_rect(box2,'blue') # blue box

def update():
    if box.x > WIDTH:
        box.x = 0
        # moves box 3 pixels to the right every frame
    box.x += 3    

pgzrun.go()    