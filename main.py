"""
Disklarity

Disk Checking tool, designed to be a 'modern' replacement for Gibson Research's ValiDrive.
At the time of writing this, ValiDrive was last updated 689.80 days ago.
"""
import sys
from wmi import WMI
from lib.helpers import *
from lib.gui import StartInterface
from lib.mainfunctions import VerifyDrive


c = WMI()

CHUNK_INDEX = 10




def ListDevices():
    print("Listing Devices...")

    for i in c.Win32_DiskDrive():
        dev = wmi_to_dict(i)

        print(f"Found: '{dev.get('Model')}' @ {dev.get('DeviceID')}'")


if __name__ == "__main__":
    args = sys.argv

    if args[1] == "list":
        print("Listing.")
        ListDevices()
        exit()

    if args[1] == "gui":
        print("Opening UI...")
        StartInterface()
        exit()
    else:
        VerifyDrive(args[1],10)
