#!/usr/bin/env python
import argparse
import hashlib
import sys
import os

def main():
    args = parse_args()
    filename = args.filename
    if os.path.isfile(filename):
        try:
            filedata = open(filename,'rb').read()
            md5hash = hashlib.md5(filedata).hexdigest()
            print("{0} is the md5 hash for file '{1}'".format(md5hash, filename))
        except Exception as e:
            print("Error: an exception occurred. \n{0}".format(str(e)))
            raise e
    else:
        print("Error: file '{0}' does not exist.".format(filename))
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '-f',
                        '--filename',
                        type=str,
                        required=True,
                        help='Path to the filename. Example: /tmp/example.iso'
                    )
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
~             
