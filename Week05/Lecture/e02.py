import paramiko

# Create an SSH client
ssh_client = paramiko.SSHClient()

# Set policy to automatically add the host to known hosts
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote host (ensure no extra space in password)
ssh_client.connect(hostname='hostname', username='user', password='pass')