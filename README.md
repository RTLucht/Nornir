# Nornir
My nornir scripts that I am playing with


I found that manually adding the network devices I wanted to configure with nornir in the host.haml file would take a long time.  I put together a host.py script with a jinja2 template hots.j2.  With the username and password in the j2 file all I had to do was put a list of IP address in the device_file.txt and run the host.py script to populate my hosts.yaml file.  I would make sure you clear it out after your done with it.
