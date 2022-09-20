import socket
import click
import psutil


@click.command(name="ipa")
@click.help_option("-h", "--help", help="도움말")
@click.option("-i", "--interface", default="all", help="네트워크 인터페이스")
def ipa(interface: str):
    """
    IP 주소 조회

    >>> mark ipa -i ipv4
    """

    addresses = psutil.net_if_addrs()
    for key, value in addresses.items():
        if interface == "ipv4":
            for network_interface in value:
                if network_interface.family == socket.AF_INET:
                    print(f"{key} : {network_interface.address}")
        else:
            for network_interface in value:
                print(f"{key} : {network_interface.address}")
