import unittest
import os
from strip_docs.strip_docs import do_file


class TestStripDocs(unittest.TestCase):
    def test_strip_docs(self):
        do_file('tests')
        with open('tests/file_to_strip.py', 'r') as f_in:
            d = f_in.read()
        self.assertNotIn('"""', d)
