import ctypes
import sys

def wmi_to_dict(obj):
    props = {}
    for prop in obj.properties:
        props[prop] = getattr(obj, prop, None)
    return props

def CheckElevation():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("[!] Please run Disklarity as Administrator.")
        sys.exit(1)
