from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config
import json
import os
import csv

csvname = input('What is the name of the file ')
nr = InitNornir(config_file="h:/Scripts/csv/config.yaml")


def version():

    r = nr.run(netmiko_send_command, command_string="show version", use_textfsm=True)

    for k,v in r.items():
        
        #print(k,v[0].result)
        info = v[0].result
        for stuff in info:
            version = stuff['version']
            hostname = stuff['hostname']
            serial = stuff['serial']
            number = len(serial)
            IP = k
        authstyle(hostname,IP,version,serial,number)
        

def authstyle(hostname,IP,version,serial,number):

    s = nr.run(netmiko_send_command, command_string="authentication display config-mode")

    for k,v in s.items():
        auth = v[0].result
    makefile(hostname,IP,version,auth,serial,number)

  
def makefile(hostname,IP,version,auth,serial,number):


    filename = 'H:/CSV_ISE_Stuff/'+ csvname+'.csv'
    write_header = not os.path.exists(filename)
    with open(filename, 'a', newline='') as csvfile:
        headers = ['Hostname','Switch IP','Version','Auth Style','Serial','Number of Switches']
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        if write_header:
            writer.writeheader()
        writer = csv.writer(csvfile)

        csvdata = (hostname,IP,version,auth,serial,number)


    
        writer.writerow(csvdata)

if __name__ == "__main__":
    version()