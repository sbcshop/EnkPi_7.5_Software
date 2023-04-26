# Example of display text
import EnkPi_7in5 as epd
import time

e_paper = epd.E_paper()
e_paper.imageblack.fill(0xff)
e_paper.imagered.fill(0x00)
    
e_paper.imageblack.text("SB COMPONENTS", 5, 10, 0x00)
e_paper.imagered.text("EnkPi 7.5 inch", 5, 40, 0xff)
e_paper.display()

#e_paper.clear_screen()
e_paper.delay(1000)
print("sleep")
e_paper.sleep()

