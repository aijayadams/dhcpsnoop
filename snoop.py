#!/usr/bin/env python3.7
import click
import datetime
from dhcpsnoop.snooper import Snooper


def set_presence(src: str) -> None:
    print("Update Presence")

@click.command()
@click.option(
    "--config-file", "-c", default="/etc/snoop.conf", help="Configuration file to load."
)
def start_snoop(config_file: str) -> None:
    s = Snooper(config_file=config_file, callback=set_presence, filter="port 68")
    s.snoop()
    print("Snooping Ended")

if __name__ == "__main__":
    start_snoop()
