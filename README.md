# Pi-TPDD
Raspberry Pi-based TPDD for the TRS-80 Model 100/102 (and probably the 200)

Currently in design.

# Hardware
* Raspberry Pi Zero WH (https://www.adafruit.com/product/3708) - $14
* Micro SD card - $10
* Micro SD Card Extender (If you want to move the USB slot) (https://www.adafruit.com/product/3688) - $6.95

* PowerBoost 1000 Charger - Rechargeable 5V Lipo USB Boost @ 1A - 1000C (https://www.adafruit.com/product/2465) - $19.95
* Lithium Ion Battery Pack - 3.7V 6600mAh (https://www.adafruit.com/product/353) - $29.50
* 5V 2.4A Switching Power Supply with 20AWG MicroUSB Cable  (https://www.adafruit.com/product/1995) - $7.50

* Tiny OTG Adapter - USB Micro to USB (https://www.adafruit.com/product/2910) - $2.95
* A USB to Serial Null modem cable (https://www.amazon.com/StarTech-com-USB-Serial-Adapter-Modem/dp/B008634VJY/ref=sr_1_3) - $19.75

* Momentary switch (normally open) - Cheap from many places
* Drive activity light - any red LED works

# Set up
Standard Raspian install

Install the power button (https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi) and software needed to shutdown the Pi when the button is pressed.

# Explanation
The Raspberry PI is the basis for the installation.

The PowerBoost 1000 Charger both provides power to the Pi and recharges the Lithium Ion Battery Pack.  The 5V 2.4A Switching Power Supply is used for charging.

The Tiny OTG Adapter is used to connect the USB to Serial Null modem cable to the Pi.  The Serial cable is, of course, needed to connect to the Model 100/102.

Since this is a headless installation, we need a way to nicely shutdown the Pi when we don't need it anymore.  And wake it up when we do need it.  So a momentary switch and some software is needed.

A drive activity light is also useful so that we have an indication that everything is actually working.
