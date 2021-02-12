from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

config_commands = ['vlan 1994', 'name Hosted_VOIP']

def get_facts(task):

    # use Netmiko to poll devices for switchport infomation, and return structured response with textFSM
    r = task.run(netmiko_send_command, command_string="show interface switchport", use_textfsm=True)
    # save the result of the Show Command under the dict key "facts" so we can access the structered results for parsing
    task.host["facts"] = r.result
    l = len(r.result)

    for x in range(0,l):
        
        # define the commands to be sent when if Access interface
        access_commands = ['interface ' + task.host['facts'][x]['interface'], 'switchport voice vlan 1994']
        # define the commands to be sent when if Trunk interface
        trunk_commands = ['interface ' + task.host['facts'][x]['interface'], 'switchport trunk allowed vlan add 1994']
        #Conditions of the interface 
        if "access" in task.host['facts'][x]['admin_mode']:
            access_config = task.run(netmiko_send_config, config_commands = access_commands)
        elif "trunk" in task.host['facts'][x]['admin_mode']:
            trunk_config = task.run(netmiko_send_config, config_commands = trunk_commands)


# Call the get_facts function and print the results of the script
def main() -> None:
    
    nr = InitNornir(config_file="Z:\Scripts\Python2\config.yaml")
    vocievlan = nr.run(netmiko_send_config, config_commands=config_commands)
    print_result(vocievlan)

    nr = InitNornir(config_file="Z:\Scripts\Python2\config.yaml")
    result = nr.run(task=get_facts)
    print_result(result)

    nr = InitNornir(config_file="Z:\Scripts\Python2\config.yaml")
    result1 = nr.run(netmiko_send_command, command_string="write me")
    print_result(result1)

# Python good practices
if __name__ == '__main__':
    main()
