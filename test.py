#!/usr/bin/env python3
import sys, platform
from os import path
from unittest import TestLoader, TextTestRunner

print("Python {} ({} {})".format(platform.python_version(), platform.system(), platform.machine()))

if not '--test-installed' in sys.argv:
    libdir = path.join(path.abspath(path.curdir), 'lib')
    sys.path.insert(0, libdir)

from tsdesktop import version
version.println()

ldr = TestLoader()
suite = ldr.discover('tsdesktop', '*_test.py')

verbose = 1
if '-v' in sys.argv: verbose = 2

rnr = TextTestRunner(verbosity=verbose)
rst = rnr.run(suite)

sys.exit(len(rst.errors))
