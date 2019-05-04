import subprocess
import os
from select import select

# Com port to use
com_port="/dev/ttyUSB0"

# Where the LaddieAlpha executable is located
laddie_alpha="/home/pi/bin/LaddieAlpha.EXE"

# The directory where the files are stored
tpdd_dir="/home/pi/tpdd"

# The process to start - 6 for 100/102, 8 for WP-2
laddieAlpha=["mono",laddie_alpha,com_port,"6"]

def start():
	""" Start the Laddie Alpha process """
	global laddieAlphaProc
	os.chdir(tpdd_dir)
	laddieAlphaProc = subprocess.Popen(laddieAlpha,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

def stop():
	""" Stop the Laddie Alpha process """
	global laddieAlphaProc
	laddieAlphaProc.terminate()
	
def poll():
	""" Poll the Laddie Alpha process
	returns (running:boolean, active:boolean) """
	global laddieAlphaProc

	active=False

	# Look to see if LaddieAlpha is still running	
	if laddieAlphaProc.poll() == None:
		running=True
	else:
		running=False

	if running:
		# Look to see if LaddieAlpha wrote out any data.
		# If it did, the "drive" is active.
		active=False
		poll_result = select([laddieAlphaProc.stdout],[],[],0.1)[0]
		while poll_result:
			if laddieAlphaProc.poll() == None:
				outs=laddieAlphaProc.stdout.readline()
				if len(outs) > 0:
					active=True
				poll_result = select([laddieAlphaProc.stdout],[],[],0.1)[0]
			else:
				break

	return (running,active)
