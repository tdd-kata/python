#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

from mark import __version__

@click.group()
@click.version_option(version=__version__, prog_name="mark", help="버전 정보")
@click.help_option("-h", "--help", help="도움말")
def main():
    """
    Custom Command

    >>> mark
    """

# main.add_command(net)

if __name__ == '__main__':
    main()
