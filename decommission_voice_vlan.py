from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

vlan = input('Vlan ID You Would like to remove: ')

config_commands = ['no vlan ' + vlan]

def get_facts(task, vlan):

    # use Netmiko to poll devices for switchport infomation, and return structured response with textFSM
    r = task.run(netmiko_send_command, command_string="show interface switchport", use_textfsm=True)
    # save the result of the Show Command under the dict key "facts" so we can access the structered results for parsing
    task.host["facts"] = r.result
    
    for x in range(0,100):
        
        
        # define the commands to be sent when if Access interface
        access_commands = ['interface ' + task.host['facts'][x]['interface'], 'no switchport voice vlan ' +vlan]
        # define the commands to be sent when if Trunk interface
        trunk_commands = ['interface ' + task.host['facts'][x]['interface'], 'switchport trunk allowed vlan remove ' +vlan]
        if "access" in task.host['facts'][x]['admin_mode'] and vlan in task.host['facts'][x]['voice_vlan']:
            access_config = task.run(netmiko_send_config, config_commands = access_commands)
        elif "trunk" in task.host['facts'][x]['admin_mode'] and not "member of bundle" in task.host['facts'][x]['mode'] and vlan in task.host['facts'][x]['trunking_vlans'][0].split(','):
            trunk_config = task.run(netmiko_send_config, config_commands = trunk_commands)


# Call the get_facts function and print the results of the script
def main() -> None:


    nr = InitNornir(config_file="H:/NORNIR/config.yaml")
    
    result = nr.run(task=get_facts,vlan=vlan)
    print_result(result)

    nr = InitNornir(config_file="H:/NORNIR/config.yaml")
    removevlan = nr.run(netmiko_send_config, config_commands=config_commands)
    print_result(removevlan)
    
    nr = InitNornir(config_file="H:/NORNIR/config.yaml")
    result1 = nr.run(netmiko_send_command, command_string="write me")
    print_result(result1)

# Python good practices
if __name__ == '__main__':
    main()
