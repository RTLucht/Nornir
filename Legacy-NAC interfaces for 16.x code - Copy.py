from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config

def get_facts(task):

    # use Netmiko and TEXTFSM to pull structured data from the IOS device
    r = task.run(netmiko_send_command, command_string="show interface switchport", use_textfsm=True)
    # This creates a dictionary 
    task.host["facts"] = r.result
    
    for x in range(0,100):
        # define the commands to be sent when if Access interface, I used this for inspiration https://www.youtube.com/watch?v=Nvgcvsg6BTM
        access_commands = ['interface ' + task.host['facts'][x]['interface'], 'authentication event server dead action authorize vlan ' +
                task.host['facts'][x]['access_vlan'],
                'authentication event server dead action authorize voice',
                'authentication host-mode multi-auth',
                'authentication order dot1x mab',
                'authentication priority mab dot1x',
                'authentication port-control auto',
                'authentication periodic',
                'authentication timer reauthenticate server',
                'authentication open',
                'mab',
                'dot1x pae authenticator',
                'dot1x timeout tx-period 3']
        if "access" in task.host['facts'][x]['admin_mode']:
            access_description = task.run(netmiko_send_config, config_commands = access_commands)


# Call the get_facts function and print the results of the script, I also wanted to sace the config once the changes were made
def main() -> None:
    nr = InitNornir(config_file="h:/Scripts/TEXTFSM/config.yaml")
    result = nr.run(task=get_facts)
    print_result(result)
    
    nr = InitNornir(config_file="h:/Scripts/TEXTFSM/config.yaml")

    result1 = nr.run(netmiko_send_command, command_string="write me")
    print_result(result1)

# Python good practices
if __name__ == '__main__':
    main()
