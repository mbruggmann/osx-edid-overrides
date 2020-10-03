import subprocess
import re
from pathlib import Path


def get_display_edids():
    """
    Finds (vendorid, productid, edid) tuples for every connected display
    """
    cmd = ['ioreg', '-l', '-d0', '-w', '0', '-r', '-c', 'AppleDisplay']
    output = subprocess.run(cmd, text=True, capture_output=True).stdout

    edids = re.findall("IODisplayEDID.*?<([a-z0-9]+)>", output)
    vendorids = re.findall("DisplayVendorID.*?([0-9]+)", output)
    productids = re.findall("DisplayProductID.*?([0-9]+)", output)

    return list(zip(vendorids, productids, edids))


def display_name_from_edid(edid):
    """
    Extract the name of the display from the EDID data

    The monitor name is stored in the 13 bytes of text following "000000fc00".
    If the name is shorter, it is terminated with a newline (0a) and then
    padded with spaces.

    See https://en.wikipedia.org/wiki/Extended_Display_Identification_Data
    """
    display_name_descriptor = '000000fc00'
    if not display_name_descriptor in edid:
        return 'Display'

    from_index = edid.index(display_name_descriptor) + 10
    to_index = from_index + 26

    name_hex = edid[from_index:to_index]
    name = bytearray.fromhex(name_hex).decode().rstrip()

    return name


def generate_override_file(vendorid, productid, name):
    """
    Generates an override file for the display
    """
    vendorpath = "DisplayVendorID-%0.2x" % int(vendorid)
    productpath = "DisplayProductId-%0.2x" % int(productid)
    path = Path('.') / 'Overrides' / vendorpath / productpath

    if path.exists():
        print('File already exists, nothing to do', path)
        return path

    print('Generating file', path)
    if not path.parent.exists():
        path.parent.mkdir()

    path.touch()
    path.write_text(f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>DisplayProductName</key>
	<string>{name} (EDID override)</string>
	<key>edid-patches</key>
	<array>
		<dict>
			<key>offset</key>
			<integer>131</integer>
			<key>data</key>
			<data>wQ==</data>
		</dict>
	</array>
</dict>
</plist>""")

    return path


def print_install_command(name, path):
    """
    Print out the command to install the override
    """
    print(f"Install the override for {name} with the following command:")

    overrides = Path('/Library/Displays/Contents/Resources')
    source = path.absolute()
    target = overrides / path
    directory = target.parent

    print(f"sudo mkdir -p {directory} && sudo cp {source} {target}")


def main():
    for display in get_display_edids():
        vendorid = display[0]
        productid = display[1]
        edid = display[2]
        name = display_name_from_edid(edid)
        path = generate_override_file(vendorid, productid, name)
        print_install_command(name, path)


if __name__ == "__main__":
    main()
