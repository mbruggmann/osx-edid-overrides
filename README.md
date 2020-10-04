# EDID overrides for Mac OS X

So we bought this new monitor from Dell (P2720DC) and connected it to our
MacBooks. Out of the box, it seemed quite blurry over the HDMI cable,
particularly with text rendering.

According to the internet, this has to do with the Macs sending the signal in
YCbCr colour format. If you suspect that you are affected by this issue, see if
you find a reference to YCbCr in the menu of the monitor settings. For the Dell,
it was in `> Menu > Color > Input Color Format`.

This being a somewhat common issue there are a few blog posts, discussion
threads and scripts for it:

* https://www.edmundofuentes.com/blog/2018/08/10/macos-external-display-antialiasing/
* https://gist.github.com/adaugherity/7435890

Compared to the method described there, this script only patches rather than
fully replaces the display configuration (as discovered by @pdutourgeerling). It
also places the override in the `/Library` folder rather than `/System/Library`,
which works without going through recovery mode.

While this did indeed switch the monitor to RGB mode for me, *use it at your own
risk*. It might not work for your monitor, your version of OS X, your display
cable, or any combination of those.

## Usage

Fetch and run the python script:
```bash
$ curl -O https://raw.githubusercontent.com/mbruggmann/osx-edid-overrides/main/generate_override.py
$ python3 generate_override.py
Found display: DELL P2720DC
Override is not present for DELL P2720DC. Install it with the following commands:
> sudo mkdir -p /Library/Displays/Contents/Resources/Overrides/DisplayVendorID-10ac
> sudo cp /Users/username/github/osx-edid-overrides/Overrides/DisplayVendorID-10ac/DisplayProductID-d0fd /Library/Displays/Contents/Resources/Overrides/DisplayVendorID-10ac/DisplayProductID-d0fd
```

That will create the necessary directory structure and file with the EDID
override next to the script, and prints the commands to install it. Feel free to
inspect the generated configuration and the commands, then go ahead and run
them.
```bash
sudo mkdir -p <overrides directory>
sudo cp <generated file> <overrides directory>
```

Changes should take effect after unplugging and reconnecting the screen. The
display name in `About this Mac > Displays` should now contain "EDID override"
(meaning that OS X picked up on the config file), and you should see your
monitor using RGB colour in the monitor settings.

## Reverting the override

If you run the script while the override is present, it will print the command
to remove it instead:
```bash
$ python3 generate_override.py
Found display: DELL P2720DC
Override is present for DELL P2720DC. Remove it with the following command:
> sudo rm /Library/Displays/Contents/Resources/Overrides/DisplayVendorID-10ac/DisplayProductID-d0fd
```

## Compatibility

We have tried this in the following configurations:

| Monitor         | Laptop                                    | OS                 | Cable   | Result                             |
| --------------- | ----------------------------------------- | ------------------ | ------- | ---------------------------------- |
| Dell P2720DC    | MacBook Pro (Retina, 13-inch, Early 2015) | Catalina (10.15.7) | HDMI    | :heavy_check_mark: Switched to RGB |

## Development

You can run the tests like so:
```bash
PYTHONPATH=. python3 test/test.py
```
