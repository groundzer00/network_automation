from ping import ip_rechable
from checking_valid_ip import is_valid_ipv4_address
from option1 import auto_backup
from option2 import auto_load
from option3 import addLoopback
import fibo

# ip list
file = open("ip.txt", "r")
f = file.readlines()

# new list of IP
lists = []

# iterate on ip list
for line in f:
    if line[-1] == '\n':
        lists.append(line[:-1])
    else:
        lists.append(line)
print("=======================")
print("Checking Valid IP ")
print("=======================")
for i in lists:
    is_valid_ipv4_address(i)
print("\n=======================")

print("Checking IP Reachability")
print("=======================")
ip_rechable(lists)
print("=======================\n")

print("==========================================================")
print("Welcome to Cisco Config generator, select option to use")
print("==========================================================")
user_input = ''  # user's option

while user_input.lower() != 'q':
    print("1 - Backup Configuration Files")
    print("2 - Load initial Config to routers")
    print("3 - Load Loopback 0 Config to routers")
    print("q - Quit using this tool\n")

    user_input = input("Select Option: ")

    if user_input == "1":
        auto_backup(lists)

    elif user_input == "2":
        auto_load(lists)

    elif user_input == "3":
        addLoopback()

    elif user_input == "q":
        break

    else:
        print("Invalid Selection, Try again\n")

print("Thank you for using my Automation - Goodbye!")






