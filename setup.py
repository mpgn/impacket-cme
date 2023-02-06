#!/usr/bin/env python
# Impacket - Collection of Python classes for working with network protocols.
#
# Copyright (C) 2022 Fortra. All rights reserved.
#
# This software is provided under a slightly modified version
# of the Apache Software License. See the accompanying LICENSE file
# for more information.
#
# Description:
#   Setup file
#
import glob
import os
import platform

from setuptools import setup
from subprocess import *

PACKAGE_NAME = "impacket"

VER_MAJOR = 0
VER_MINOR = 10
VER_MAINT = 1
VER_PREREL = "dev1"
try:
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) == 0:
        p = Popen("git log -1 --format=%cd --date=format:%Y%m%d.%H%M%S", shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
        (outstr, __) = p.communicate()
        (VER_CDATE,VER_CTIME) = outstr.strip().decode("utf-8").split('.')

        p = Popen("git rev-parse --short HEAD", shell=True, stdin=PIPE, stderr=PIPE, stdout=PIPE)
        (outstr, __) = p.communicate()
        VER_CHASH = outstr.strip().decode("utf-8")

        VER_LOCAL = "+{}.{}.{}".format(VER_CDATE, VER_CTIME, VER_CHASH)
    else:
        VER_LOCAL = ""
except Exception:
    VER_LOCAL = ""

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=PACKAGE_NAME,
    version="{}.{}.{}.{}{}".format(VER_MAJOR, VER_MINOR, VER_MAINT, VER_PREREL, VER_LOCAL),
    description="Network protocols Constructors and Dissectors",
    url="https://www.coresecurity.com",
    author="SecureAuth Corporation",
    maintainer="Fortra",
    license="Apache modified",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    platforms=["Unix", "Windows"],
    packages=['impacket', 'impacket.dcerpc', 'impacket.dcerpc.v5', 'impacket.dcerpc.v5.dcom',
              'impacket.krb5', 'impacket.ldap'],
    install_requires=['pyasn1>=0.2.3', 'pycryptodomex', 'pyOpenSSL>=21.0.0', 'six', 'ldap3>=2.5,!=2.5.2,!=2.5.0,!=2.6',
                      'ldapdomaindump>=0.9.0', 'flask>=1.0', 'future', 'charset_normalizer', 'dsinternals'],
    extras_require={'pyreadline:sys_platform=="win32"': [],
                    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
    ]
)
