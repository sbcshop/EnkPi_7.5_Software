# Example of display shapes Like rectangle, circle
import EnkPi_7in5 as epd
import time
import math

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)

e_paper.imageblack.vline(10, 90, 60, 0x00)
e_paper.imageblack.vline(120, 90, 60, 0x00)
e_paper.imagered.hline(10, 90, 110, 0xff)
e_paper.imagered.hline(10, 150, 110, 0xff)
e_paper.imagered.line(10, 90, 120, 150, 0xff)
e_paper.imagered.line(120, 90, 10, 150, 0xff)
e_paper.delay(50)
    
e_paper.imageblack.rect(10, 180, 50, 80, 0x00 )
e_paper.imageblack.fill_rect(70, 180, 50, 80,0x00 )
e_paper.imagered.rect(10, 300, 50, 80, 0xff )
e_paper.imagered.fill_rect(70, 300, 50, 80,0xff )

def ring(x,y,r,c):
    e_paper.imagered.pixel(x-r,y,c)
    e_paper.imagered.pixel(x+r,y,c)
    e_paper.imagered.pixel(x,y-r,c)
    e_paper.imagered.pixel(x,y+r,c)
    for i in range(1,r):
        a = int(math.sqrt(r*r-i*i))
        e_paper.imagered.pixel(x-a,y-i,c)
        e_paper.imagered.pixel(x+a,y-i,c)
        e_paper.imagered.pixel(x-a,y+i,c)
        e_paper.imagered.pixel(x+a,y+i,c)
        e_paper.imagered.pixel(x-i,y-a,c)
        e_paper.imagered.pixel(x+i,y-a,c)
        e_paper.imagered.pixel(x-i,y+a,c)
        e_paper.imagered.pixel(x+i,y+a,c)
        
def circle(x,y,r,c):
    e_paper.imagered.hline(x-r,y,r*2,c)
    for i in range(1,r):
        a = int(math.sqrt(r*r-i*i)) # Pythagoras!
        e_paper.imagered.hline(x-a,y+i,a*2,c) # Lower half
        e_paper.imagered.hline(x-a,y-i,a*2,c) # Upper half
        
circle(500,200,60,0xff)#x,y,radius,color
ring(300,200,60,0xff)

e_paper.display()
#e_paper.clear_screen()
e_paper.delay(1000)
e_paper.sleep()

