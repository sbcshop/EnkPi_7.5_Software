# Example of button
from EnkPi_7in5 import Buzzer
from machine import Pin
import time

mi5=659 #frequency

button1 = Pin(2, Pin.IN, Pin.PULL_UP)
button2 = Pin(3, Pin.IN, Pin.PULL_UP)
button3 = Pin(4, Pin.IN, Pin.PULL_UP)
button4 = Pin(5, Pin.IN, Pin.PULL_UP)
button5 = Pin(14, Pin.IN, Pin.PULL_UP)
button6 = Pin(15, Pin.IN, Pin.PULL_UP)

while 1:
    if button1.value() == 0:
        print("button 1")
        Buzzer.tone(mi5,0.5,0.1)
               
    elif button2.value() == 0:
        print("button 2")
        Buzzer.tone(mi5,0.5,0.1)
        
    elif button3.value() == 0:
        print("button 3")
        Buzzer.tone(mi5,0.5,0.1)
        
    elif button4.value() == 0:
        print("button 4")
        Buzzer.tone(mi5,0.5,0.1)
         
    elif button5.value() == 0:
        print("button 5")
        Buzzer.tone(mi5,0.5,0.1)
        
    elif button6.value() == 0:
        print("button 6")
        Buzzer.tone(mi5,0.5,0.1)


