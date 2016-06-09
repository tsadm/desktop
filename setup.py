#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from os import path
from setuptools import setup

sys.path.insert(0, path.join(path.curdir, 'lib'))
from tsdesktop import version

desc = """tsadm desktop client - docker based environments for running web sites locally"""

install_requires=[
    'bottle>=0.12.9',
    'docker-py>=1.8.1',
]
if sys.version_info.major == 2:
    install_requires.append('configparser>=3.5.0')

setup(
    name=version.APPNAME,
    version=version.VERSION,

    description=desc,
    long_description=desc,

    license='BSD',
    url='https://github.com/tsadm/desktop',

    author='Jeremías Casteglione',
    author_email='jeremias@tincan.co.uk',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],

    install_requires=install_requires,

    packages=[
        'tsdesktop',
        'tsdesktop.bottman',
        'tsdesktop.bottman.views',
        'tsdesktop.dockman',
    ],
    package_dir={
        'tsdesktop': 'lib/tsdesktop',
    },
    package_data={
        'tsdesktop.bottman': [
            'templates/*.tpl',
            'templates/inc/*.tpl',
            'templates/static/*.css',
            'templates/static/*.ico',
            'templates/static/*.js',
        ],
    },

    entry_points={
        'console_scripts': [
            'tsdesktop=tsdesktop.cmd:main',
        ],
    },
)
