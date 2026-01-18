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
