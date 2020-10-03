import unittest
from pathlib import Path

from generate_override import Display, find_display_data, path_for_override_file

class TestEdidOverrides(unittest.TestCase):

    def test_find_display_data(self):
        ioreg_output = Path('test/ioreg-output.txt').read_text()
        displays = find_display_data(ioreg_output)
        self.assertEqual(1, len(displays))

        display = displays[0]
        self.assertEqual(display.vendor_id, 4268)
        self.assertEqual(display.product_id, 53501)
        self.assertEqual(display.name, 'DELL P2720DC')

    def test_path_for_override_file(self):
        display = Display(
            vendor_id = 4268,
            product_id = 53501,
            name = 'display',
            edid = 'foobar'
        )
        path = path_for_override_file(display)
        self.assertEqual(path, Path('Overrides/DisplayVendorID-10ac/DisplayProductID-d0fd'))


if __name__ == '__main__':
    unittest.main()
