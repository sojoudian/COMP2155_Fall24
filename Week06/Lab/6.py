import paramiko
import time

def save_running_to_startup():
    # Create an SSH client instance
    ssh_client = paramiko.SSHClient()
    
    # Load the system's known hosts (to verify the server's authenticity)
    ssh_client.load_system_host_keys()
    
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

    # Provide the enable password (replace 'cisco' with the actual enable password)
    shell.send("cisco\n")
    time.sleep(1)

    # Send the command to save the running configuration to the startup configuration
    shell.send("copy running-config startup-config\n")
    time.sleep(2)

    # Handle any confirmation prompts (some devices ask for confirmation)
    shell.send("\n")  # Send a newline to confirm the copy
    time.sleep(2)

    # Optionally, verify the configuration is saved (show running-config or related command)
    shell.send("show running-config | include clock\n")
    time.sleep(2)

    # Receive and print the output
    output = shell.recv(10000).decode('utf-8')
    print("Output:")
    print(output)

    # Close the SSH connection
    ssh_client.close()

if __name__ == '__main__':
    save_running_to_startup()
