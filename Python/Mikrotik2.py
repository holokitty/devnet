import netmiko
frome netmiko import ConnectHandler

mikrotik_router_1 = {
    'device_type' = 'mikrotik_routeros',
    'host': '192.168.1.19',
    'port' = '22',
    'username' = 'admin+ct',
    'password' = '456KS0lsnf',
}
sshCli = ConnectHandler(**mikrotik_router_1)
output = sshCli.send_command("/ip address print")
print(output)
sshCli.disconnect()

