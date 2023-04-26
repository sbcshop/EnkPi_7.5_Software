from machine import Pin
from time import sleep

Led = Pin("LED", Pin.OUT) # "LED" to select onboard led for Pico W 

while True:
    Led.on()  #To switch on LED
    sleep(2)  # wait 2 second
    print("LED is ON")
    
    Led.off() #To switch off LED
    sleep(2)  #wait 2 second
    print("LED is OFF")
    
    
