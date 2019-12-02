# -*- coding: utf-8 -*-

"""
A docopt library try program.

Usage:
 try <host> <port>
 try --host=<host> --port=<port> [--protocol=<pro>]
 try [-s] [-t] test
 try copy (-r | -d)
 try open <file>...
 try move (<from> <to>)...
 try merge [<file>]...
"""

import docopt

if __name__ == '__main__':
    
    args = docopt.docopt(__doc__, version='1.0.0')
    
    print(args)