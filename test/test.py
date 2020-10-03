import unittest
from pathlib import Path

from generate_override import find_display_data

class TestEdidOverrides(unittest.TestCase):

    def test_ioreg_parser(self):
        ioreg_output = Path('test/ioreg-output.txt').read_text()
        displays = find_display_data(ioreg_output)
        self.assertEqual(1, len(displays))

        display = displays[0]
        self.assertEqual(display.vendor_id, 4268)
        self.assertEqual(display.product_id, 53501)
        self.assertEqual(display.name, 'DELL P2720DC')


if __name__ == '__main__':
    unittest.main()
