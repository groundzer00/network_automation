import subprocess

def ip_rechable(lists):
    for ip in lists:
        ping_rep = subprocess.call('ping %s /n 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ping_rep == 0:
            print(f"{ip} is Rechable")
            continue

        else:
            print(f"{ip} is not Rechable")
            continue
