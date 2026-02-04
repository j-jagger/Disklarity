"""
Disklarity

Entry Point

Disk Checking tool, designed to be a 'modern' replacement for Gibson Research's ValiDrive.
At the time of writing this, ValiDrive was last updated 689.80 days ago.

"""
import sys
from wmi import WMI
from lib.helpers import *
from lib.gui import StartInterface
from lib.mainfunctions import VerifyDrive, ListDevices,PrintHelp
import ctypes

AMOUNT_OF_CHECKS = 10



def CheckElevation(argv): # Experimental; Finnicky in practice.
    try:
        s32 = ctypes.windll.shell32 # WinShell32 Object
        if not s32.IsUserAnAdmin():
            print("[!] Disklarity requires Administrative Privileges to open Win32 devices as file-like objects.")
            print("[!] Attempting UAC Elevation...")
        else:
            return

        argument_line = " ".join(str(arg) for arg in argv) # Reconstruct arguments as string
        executable = str(sys.executable) # Reconstruct executable location
        ret = s32.ShellExecuteW(None, "runas", executable, argument_line, None, 1) # Re-execute as administrator.
        if ret <= 32:
            raise RuntimeError(f"[!] UAC Elevation Failed! RET: {ret}")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Elevation failed! {e}")


def Entrypoint():
    args = sys.argv # Arguments


    try:
        args[1]
    except IndexError:
        print("Please provide arguments. Run 'help' for more info.")
        sys.exit(1)
    
    CheckElevation(args) # Checks for elevation and elevates if possible.

    if args[1] == "list":
        ListDevices()
        sys.exit()

    if args[1] == "help":
        PrintHelp()
        sys.exit()

    if args[1] == "gui":
        StartInterface()
        sys.exit()

    else:
        VerifyDrive(args[1],int(args[2]) or AMOUNT_OF_CHECKS)



if __name__ == "__main__":
    Entrypoint()