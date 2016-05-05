#!/usr/bin/env python3

import sys
from os.path import dirname, abspath, join

libdir = abspath(join(dirname(__file__), '..', 'lib'))
sys.path.insert(0, libdir)

ziplib = abspath(join(libdir, 'tsdesktop.zip'))
sys.path.insert(0, ziplib)

from tsdesktop import cmd
sys.exit(cmd.main())
