from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
from rtr_inventory import routers, loopbacks


def addLoopback():
    for devicelist, ips in zip(routers, loopbacks):
        try:
            net_connect = ConnectHandler(**devicelist)
            net_connect.enable()
            config_commands = ['int loop0',
                               'ip address ' + ips + ' 255.255.255.255',
                               'description Created with Python and Netmiko!!']
            output = net_connect.send_config_set(config_commands)
            print(output)
            net_connect.disconnect()
            print("Done adding loopback 0 to all routers!")

        except NetMikoTimeoutException:
            print('Device not Reachable! Kindly check this')
            continue

        except NetMikoAuthenticationException:
            print('Authentication Failure')
            continue

        except SSHException:
            print('Make sure SSH is ENABLED')
            continue
