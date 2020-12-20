from setuptools import setup, find_packages

from strip_docs import __version__

setup(keywords=['wheel', 'strip', 'size', 'reduction'],
      packages=find_packages(include=['doctor_wheel']),
      version=__version__,
      entry_points={
            "console_scripts": [
                  "strip-docs = strip_docs.run:run",
            ]
      }
      )
