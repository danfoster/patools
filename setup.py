#!/usr/bin/env python3

from setuptools import setup

setup(
    name='patools',
    version='0.0.1',
    packages=['patools'],
    entry_points = {
        'console_scripts': [
            'pa_setoutput = patools.setoutput:main'
        ]
    },
    install_requires = [
        'pulsectl'
    ]
)
