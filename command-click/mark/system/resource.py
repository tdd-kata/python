import click
import psutil


@click.command(name="sys")
@click.help_option("-h", "--help", help="도움말")
def sys():
    """
    시스템 리소스 사용량 조회

    >>> mark sys
    """

    print("\n[CPU]")
    physical_core = psutil.cpu_count(logical=False)
    print(f"CPU 물리 코어 수 : {physical_core}")

    logical_core = psutil.cpu_count(logical=True)
    print(f"CPU 논리 코어 수 : {logical_core}")

    print("\n[Virtual Memory]")
    memory = psutil.virtual_memory()
    print(f"총 메모리 : {to_gb(memory.total)} GB")
    print(f"메모리 사용량 : {to_gb(memory.used)} GB")
    print(f"메모리 사용률 : {memory.percent}%")

    print("\n[Swap Memory]")
    swap = psutil.swap_memory()
    print(f"총 Swap 메모리 : {to_gb(swap.total)} GB")
    print(f"Swap 메모리 사용량 : {to_gb(swap.used)} GB")
    print(f"Swap 메모리 사용률 : {swap.percent}%")


def to_gb(byte_unit: int) -> str:
    # [PEP 498 - Literal String Interpolation](https://peps.python.org/pep-0498/)
    # f-string is a literal string, prefixed with 'f'
    return f"{byte_unit / 1024 / 1024 / 1024:.2f}"
