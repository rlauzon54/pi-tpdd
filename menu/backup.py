import subprocess
import os
from select import select

backup_process=0
restore_process=1
no_process=2

# Backup and restore scripts
BACKUP=["/bin/bash","/home/pi/bin/backup"]
RESTORE=["/bin/bash","/home/pi/bin/restore"]

def start(process_type):
	""" Start the process """
	global backup_restore_proc
	if process_type==backup_process:
		process_to_start = BACKUP
	else:
		process_to_start = RESTORE
	backup_restore_proc = subprocess.Popen(process_to_start,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

def poll():
	""" Poll the backup/restore process """
	global backup_restore_proc

	# Look to see if the process is still running	
	if backup_restore_proc.poll() == None:
		running=True
	else:
		running=False

	return running
