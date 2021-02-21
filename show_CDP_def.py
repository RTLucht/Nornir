
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import csv
import os

nr = InitNornir(config_file="H:/Scripts/TEXTFSM/config.yaml")

IP = task.host.hostname
name = input('Enter the filename: ')
def get_facts(task):
    r = task.run(netmiko_send_command, delay_factor=4, command_string="show run all | inc cdp run")
    task.host["cdp"] = r.result
    r = task.run(netmiko_send_command, delay_factor=4, command_string="show run | inc default-gateway")
    task.host["gateway"] = r.result.split(' ')
    r = task.run(netmiko_send_command, delay_factor=4, command_string="sh run | inc ip address " + IP)
    task.host["mgmt"] = r.result.split(' ')
    r = task.run(netmiko_send_command, delay_factor=4, command_string="show version", use_textfsm=True)
    task.host["version"] = r.result
    cdp = task.host['cdp']
    subn = task.host['mgmt'][4]
    gateway = task.host['gateway'][2]
    image = task.host['version'][0]['version']
    host = task.host['version'][0]['hostname']


    filename = 'H:/Scripts/TEXTFSM/'+ name +'.csv'
    write_header = not os.path.exists(filename)
    with open(filename, 'a') as csvfile:
        headers = ['Hostname', 'IP Address', 'Subnet Mask', 'Gateway IP', 'CDP', 'Image']
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        if write_header:
            writer.writeheader()
        writer = csv.writer(csvfile)
        csvdata = (host, task.host.hostname, subn, gateway, cdp, image)
        writer.writerow(csvdata)


       



result = nr.run(task=get_facts)
print_result(result)
#import ipdb
#ipdb.set_trace()
