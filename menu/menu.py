import subprocess
import time
import board
import busio
import laddieAlpha
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import getip

def center_text(text):
	maxwidth, unused = draw.textsize(text, font=font)
	return int((128-maxwidth)/2)

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

top = -2

# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',12)

# Set up buttons and joystick
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

# Start LaddieAlpha
laddieAlpha.start()

shutdown=False
exit_prog=False

while True:
	if not button_A.value:
		if not button_C.value:
			shutdown=True
	#elif not button_B.value:
	#	if not button_C.value:
	#		exit_prog=True

	# Refresh the screen
	draw.rectangle((0, 0, width, height), outline=0, fill=0)

	ip_addresses=getip.getip()
	x=center_text(ip_addresses[0])
	draw.text((x, top+0), ip_addresses[0], font=font, fill=255)

	# Look to see if LaddieAlpha is still running	
	(running,active) = laddieAlpha.poll()
	if running:
		status="Running"
	else:
		# If it's stopped, moving the joystick up will restart it
		status="Stopped"
		if not button_U.value:
			laddieAlpha.start()
	x=center_text(status)
	draw.text((x, top+12), status, font=font, fill=255)

	if active:
		activeDisplay="Drive Active"
	else:
		activeDisplay="            "
	x=center_text(activeDisplay)
	draw.text((x, top+24), activeDisplay, font=font, fill=255)

	# If shutdown was requested, display that indicator
	if shutdown:
		shutdown_text="Shutdown requested"
		x=center_text(shutdown_text)
		draw.text((0,top+36),shutdown_text,font=font,fill=255)

	disp.image(image)
	disp.show()

	if exit_prog:
		laddieAlpha.stop()
		disp.fill(0)
		disp.show()
		break;

	if shutdown:
		subprocess.call(["shutdown","-h","now"])
