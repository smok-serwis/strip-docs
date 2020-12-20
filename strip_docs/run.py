import sys
import os
from strip_docs.strip_docs import do_file


def run():
    if len(sys.argv) == 1:
        print('''Use as:

strip-docs <name of directory with py, pyx and pyd files>
''')
        sys.exit(1)
    for dir_or_file_name in sys.argv[1]:
        if os.path.isdir(dir_or_file_name):
            for rootdir, dirs, files in os.walk(dir_or_file_name):
                for file in files:
                    if file.endswith('.py') or file.endswith('.pyx') or file.endswith('.pxd'):
                        path = os.path.join(rootdir, file)
                        print('Doing %s' % (path,))
                        do_file(path)
        else:
            print('Doing %s' % (dir_or_file_name, ))
            do_file(dir_or_file_name)
