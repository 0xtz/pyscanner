#!/usr/bin/python3
# Path: main.py
# Compare this snippet from _info.py:
#

# import the needed libraries
from rich.console import Console
from rich import print

import argparse
import datetime
import time
import sys
import socket
import concurrent.futures

import _info


# scan function
def scanner(host: str, port: int) -> None:
    # create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.6)
        try:
            if s.connect_ex((host, port)) == 0:
                console.print(f"[{port}] is open  ", style="bold green")
            else:
                print(f":x: [red][{port}] closed[/red]", end="\r ", flush=True)
        except KeyboardInterrupt:
            print("\n[!] Exiting... ")
            sys.exit()

        except Exception as e:
            pass


if __name__ == "__main__":
    # define the arguments
    parser = argparse.ArgumentParser(
        description=" A Python Multithreaded TCP Port Scanner")

    parser.add_argument('-t', '--target', dest='target',
                        help='Target IP address', required=True)
    parser.add_argument('-p', '--port', nargs="+", dest='port',
                        help='Specify a port to knock', required=False)
    parser.add_argument('-f', '--fast', action="store_true",
                        help='Fast Scan, the top 1k ports', required=False)
    args = parser.parse_args()

    # create a console
    console = Console()

    console.print(_info.pyscanners.banner, style="italic yellow3")

    console.print(
        f" :star: starting pyscanner at {datetime.datetime.now()} ", style="bold yellow3")
    console.print(
        f" :boom: scan report for [bold]{args.target}[/bold]\n", style="bold blue")

    start_time = time.perf_counter()

    if args.port:
        # ports = [args.port]
        # min(32, os.cpu_count() + 4) -> f
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in args.port:
                executor.submit(scanner, args.target, int(port))
    else:
        # create a thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            # if fast scan is selected
            if args.fast:
                for port in _info.pyscanners.top_ports:
                    executor.submit(scanner, args.target, port)
                pass
            else:
                for port in range(65535):  # tcp ports range 65535
                    executor.submit(scanner, args.target, port)

    print(f"Done {' '*10} \n", end="\n", flush=True)
    console.print(
        f":star: finished at {(time.perf_counter() - start_time):0.02f} ", style="yellow3")
