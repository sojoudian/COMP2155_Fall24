import paramiko
import time

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Automatically add new host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the Cisco device (router/switch)
ssh_client.connect(hostname='192.168.122.100', port=22, username='u1', password='cisco')

# Create an interactive shell session
shell = ssh_client.invoke_shell()

# Wait for the shell to be ready
time.sleep(1)

# Execute the "show ip interface brief" command
shell.send("show ip interface brief\n")
time.sleep(2)  # Allow some time for the command to execute

# Receive the output from the command
output = shell.recv(10000).decode('utf-8')

# Print the output
print("Output:")
print(output)

# Close the SSH connection
ssh_client.close()
