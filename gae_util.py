#!/usr/bin/env python
"""GAE utils script."""

import os
import argparse
import subprocess


def main():  # noqa
    """Operation related to GAE app."""
    parser = argparse.ArgumentParser(description='GAE Utility tool.')

    front_group = parser.add_argument_group('front')
    front_group.add_argument('-front',
                             help='Build frontend.',
                             action='store_true')

    front_group.add_argument('--build', '--b',
                             help='Build frontend project.',
                             action='store_true')
    front_group.add_argument('--start', '--s',
                             help='Start Frontend server.',
                             action='store_true')
    front_group.add_argument('--test', '--t',
                             help='Start Frontend server.',
                             action='store_true')

    args = parser.parse_args()

    if args.front:
        # Start Frontend server
        os.chdir('frontend')

        subprocess.call(['yarn'])

        if args.test:
            subprocess.call(['yarn', 'test'])

        if args.build:
            subprocess.call(['yarn', 'build'])
        elif args.start:
            subprocess.call(['yarn', 'start'])

        os.chdir('..')  # Go back to previous folder

if __name__ == "__main__":
    main()
