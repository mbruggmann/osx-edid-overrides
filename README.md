# EDID overrides for Mac OS X

So we bought this new monitor from Dell (P2720DC) and connected it to our
MacBooks. Out of the box, it seemed quite blurry with both the USB-C and HDMI
cables, particularly with text rendering.

According to the internet, this has to do with the Macs sending the signal in
YCbCr colour format. If you suspect that you are affected by this issue, see if
you find a reference to YCbCr in the menu of the monitor settings. For the Dell,
it was in `> Menu > Color > Input Color Format`.

This being a somewhat common issue there are a few blog posts, discussion
threads and scripts for it:

* https://www.edmundofuentes.com/blog/2018/08/10/macos-external-display-antialiasing/
* https://gist.github.com/adaugherity/7435890

Compared to the method described there, this script only patches rather than
fully replaces the display configuration (as discovered by @pdutourgeerling).
It also places the override in the `/Library` rather than `/System/Library`
location which works without going into recovery mode or even rebooting.

While this worked for me, ~use it at your own risk~. It might not work for your
monitor, your version of OS X, your display cable, or any combination of those.

## Usage

Clone the repository and run the python script:
```bash
$ git clone https://github.com/mbruggmann/osx-edid-overrides
$ cd osx-edid-overrides
$ python3 generate_override.py
Generating file Overrides/DisplayVendorID-10ac/DisplayProductId-d0fd
Install the override for DELL P2720DC with the following command:
sudo mkdir -p /Library/Displays/Contents/Resources/Overrides/DisplayVendorID-10ac && sudo cp /Users/username/github/osx-edid-overrides/Overrides/DisplayVendorID-10ac/DisplayProductId-d0fd /Library/Displays/Contents/Resources/Overrides/DisplayVendorID-10ac/DisplayProductId-d0fd
```

That will create the necessary directory structure and file with the EDID
override next to the script, and prints the commands to install it. Feel free to
inspect the generated configuration and the commands, then go ahead and run them.
```bash
sudo mkdir -p <overrides directory>
sudo cp <generated file> <overrides directory>
```

Changes should take effect after unplugging and reconnecting the screen. The
display name in `About this Mac > Displays` should now contain "EDID override"
(meaning the OS X picked up on the config file), and you should see your monitor
using RGB colour in the monitor settings.

## Compatibility

It has shown to work in the following configurations:

| Monitor         | Laptop               | Cable   | Result                             |
| --------------- | -------------------- | ------- | ---------------------------------- |
| Dell P2720DC    | MacBook Pro 13, 2015 | HDMI    | :heavy_check_mark: Switched to RGB |
