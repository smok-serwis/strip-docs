import unittest
import os


class TestStripDocs(unittest.TestCase):
    def test_strip_docs(self):
        self.assertFalse(os.system('sudo strip-docs tests'))
        with open('tests/file_to_strip.py', 'r') as f_in:
            d = f_in.read()
        self.assertNotIn('"""', d)
