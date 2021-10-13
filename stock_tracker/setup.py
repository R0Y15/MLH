"""setup/install script for ystockquote"""


import os
from distutils.core import setup

from ystockquote import __version__

direct = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(direct, 'README.rst')) as f:
    LONG_DESCRIPTION = '\n' + f.read()

setup(
    name='ystockquote',
    version=__version__,
    py_modules=['ystockquote'],
    author='Corey Goldberg',
    author_email='cgoldberg _at_ gmail.com',
    description='retrieve stock quote data from Yahoo Finance',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/cgoldberg/ystockquote',
    download_url='http://pypi.python.org/pypi/ystockquote',
    keywords='stocks stockmarket market finance yahoo quotes'.split(),
    license='GNU LGPLv2+',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Investment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
