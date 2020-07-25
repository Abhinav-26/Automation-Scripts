import os
import time

TargetIP = input("Enter the IP of Target Machine :")

print("Enter the number to perform the tasks :\n")
print("""
	Press 1  for Basic Scanning
	Press 2  for Scanning Specific Port No
	Press 3  for Scanning IP Ranges
	Press 4  for Scanning top-popular ports
	Press 5  for Scanning with disbaling DNS resolution
	Press 6  for Scanning to detect services used
	Press 7  for Scanning only TCP protocols
	Press 8  for Scanning only UDP protocols
	Press 9  for Scanning CVE detection
	Press 10 for Scanning Aggresive Scanning\n""")

usrInput = int(input("Enter the Number To Perform the Scans :"))

print("[INFO] performing the scan...")
time.sleep(2.0)

if (usrInput == 1):
	os.system("nmap {}".format(TargetIP))
	exit(0)

elif (usrInput == 2):
	port=input("Enter the IP Port to Scan :")
	os.system("nmap -p {} {}".format(port,TargetIP))
	exit(0)

elif (usrInput == 3):
	#range=input("Enter the IP ranges to Scan :")
	iprange = input("Enter the Complete IP Range :")
	os.system("nmap -p {}".format(iprange))
	exit(0)

elif (usrInput == 4):
	num=int(input("Enter the count of ports you want to Scan :"))
	os.system("nmap --top-ports {} {}".format(num,TargetIP))
	exit(0)

elif (usrInput == 5):
	os.system("nmap -p 80 -n {}".format(TargetIP))
	exit(0)

elif (usrInput == 6):
	os.system("nmap -sV {}".format(TargetIP))
	exit(0)

elif (usrInput == 7):
	os.system("nmap -sT {}".format(TargetIP))
	exit(0)

elif (usrInput == 8):
	os.system("nmap -sU {}".format(TargetIP))
	exit(0)

elif (usrInput == 9):
	os.system("nmap -Pn --script vuln {}".format(TargetIP))
	exit(0)

elif (usrInput == 10):
	os.system("nmap -sV -O -A -Pn {}".format(TargetIP))
	exit(0)

else:
	print("[INFO] exiting...")
	time.sleep(2.0)
	print("Please Enter Correct Number!!!")
