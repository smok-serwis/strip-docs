from __future__ import print_function

import os

try:
    import io
except ImportError:
    import cStringIO as io
import token
import tokenize


def do_path(pathname):
    if os.path.isdir(pathname):
        for rootdir, dirs, files in os.walk(pathname):
            for file in files:
                if file.endswith('.py') or file.endswith('.pyx') or file.endswith('.pxd'):
                    path = os.path.join(rootdir, file)
                    print('Doing %s' % (path,))
                    do_file(path)
    else:
        do_file(pathname)


def do_file(fname):
    """ Run on just one file.

    """
    mod = io.StringIO()
    with open(fname, "r") as source:

        prev_toktype = token.INDENT
        first_line = None
        last_lineno = -1
        last_col = 0

        tokgen = tokenize.generate_tokens(source.readline)
        for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
            if 0:  # Change to if 1 to see the tokens fly by.
                print(u'%10s %-14s %-20r %r' % (
                    tokenize.tok_name.get(toktype, toktype),
                    '%d.%d-%d.%d' % (slineno, scol, elineno, ecol),
                    ttext, ltext
                ))
            if isinstance(ttext, bytes):
                ttext = ttext.decode('utf-8')
            if slineno > last_lineno:
                last_col = 0
            if scol > last_col:
                mod.write(u" " * (scol - last_col))
            if toktype == token.STRING and prev_toktype == token.INDENT:
                # Docstring
                mod.write(u"#--")
            elif toktype == tokenize.COMMENT:
                # Comment
                mod.write(u"##\n")
            else:
                mod.write(ttext)
            prev_toktype = toktype
            last_col = ecol
            last_lineno = elineno

    with open(fname, 'w') as f_out:
        f_out.write(mod.getvalue())
