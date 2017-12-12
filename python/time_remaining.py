#!/usr/bin/env python
import datetime
import argparse
import sys

def main():
    args = parse_args()
    target = date_from_args(args)
    today = datetime.datetime.now()
    print "Time Right Now: \t"+str(today.replace(microsecond=0))
    print str(args.description)+": \t"+str(target)
    difference = target - today
    print "Days Remaining: \t"+str(difference)

def date_from_args(args):
    target = None
    try:
        target = datetime.datetime(args.year, args.month, args.day, args.hour, args.minute, args.second)
    except Exception as e:
        print "Failed to calculate date, please try again."
        sys.exit()
    return target

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--year', type=int, help='Year in the format of YYYY. Required Int.')
    parser.add_argument('-m', '--month', type=int, help='Month in the format of (M)M. E.g., 1 or 12. Required Int.')
    parser.add_argument('-d', '--day', type=int, help='Day in the format of (D)D. E.g., 6 or 26. Required Int.')
    parser.add_argument('-o', '--hour', type=int, help='24 Hour in the format of (H)H. E.g., 8 for 8AM or 20 for 8PM. Required Int.')
    parser.add_argument('-i', '--minute', type=int, help='Minute in the format of (M)M. E.g., 5 or 50. Required Int.')
    parser.add_argument('-s', '--second', type=int, help='Second in the format of (S)S. E.g., 5 or 50. Required Int.')
    parser.add_argument('-e', '--description', type=str, default="The Target Date", help='Describe your target date as a string. E.g., "Birthday" or "Solstice"')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
