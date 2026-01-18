from wmi import WMI
import hashlib
from lib.helpers import *

c = WMI()



def VerifyDrive(path,x_many_reads):

    try:
        for i in c.Win32_DiskDrive():
            dev = wmi_to_dict(i)
            if dev.get("DeviceID") == path:
                wmidevice = dev
        if not wmidevice:
            raise FileNotFoundError()
    except Exception as e:
        print(f"[!] Failed to load {path} via WMI: {e}")
        exit()

    print(f"[✔] Located device {wmidevice.get("Caption")} [Path @ {path}]")

    chunksize = wmidevice.get("DefaultBlockSize") or wmidevice.get("BytesPerSector")
    filesystemsize = int(wmidevice.get("Size"))

    step = filesystemsize // x_many_reads



    print(
        f"[?] Device tells us it's ~{int(filesystemsize)/1e9:.2f}GB. We'll be the judge of that."
    )

    print(
        f"[✔] Step set to {step}. Ready for liftoff, houston. Hit enter to continue."
    )

    input()

    with open(path, "rb") as device:
        for chunk in range(x_many_reads):
            offset = step * chunk

            device.seek(offset)
            print(f"Trying read... [Offset: {offset}]")
            try:
                data = device.read(chunksize)
                if not data:
                    print(f"!!! EMPTY READ @ {offset} !!!")
                elif data == bytes(chunksize):
                    print(f"!!! READ EMPTY BYTES @ {offset} !!!")
                else:
                    print(f"[✔] Chunk @ {offset} normal. SHA256[16]: {hashlib.sha256(data).hexdigest()[:16]}")
            except:
                print(f"!!! READ FAILED @ {offset} !!!")

def ListDevices():
    print("Listing Devices...")

    for i in c.Win32_DiskDrive():
        dev = wmi_to_dict(i)

        print(f"Found: '{dev.get('Model')}' @ {dev.get('DeviceID')}'")

def PrintHelp():
    # I would use one multiline print statement for this, but it looks weird.
    print("\n" * 3)
    print("Disklarity [https://github.com/j-jagger/Disklarity/]")
    print("Disk Capacity Verification Utility")
    print("+-----------------------+----------------------------------+")
    print("| Command & Name        | Description                      |")
    print("+-----------------------+----------------------------------+")
    print("| disklarity.py list    | Lists all Win32_DiskDrives.      |")
    print("| disklarity.py \\.\dev0 | Runs Disklarity on that drive.   |")
    #print("| disklarity.py gui     | Opens the User Interface.        |") not yet implemented
    print("+-----------------------+----------------------------------+")
    print("\n" * 3)

