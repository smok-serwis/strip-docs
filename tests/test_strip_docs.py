import unittest
import os


class TestStripDocs(unittest.TestCase):
    def test_strip_docs(self):
        os.system('strip-docs tests/file_to_strip.py')
        with open('tests/file_to_strip.py', 'r') as f_in:
            d = f_in.read()
        self.assertNotIn('"""', d)
