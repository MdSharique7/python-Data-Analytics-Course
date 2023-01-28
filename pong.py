import pgzrun

WIDTH = 800
HEIGHT = 500

box_red = Rect((10,10),(20,100))
box_blue = Rect((WIDTH-30,10),(20,100))
ball = Rect((WIDTH/2,HEIGHT/2),(20,20))
brs = 5
bbs = 6
bs = (10,10)


def draw():
    screen.fill('white')
    screen.draw.filled_rect(box_red,'red')
    screen.draw.filled_rect(box_blue,'blue')
    screen.draw.filled_rect(ball,'black')

def update():
    global brs , bbs , bs
    brs = move_vertically(box_red,brs)
    bbs = move_vertically(box_blue,bbs) 
    bs = move_ball(ball,bs)
    # print(box_blue.bottom,box_blue.top,bbs)

def move_vertically(box,speed):
        box.y +=speed
        if box.bottom >= HEIGHT or box.top <= 0:
            speed = -speed
        return speed   
def move_ball(b,s):
    b.x += s[0]
    b.y += s[1]
    if b.bottom >= HEIGHT or b.top <= 0:
        s =s[0],-s[1]
    if b.left<=0 or b.right >= WIDTH:
        s = -s[0],s[1]  
    #  collision
    if b.colliderect(box_red) or b.colliderect(box_blue):
        s = -s[0],s[1]  
    return s


pgzrun.go()
