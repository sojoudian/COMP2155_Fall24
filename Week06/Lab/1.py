import paramiko

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Automatically add new host keys
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the Cisco device (router/switch)
ssh_client.connect(hostname='192.168.122.100', port=22, username='u1', password='cisco')

try:
    # Execute the "show ip interface brief" command
    stdin, stdout, stderr = ssh_client.exec_command("show ip interface brief")

    # Fetch the output and error
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    # Print the output and error (if any)
    if output:
        print("Output:")
        print(output)

    if error:
        print("Error:")
        print(error)

finally:
    # Manually close the session and transport to avoid resource issues
    stdout.channel.close()  # Ensure the channel is properly closed
    ssh_client.close()      # Ensure the SSH client is properly closed
