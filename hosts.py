from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('Z:\Scripts\Python2')

env = Environment(loader=file_loader)
template = env.get_template('host.j2')
with open('Z:\Scripts\Python2\device_file.txt') as f:
    IPS = f.read().splitlines()
    file = open('Z:\Scripts\Python2\hosts.yaml','a')
    output = template.render(IPS=IPS)
    #Print the output
    print(output)
    file.write(output)
    file.close()
