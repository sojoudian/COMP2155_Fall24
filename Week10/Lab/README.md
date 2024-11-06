# Week 10 Lab

## How to connect to the Cisco Router and change from the USER EXEC mode to the GLOBAL CONFIG mode.
```python
from netmiko import ConnectHandler

connection = {
    'host': '192.168.122.100',
    'username': 'u1',
    'password': 'cisco',
    'secret': 'cisco',    
    'device_type': 'cisco_ios'
}
```
