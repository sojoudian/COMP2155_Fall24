import paramiko
import time

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Load the system's known hosts (to verify the server's authenticity)
ssh_client.load_system_host_keys()

# Automatically add new host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh_client.connect(hostname='your_remote_host', port=22, username='your_username', password='your_password')

# Invoke an interactive shell session
shell = ssh_client.invoke_shell()

# Send a command to the remote shell (e.g., 'show version')
shell.send("show version\n")

# Pause execution for 1 second to allow command execution
time.sleep(1)

# Receive and read the response (adjust the byte size as needed)
response = shell.recv(1000)  # Read up to 1000 bytes

# Decode the output to a string (UTF-8)
output = response.decode('utf-8')

# Print the output
print(output)

# Close the SSH connection
ssh_client.close()
