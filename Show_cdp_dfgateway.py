from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import csv

def get_facts(task):
    r = task.run(netmiko_send_command, command_string="show run all | inc cdp run")
    task.host["cdp"] = r.result
    r = task.run(netmiko_send_command, command_string="show run | inc default-gateway")
    task.host["gateway"] = r.result
    cdp = task.host['cdp']
    gateway = task.host['gateway']

    with open('devicereport.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        csvdata = (task.host.hostname, cdp, gateway)
        writer.writerow(csvdata)


       

def main() -> None:
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=get_facts)
    print_result(result)

# Python good practices
if __name__ == '__main__':
    main()
