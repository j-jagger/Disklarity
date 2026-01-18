"""
Disklarity

Disk Checking tool, designed to be a 'modern' replacement for Gibson Research's ValiDrive.
At the time of writing this, ValiDrive was last updated 689.80 days ago.
"""
import sys
from wmi import WMI
from lib.helpers import *
from lib.gui import StartInterface
from lib.mainfunctions import VerifyDrive, ListDevices,PrintHelp


def Entrypoint():
    args = sys.argv

    try:
        args[1]
    except IndexError:
        print("Please provide arguments. Run 'help' for more info.")
        exit(1)
    
    if args[1] == "list":
        ListDevices()
        exit()

    if args[1] == "help":
        PrintHelp()
        exit()

    if args[1] == "gui":
        StartInterface()
        exit()

    else:
        VerifyDrive(args[1],10)


if __name__ == "__main__":
    Entrypoint()