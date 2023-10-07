from urllib.request import urlretrieve
import nmap, os, subprocess, getpass
import sys

#gets the file path for python install
path = (sys.executable).strip("python.exe")

#lets the user know its being installed
print("installing required libraries...")

#changed the directory for the execution of the os.system()
os.chdir(path)

#executes the code to install the needed libraries
os.system("python -m pip install scapy")
os.system("python -m pip install python-nmap")