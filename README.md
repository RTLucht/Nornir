# Nornir
My nornir scripts that I am playing with, I found ntc-templates to be very helpful with scripting out what I wanted to do.

https://pypi.org/project/ntc-templates/



I had some troubles though, be defualt the scripts I ran would look in the folder where these are saved but I kept getting a permissions error.

So I had to set a Enviorment Varialbe on my Windows 10 machine

I copied the ntc_templates folder to my C: and created a System Variable  (Variable name) NET_TEXTFSM (Variable value) C:\ntc_templates\templates and my scripts 
using textfsm worked beautiful.

I would also check out IPvZero's channel on youtube https://www.youtube.com/channel/UCQ7d_M3T1TdVX3Nnxp6wmAA 


I found that manually adding the network devices I wanted to configure with nornir in the host.haml file would take a long time.  I put together a host.py script with a jinja2 template hots.j2.  With the username and password in the j2 file all I had to do was put a list of IP address in the device_file.txt and run the host.py script to populate my hosts.yaml file.  I would make sure you clear it out after your done with it.
