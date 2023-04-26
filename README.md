# EnkPi_7.5_Software

### EnkPi is a series of 4 ePaper displays mounted on PCBs to provide sturdiness and comfort to the users.
Powered with **Raspberry Pi Pico W**, these EnkPi boards have Partial Refresh Support with up to 170 degrees Wide Viewing Angle. In this github repo will see setup and getting started guide for EnkPi 2.9" series.

<img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/EnkPi_2_9.jpg " width = "500" height = "300" />
<img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/pinout_2_9.jpg" width = "700" height = "300"/>

## Getting Started with EnkPi
### 1. Step to install boot Firmware
   - Every EnkPi will be provided with boot firmware already installed, so you can directly go to step 2
   - If in any case, you need to install firmware for your board, then you can follow the tutorial [here](https://github.com/sbcshop/PiCoder-Software/blob/main/README.md#1-how-to-install-boot-firmware-in-picoder-kit)

### 2. Testing Pico W on EnkPi
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect EnkPi with a laptop/PC using a micro USB cable and the micro USB port on Pico W present on EnkPi.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on EnkPi. 
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up EnkPi and it should run your script, go to step 3. Once you have transferred your code to the EnkPi board, to see your script running, just plug in power either way using micro USB or Type C, both will work.
    
### 3. How to move your script on Pico W of EnkPi
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr1.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr2.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr3.jpg" />
      <img src="https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/scr4.jpg" />
   
   In similar way you can add various python code files to Pico. Also to try out sample codes given here in [examples folder](https://github.com/sbcshop/EnkPi_2.9_Software/tree/main/examples) you need to save library files from [lib](https://github.com/sbcshop/EnkPi_2.9_Software/tree/main/lib) folder into Pico W of EnkPi.
   
   To do this follow same steps as shown in step 3 but **_to save library file don't change name keep default one:_** [EnkPi_2in9.py](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/lib/EnkPi_2in9.py), [pics.py](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/lib/pics.py)

### Example Codes
   Save whatever example code file you want to try as main.py in pico w as shown in above step 3, also add related lib files with default name.
   - [Example 1](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/display_pattern.py) : This code generates pattern, you can experiment to develop your favourite one
   - [Example 2](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/display_text.py) : Try this code to display text, make sure to install library EnkPi_2in9.py
   - [Example 4](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/display_shapes.py) : Play with some shapes like circle, square, etc.
   - [Example 3](https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/examples/display_images.py) : To display images on EnkPi, this code need library EnkPi_2in9.py & pics.py
   - and [More...](https://github.com/sbcshop/EnkPi_2.9_Software/tree/main/examples)
   
   Now you are ready to try out your own codes, **_Happy Coding!_**

## Documentation
  * [MicroPython getting started for RPI](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   ![EnkPi4_2]() 
   * [EnkPi 4.2"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297434195) - EnkPi with 4.2" E-paper display size
 
   ![EnkPi5_83]()
   * [EnkPi 5.83"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297466963) - EnkPi with 5.83" E-paper display size

   ![EnkPi7_5]()
   * [EnkPi 7.5"](https://shop.sb-components.co.uk/products/enkpi?variant=40474297434195) - EnkPi with 7.5" E-paper display size
 
   ![Universal_E-paper_HAT]()
   * [Universal E-paper HAT]() - EnkPi with 5.83" E-paper display size

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
