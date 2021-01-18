from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException
import datetime

def auto_backup(IP_LISTS):
    TNOW = datetime.date.today()
    for IP in IP_LISTS:
        RTR = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'admin',
            'password': 'cisco',
            'secret': 'cisco',
        }
        print('\n### Connecting to device ' + IP.strip() + ' ###\n')
        try:
            net_connect = ConnectHandler(**RTR)
        except NetMikoTimeoutException:
            print('Device not Reachable! Kindly check IP in IP-LIST')
            continue

        except NetMikoAuthenticationException:
            print('Authentication Failure')
            continue

        except SSHException:
            print('Make sure SSH is ENABLED')
            continue

        print('### Initiating Config backup')
        net_connect.enable()
        output = net_connect.send_command('show run')
        SAVE_FILE = open('Router_' + IP + '_' + str(TNOW) + '.txt', 'w')
        SAVE_FILE.write(output)
        SAVE_FILE.close()
        net_connect.disconnect()
        print('*** Done backing up config for ' + IP + '\n')
