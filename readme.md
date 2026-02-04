# ![Disklarity](/branding/disklarity-lg.png)
## By Joe Jagger


Disk Capacity Verification Utility

[![Releases](https://img.shields.io/badge/Disklarity-View_Binaries-blue?style=for-the-badge)](https://github.com/j-jagger/Disklarity/releases)
![Build Status](https://img.shields.io/github/actions/workflow/status/j-jagger/Disklarity/buildrelease.yml?style=for-the-badge)


## Opening Notes:
Disklarity, as afforely-mentioned, is a Disk Capacity Verification Utility. It divides the filesystem of a disk into segments based on the advertised size, then reads them.

It was created as I purchased a large amount of MicroSD cards over Christmas, of which I could do to test considering they're not exactly main-branded. I **could** use [Gibson Research's ValiDrive](https://www.grc.com/validrive.htm), which would've been my normal go-to, but I decided to write this instead as a personal challenge.

## Usage:

Using Disklarity is quite simple.

To begin with, run Python as an Administrator.

Then, run:

```bash
disklarity list
```

this should output similar to the following:

```
Listing.
Listing Devices...
Found: 'KINGSTON SV300S37A240G' @ \\.\PHYSICALDRIVE0' # Boot Disk
Found: 'KINGSTON SNV2S2000G' @ \\.\PHYSICALDRIVE1' # This is my SSD.
Found: 'Generic- SD/MMC USB Device' @ \\.\PHYSICALDRIVE2' # This is a MicroSD card reader I used for testing.
```

Note that ``\\.\PHYSICALDRIVE0`` is your Windows drive. No matter your UAC level, Windows will NOT let you verify this drive.

Next, once you've found your device of choice run:

```
disklarity \\.\PHYSICALDRIVE#
```

Wherein # is the number at the end of your device's ``\\.\PHYSICALDRIVE`` string.

After that, the program should guide you the rest of the way.



## Current State & Caveats:
- Runs, and presumably works. (OnMyMachine™)
- ~~Only tested on two devices (Broken MicroSD over-reporting size & random 1MB drive I found.).~~
- No GUI. Tkinter-based GUI planned.
- Missing thorough fake space checks.

## Todo:
- Add afforementioned fake space checks.
- GUI [TKinter / WebView2?]
- Increased configurability
- Simpler Device Selection
- Various Cleanups.



Thank you for your time, and enjoy! (Hopefully.)