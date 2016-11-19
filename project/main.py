#!/usr/bin/python
__author__ = 'skami'

import sys
from lib import Options

#print "Hello World!"


if __name__ == '__main__':
    options = Options()
    opts = options.parse(sys.argv[1:])
    if opts.verbose:
        print "test"
