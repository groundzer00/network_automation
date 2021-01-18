import socket
import sys

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
        print(f"{address} is Valid")
    except socket.error:
        if address.count('.') == 3:
            print(f"{address} is inValid IP Address, exiting ....")
            sys.exit()
