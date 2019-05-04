# Pi-TPDD
Raspberry Pi-based TPDD for the TRS-80 Model 100/102/200, WP-2

Version 1 complete

# Hardware
* Raspberry Pi Zero WH (https://www.adafruit.com/product/3708) - $14
* Micro SD card - $10
* Adafruit 128x64 OLED Bonnet for Raspberry Pi (https://www.adafruit.com/product/3531)
* Adafruit Pi Protector for Raspberry Pi Model Zero (https://www.adafruit.com/product/2883) - $5
* Tiny OTG Adapter - USB Micro to USB (https://www.adafruit.com/product/2910) - $2.95
* A USB to Serial Null modem cable (https://www.amazon.com/StarTech-com-USB-Serial-Adapter-Modem/dp/B008634VJY/ref=sr_1_3) - $19.75
* LiFePO4wered/Pi+ (https://www.crowdsupply.com/silicognition/lifepo4wered-pi-plus) - $49-$55 depending on the battery

Standoffs (like these: https://www.adafruit.com/product/3299) should also be used to provide some stability.

I went with the LiFePO4wered/Pi+ because I had one.  Out of the UPSs for the Raspberry PI, this one has a real on/off button and can shut down your PI nicely when you turn it off.

Note that you do really need the Pi Protector - at least the bottom part of it.  If you are using the LiFePO4wered/Pi+, you can short it out should you put the bare Pi on something metal.  That's a really big battery and it could cause some damage - not just to the Pi.  The LiFePO4wered/Pi+ site does have a warning about that.

# Set up
Standard Raspian headless install

You probably want to set up SSH so you can access it over your wireless network.

Follow instructions for installing the OLED Bonnet and LiFePO4wered/Pi+.

You will need to install Mono on your Pi0.

Copy over LaddieAlpha (http://bitchin100.com/wiki/index.php?title=LaddieCon).  I suggest putting it in the bin folder (create if necessary).

Copy over the "menu" folder in this project.  It should go in /home/pi.

Add this line to /etc/rc.local

'''
sudo python3 /home/pi/menu/menu.py &
'''

Put your files in /home/pi/tpdd

# Explanation
The menu.py program is the driver for the whole thing.

It will start LaddieAlpha.  If you need to change anything about running LaddieAlpha, see laddieAlpha.py.  The configurable parts are at the top of the file.

It will display the IP address or your wireless connection (if there is one - "None" otherwise).

It will display the running status of LaddieAlpha.  If LaddieAlpha should stop, move the joystick up and it will restart LaddieAlpha.

When the drive is active (i.e. transferring data), an indicator will display saying so.

Pressing the joystick (as a button) while holding the #5 button down will tell the Pi to shut down.
Pressing the joystick (as a button) while holding the #6 button down will tell the menu.py program to stop (currently commented out because it's there mainly for debugging purposes)
