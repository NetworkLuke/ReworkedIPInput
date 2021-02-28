from netmiko import ConnectHandler

device = (input('Please enter IP address of devices, seperated by a space: ') .split())

print(device)

device_type = 'cisco_ios_telnet'
username = 'networkluke'
password = 'networkluke'

for device in device:
    net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
    prompter = net_connect.findprompt()
    if '>' in prompter:
        net_connect.enable()
        
    print("You are now conencted to " + device + "!")