# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

 setup(
   name='testpackage_nicpic',
   version='0.1.0',
   author='Nicolas Pichette',
   author_email='pichetten@outlook.com',
   packages=['package_name', 'package_name.test'],
   license='LICENSE.txt',
   description='Test package',
   long_description=open('README.txt').read(),
   install_requires=[
       "Python 3.7",
       "pytest",
   ],
)