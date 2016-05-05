if __name__ == '__main__':
    import sys
    from os.path import dirname, abspath, join

    libdir = abspath(join(dirname(__file__), '..', 'lib'))
    sys.path.insert(0, libdir)

    from tsdesktop import cmd
    sys.exit(cmd.main())
