"""
Disklarity

Entry Point

Disk Checking tool, designed to be a 'modern' replacement for Gibson Research's ValiDrive.
At the time of writing this, ValiDrive was last updated 689.80 days ago.

Work in progress.

"""

import sys
from lib.helpers import CheckElevation
from lib.gui import StartInterface
from lib.mainfunctions import VerifyDrive, ListDevices, PrintHelp

AMOUNT_OF_CHECKS = 12

if not sys.stdin.isatty() or not sys.stdout.isatty():
    print("[!] Do not open Disklarity directly. Open it in a command line.")
    input()
    sys.exit(1)


def Entrypoint():
    args = sys.argv  # Arguments

    try:
        args[1]
    except IndexError:
        print("Please provide arguments. Run 'help' for more info.")
        sys.exit(1)

    if args[1] == "help":
        PrintHelp()
        sys.exit()

    CheckElevation()  # Checks for elevation and elevates if possible.

    if args[1] == "list":
        ListDevices()
        sys.exit()


    if args[1] == "gui":
        StartInterface()
        sys.exit()

    if args[1] == "verify":
        checks = AMOUNT_OF_CHECKS
        try:
            checks = int(args[3]) if int(args[3]) != 0 else AMOUNT_OF_CHECKS
        except:
            pass

        VerifyDrive(path=args[2], x_many_reads=checks)


if __name__ == "__main__":
    try:
        Entrypoint()
    except Exception as e:
        if type(e) == IndexError:
            print(
                f"[! FATAL !] An error has occurred, specifically, an index error. This is usually caused by broken arguments.\n[! DEBUG !] Error: {e}"
            )
        else:
            print(f"[! FATAL !] An error has occurred.\nDebug: {e}")
