import unittest
from strip_docs.strip_docs import do_path


class TestStripDocs(unittest.TestCase):
    def test_strip_docs(self):
        do_path('tests')
        with open('tests/file_to_strip.py', 'r') as f_in:
            d = f_in.read()
        self.assertNotIn('"""', d)
