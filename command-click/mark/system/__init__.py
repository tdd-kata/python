import click

from .resource import sys


@click.group()
@click.help_option("-h", "--help", help="도움말")
def system():
    """
    시스템 명령어
    """
    pass


system.add_command(sys)
