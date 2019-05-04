import subprocess
	
def getip():
	# Set up the interfaces we are looking for
	interfaces= {"wlan0:":"none"}
	
	# Get the network interfaces
	#ifconfig=subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read()
	ifconfig=subprocess.check_output("ifconfig",shell=True).decode("utf-8")

	# Go through the lines
	for line in ifconfig.split('\n'):
		# Split up the lines by space
		parts=line.split(' ')
	
		# The interface names are in pos 0
		if parts[0] != '':
			interface=parts[0]
	
		# We only care about lines that have at least 10 parts
		if len(parts)>10:
			# If we find the internet address line
			if parts[8] == "inet":
				# And it's in an interface we care about
				if interface in interfaces:
					# Update the interfaces list
					interfaces[interface]=parts[9]
	
	display=[]
	for name,value in interfaces.items():
		display.append(value)
	
	return display

if __name__ == "__main__":
	print(getip())
