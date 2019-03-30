from turtle import *

speed(0)
shape("turtle")
color("red")
left (30)
def hinhthoi():
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
for i in range (4): 
    hinhthoi()
    right (30)
mainloop()