from wmi import WMI
import hashlib
from lib.helpers import *

c = WMI()



def VerifyDrive(path,x_many_reads):

    try:
        for i in c.Win32_DiskDrive(): # Irritating to use WMI object
            dev = wmi_to_dict(i) # Very nice to use dict object
            if dev.get("DeviceID") == path:
                wmidevice = dev # Ensuring passed device actually exists.
        if not wmidevice:
            raise FileNotFoundError() 
    except Exception as e:
        print(f"[!] Failed to load {path} via WMI: {e}")
        exit()

    print(f"[✔] Located device {wmidevice.get("Caption")} [Path @ {path}]")

    chunksize = wmidevice.get("DefaultBlockSize") or wmidevice.get("BytesPerSector") # Might remove BytesPerSector.
    try:
        filesystemsize = int(wmidevice.get("Size")) # get FS size so we can divide it in a moment.
    except TypeError as e:
        print(f"[!] Fatal error getting FileSystem size. If {path} is an adapter (SD MMC, Etc), ensure the storage device is inserted.")
        print(f"[?] Debug: {e}")
        exit(1)

    step = filesystemsize // x_many_reads # how many steps in bytes should we do



    print(
        f"[?] Device tells us it's ~{int(filesystemsize)/1e9:.2f}GB."
    )

    print(
        f"[✔] Step set to {step}. Ready for liftoff. Hit enter to continue."
    )

    input() # Will stop yielding when user hits enter in stdin.

    with open(path, "rb") as device: # Opens device as a file-like object. This would be so much easier in UNIX/BSD.
        for chunk in range(x_many_reads): # For every chunk in the amount of reads we should do
            offset = step * chunk 

            device.seek(offset) # Change Pointer location
            print(f"Trying read... [Offset: {offset}]") 
            try:
                data = device.read(chunksize) # Attempt read
                if not data:
                    print(f"!!! EMPTY READ @ {offset} !!!")
                elif data == bytes(chunksize): # Might modify this, it's a bit inefficient I believe as it allocates an entire bytes object. If chunksize is like 1gb (not sure why anyone would set that in the first place) this would be a major issue.
                    print(f"!!! READ EMPTY BYTES @ {offset} !!!")
                else:
                    # TODO: Add SHA logs and a filesystem verification system.
                    print(f"[✔] Chunk @ {offset} normal. SHA256 Trunc. 16: {hashlib.sha256(data).hexdigest()[:16]}")
            except:
                print(f"!!! READ FAILED @ {offset} !!!")

def ListDevices():
    print("[?] Listing Devices...")

    try:
        for i in c.Win32_DiskDrive(): # Another annoying WMI device
            dev = wmi_to_dict(i) # Another beautiful, charming dict-man.

            print(f"[✔] Found: '{dev.get('Model')}' @ {dev.get('DeviceID')}'") # Verbosity!
    except Exception as e:
        print(f"[!] Failed to list devices: {e}")

def PrintHelp():
    # I would use one multiline print statement for this, but it looks weird.
    print("\n" * 3)
    print("Disklarity [https://github.com/j-jagger/Disklarity/]")
    print("Disk Capacity Verification Utility")
    print("+-----------------------+----------------------------------+")
    print("| Command & Name        | Description                      |")
    print("+-----------------------+----------------------------------+")
    print("| disklarity.py list    | Lists all Win32_DiskDrives.      |")
    print("| disklarity.py \.\dev0 | Runs Disklarity on that drive.   |")
    #print("| disklarity.py gui     | Opens the User Interface.        |") not yet implemented
    print("+-----------------------+----------------------------------+")
    print("\n" * 3)

