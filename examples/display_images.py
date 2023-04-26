# Example of Display images

import EnkPi_7in5 as epd
import time
import pics # save pics.py file in EnkPi

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)
    
e_paper.imagered.blit(pics.sb_logo , 100,50) # print sb components logo

e_paper.display()

#e_paper.clear_screen()
e_paper.delay(1000)
e_paper.sleep()

