#!/usr/bin/env python
from setuptools import setup

description = '''Intuitive and easy to use Python SDK for the Cisco DNA Center Rest API that integrates with all major versions
of the DNA Center REST API.'''

setup(
    name='dnac_api',
    version='0.0.1',
    packages=['dnac_api'],
    keywords='dnac_api Cisco DNA Center',
    url='https://github.com/superadm1n/dnac_api',
    license='GPLv3',
    author='Kyle Kowalczyk',
    author_email='kowalkyl@gmail.com',
    description='Python SDK for the Cisco DNA Rest API',
    long_description=description,
    install_requires=['requests>=2.22.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only'
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Natural Language :: English'
    ]
)