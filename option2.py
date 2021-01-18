from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException


def auto_load(IP_LISTS):
    for IP in IP_LISTS:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'admin',
            'password': 'cisco',
            'secret': 'cisco',
        }
        print('\n### Connecting to device ' + IP.strip() + ' ###\n')
        try:
            net_connect = ConnectHandler(**Router,session_log='output.txt')
            print('### Adding default Config to Router ' + IP)
            net_connect.enable()

            output = net_connect.send_config_from_file('initial_config.txt')
            print(output + '\n')
            net_connect.disconnect()

        except NetMikoTimeoutException:
            print('Device not Reachable! Kindly check this ' + IP + ' in ip.txt')
            continue

        except NetMikoAuthenticationException:
            print('Authentication Failure')
            continue

        except SSHException:
            print('Make sure SSH is ENABLED')
            continue