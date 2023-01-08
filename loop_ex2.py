from turtle import *

speed('slowest')
side = 10
for i in range(side):
    forward(100)
    for i in range(4):
        forward(50)
        left(90)
        write(i)
    left(360//side)
    mainloop()    
