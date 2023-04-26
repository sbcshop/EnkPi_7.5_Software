# Example of display pattern

import EnkPi_7in5 as epd
import time

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)

for k in range(0, 4):
    for j in range(0, 4):
        for i in range(0, 5):
            e_paper.imageblack.fill_rect(0+100+j*200, i*20+k*200, 100, 20, 0x00)
        for i in range(0, 5):
            e_paper.imagered.fill_rect(0+0+j*200, i*20+100+k*200, 100, 20, 0xff)
            
e_paper.display()
e_paper.delay(50)

#epd.clear_screen()
e_paper.delay(100)
print("sleep")
e_paper.sleep()

