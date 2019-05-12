import subprocess

def get_battery_level():
	battery_level_high=3500
	output = subprocess.check_output(['lifepo4wered-cli','get'], universal_newlines=True)
	lines = output.split("\n")
	for line in lines:
		parts=line.split(" ")
		if parts[0]=="VBAT":
			battery_level=int(parts[2])
		if parts[0]=="VBAT_SHDN":
			battery_level_low=int(parts[2])

	return battery_level-battery_level_low

#print(get_battery_level())
