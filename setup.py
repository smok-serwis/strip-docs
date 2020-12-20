from setuptools import setup, find_packages

from doctor_wheel import __version__

setup(keywords=['wheel', 'strip', 'size', 'reduction'],
      packages=find_packages(include=['doctor_wheel']),
      version=__version__,
      entry_points={
            "console_scripts": [
                  "strip-docs = strip_docs.strip_docs:run",
            ]
      }
      )
