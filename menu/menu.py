import subprocess
import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import backup
import getip
import battery
import laddieAlpha

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
backup_process=None

def display_status(ip_address,status,active,special,battery):
	# Refresh the screen
	draw.rectangle((0, 0, width, height), outline=0, fill=0)

	x=center_text(ip_address)
	draw.text((x, top+0), ip_address, font=font, fill=255)

	x=center_text(status)
	draw.text((x, top+12), status, font=font, fill=255)

	x=center_text(active)
	draw.text((x, top+24), active, font=font, fill=255)

	x=center_text(special)
	draw.text((x, top+36), special, font=font, fill=255)

	x=center_text(battery)
	draw.text((x, top+48), battery, font=font, fill=255)

	disp.image(image)
	disp.show()


while True:
	special="            "
	if not button_A.value:
		if not button_C.value:
			shutdown=True
			special="Shutdown requested"
	elif not button_B.value:
		if not button_C.value:
			exit_prog=True
		elif not button_D.value:
			backup_process=backup.start(backup.backup_process)
			special="Backup running"
		elif not button_U.value:
			backup_process=backup.start(backup.restore_process)
			special="Restore running"

	ip_address=getip.getip()[0]

	# Look to see if LaddieAlpha is still running	
	(running,active) = laddieAlpha.poll()
	if running:
		status="Running"
	else:
		# If it's stopped, moving the joystick up will restart it
		status="Stopped"
		if not button_U.value:
			laddieAlpha.start()

	if active:
		active_display="Drive Active"
	else:
		active_display="            "

	# Get the battery level
	battery_level=battery.get_battery_level()
	battery_display="Bat: {battery_level} mV left".format(battery_level=battery_level)

	if backup_process != None:
		if backup_process.poll() == False:
			backup_process=None
			special=""

	display_status(ip_address,status,active_display,special,battery_display)

	if exit_prog:
		laddieAlpha.stop()
		disp.fill(0)
		disp.show()
		break;

	# Note that we wait until here before starting the shutdown
	# to give the Pi time to display that status.
	if shutdown:
		subprocess.call(["shutdown","-h","now"])

