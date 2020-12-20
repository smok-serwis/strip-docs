import sys
from strip_docs.strip_docs import do_path


def run():
    if len(sys.argv) == 1:
        print('''Use as:

strip-docs <name of directory with py, pyx and pyd files>
''')
        sys.exit(1)
    for dir_or_file_name in sys.argv[1]:
        do_path(dir_or_file_name)
