iimport paramiko
import time

def configure_timezone():
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    
    # Automatically add new host keys
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the Cisco device (replace with your actual device details)
    ssh_client.connect(hostname='192.168.122.100', port=22, username='u1', password='cisco')

    # Create an interactive shell session
    shell = ssh_client.invoke_shell()
    
    # Wait for the shell to be ready
    time.sleep(1)

    # Enter enable mode
    shell.send("enable\n")
    time.sleep(1)

    # Provide the enable password
    shell.send("cisco\n")
    time.sleep(1)

    # Enter global configuration mode
    shell.send("configure terminal\n")
    time.sleep(1)

    # Set the time zone to EST (Eastern Standard Time, UTC -5)
    shell.send("clock timezone EST -5\n")
    time.sleep(1)

    # Enable daylight saving time (EDT, automatic adjustment)
    shell.send("clock summer-time EDT recurring\n")
    time.sleep(1)

    # Exit configuration mode
    shell.send("end\n")
    time.sleep(1)

    # # Save the configuration (optional, to make changes persistent across reboots)
    # shell.send("write memory\n")
    # time.sleep(2)

    # Verify the new time zone settings by showing the clock
    shell.send("show clock\n")
    time.sleep(2)

    # Receive and print the output
    output = shell.recv(10000).decode('utf-8')
    print("Output:")
    print(output)

    # Close the SSH connection
    ssh_client.close()

if __name__ == '__main__':
    configure_timezone()
