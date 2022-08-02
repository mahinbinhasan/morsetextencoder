from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Morse to Text and text to morse Decoder and Encoder'
setup(
    name="mahinmorsetext"
    version=VERSION,
    author="Mahin Bin Hasan (mahinbinhasan)",
    author_email="<allmahin149@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'morsecode','morsetotext','decoder','encoder','morsedecoder'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Everyone",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)