from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

commands = input ("Enter Commands: ")
cmds = commands.split(",")

for cmd in cmds:
    nr = InitNornir("h:/Scripts/TEXTFSM/config.yaml")

    result = nr.run(
        task=netmiko_send_command,
        command_string=cmd,
        )


    print_result(result)
