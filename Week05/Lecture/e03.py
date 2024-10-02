import paramiko

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Load the system's known hosts (to verify the server's authenticity)
ssh_client.load_system_host_keys()

# Automatically add new host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh_client.connect(hostname='your_remote_host', port=22, username='your_username', password='your_password')

# Execute the command
stdin, stdout, stderr = ssh_client.exec_command("ls")

# Fetch the standard output and error
output = stdout.read().decode('utf-8')
error = stderr.read().decode('utf-8')

# Print the output and error (if any)
if output:
    print("Output:")
    print(output)

if error:
    print("Error:")
    print(error)

# Close the SSH connection
ssh_client.close()