# Example of display text
from EnkPi_7in5 import RTC
import time

rtc = RTC()
while 1:
    print(rtc.read_time())
    rtc.set_time('12:24:00,Thursday,2023-03-20') # set time, after setting time uncomment this line 
    print(rtc.temperature())
    time.sleep(1)
