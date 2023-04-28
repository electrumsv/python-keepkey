#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='electrumsv-keepkey',
    version='6.1.0',
    author='TREZOR and KeepKey and ElectrumSV',
    author_email='roger.taylor.email@gmail.com',
    description='Python library for communicating with KeepKey Hardware Wallet',
    url='https://github.com/electrumsv/python-keepkey',
    packages=find_packages(exclude=['tests']),
    scripts = ['keepkeyctl'],
    test_suite='tests/**/test_*.py',
    install_requires=[
        'ecdsa>=0.9',
        'protobuf>=3.0.0',
        'mnemonic>=0.8',
        'hidapi>=0.7.99.post15',
        'libusb1>=1.6'
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
)
