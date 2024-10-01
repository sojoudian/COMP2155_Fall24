import paramiko

# Create an SSH client
ssh_client = paramiko.SSHClient()

# Connect to the remote host (ensure no extra space in password)
ssh_client.connect(hostname='hostname', username='user', password='pass')