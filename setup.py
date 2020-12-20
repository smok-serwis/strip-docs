from setuptools import setup, find_packages

from strip_docs import __version__

setup(keywords=['docs', 'stripping', 'pydoc', 'removal'],
      packages=find_packages(include=['strip_docs']),
      version=__version__,
      entry_points={
            "console_scripts": [
                  "strip-docs = strip_docs.run:run",
            ]
      }
      )
