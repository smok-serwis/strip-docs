# strip-docs
[![PyPI](https://img.shields.io/pypi/pyversions/strip-docs.svg)](https://pypi.python.org/pypi/strip-docs)
[![PyPI version](https://badge.fury.io/py/strip-docs.svg)](https://badge.fury.io/py/strip-docs)
[![PyPI](https://img.shields.io/pypi/implementation/strip-docs.svg)](https://pypi.python.org/pypi/strip-docs)
[![Maintainability](https://api.codeclimate.com/v1/badges/657b03d115f6e001633c/maintainability)](https://codeclimate.com/github/smok-serwis/strip-docs/maintainability)
[![Wheel](https://img.shields.io/pypi/wheel/strip-docs.svg)](https://pypi.org/project/strip-docs/)
[![Build status](https://circleci.com/gh/smok-serwis/strip-docs.svg?style=shield)](https://app.circleci.com/pipelines/github/smok-serwis/strip-docs)

A Python utility to remove all docstrings from your modules before shipping


Info-anarchized from 
[this Stack Overflow post](https://stackoverflow.com/questions/1769332/script-to-remove-python-comments-docstrings)


# Usage

Just install it via pip

```bash
pip install strip-docs
```

And then launch it on any list of files or directories that you would like
to see the docstrings gone, this way:

```bash
strip-docs dir1 dir2 file1 file2 ...
```

All .py, .pyx and .pxd files will be processed.

If you specify a single file, it will be processed

# Caveats

Try to avoid writing empty classes or routines like this:

```python
def empty_routine():
    """I am an empty routine"""
```

Because the syntax itself is not analyzed, this will result in a Python SyntaxError.

Better write this:

```python
def empty_routine():
    """I am an empty routine"""
    ...
```

So after trimming the docstrings it remains valid Python.

