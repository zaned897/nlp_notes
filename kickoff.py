from os import MFD_HUGE_SHIFT
from wasabi import Printer
msg = Printer()

def check_requirements():
	"""Check the requirements"""
	import subprocess
	import sys
	import os
	if os.path.isfile("src/requirements.txt"):
		if os.stat("src/requirements.txt").st_size == 0:
			print("No requirements.txt found")
			print("Please add requirements to requirements.txt")
			sys.exit()
		else:
			with open("src/requirements.txt") as file:
				for line in file:
					if not line.strip() or line.startswith('#'):
						continue
					try:
						subprocess.check_call([sys.executable, "-m", "pip", "install", line.strip()])
						msg.good(f"{line.strip()} installed successfully")
					except subprocess.CalledProcessError:
						print("Error: Could not install " + line.strip())
						sys.exit()
	return True

if __name__ == "__main__":
	msg.divider("Checking requirements")
	check_requirements()