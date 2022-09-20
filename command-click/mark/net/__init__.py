import click

from .ip_address import ipa


@click.group()
@click.help_option("-h", "--help", help="도움말")
def net():
    """
    네트워크 명령어
    """
    pass


net.add_command(ipa)
