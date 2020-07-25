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

