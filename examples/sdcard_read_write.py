# Example of data read/write to sd card

import time
from EnkPi_7in5 import SDCard
import os

data = "SB COMPONENTS"

sd=SDCard()
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc")) # check the files in sd card

fn = "/fc/File.txt"
print("Single block read/write")

#################################################

with open(fn, "a") as f:  # append data to file
    n = f.write(data+'\n')
    print(n, "bytes written")
#os.umount("/fc")
time.sleep(0.2)
#################################################

#################################################
with open(fn, "r") as f:  # read data from file
    result = f.read()
    print(result)
    print(len(result), "bytes read")
os.umount("/fc")
#################################################    


