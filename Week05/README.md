
# SSH (Secure Shell)

SSH is a protocol used to securely connect to remote machines, typically over an encrypted channel. It is widely supported across Unix-like systems (Linux, BSD, macOS), Windows, and network devices (Cisco, Juniper, etc.).

## Supported Systems

- **Unix-like OS**: FreeBSD, OpenBSD, macOS, and all BSD family systems.
- **Linux Distributions**: RedHat, CentOS, Ubuntu, Debian, Kali, Mint, and more.
- **Windows OS**: Native OpenSSH client in PowerShell (Windows 10 and later) or third-party tools like PuTTY.

## SSH Use Cases

- Connect to **SSH servers**: Routers, Switches, Firewalls, Linux Servers, Windows Servers, and BSD Servers.
- Network devices: SSH is used for securely configuring routers and switches (Cisco, Juniper).

## Common SSH Clients

- **Command Line (Built-in)**: Available in most Unix-like systems and Windows PowerShell.
- **GUI Tools**:
  - **PuTTY** (Windows, Linux)
  - **SecureCRT**
  - **MobaXterm** (Windows)
  - **Termius** (Cross-platform)

## How to Use the SSH Command

### Basic SSH connection:

```bash
ssh username@host
```

Example:

```bash
ssh user@192.168.1.100
```

### Specifying a Port (if the SSH server is running on a non-standard port):

```bash
ssh -p 2222 user@192.168.1.100
```

### Using Public Key Authentication:

To authenticate using a key pair:

```bash
ssh -i /path/to/private_key user@192.168.1.100
```

#### Key Generation:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### Logging in with Password Authentication:

Simply enter the password when prompted:

```bash
ssh user@host
```

## Connecting to Cisco Devices

Cisco routers, switches, and firewalls often use SSH for secure remote access:

```bash
ssh admin@cisco_device_ip
```

You may also use public key authentication or password-based authentication on Cisco devices, depending on the security policies.

## Public Key Authentication Setup

### Generate a key pair:

```bash
ssh-keygen
```

### Copy your public key to the remote server:

```bash
ssh-copy-id user@remote_host
```

Or manually copy the contents of your `~/.ssh/id_rsa.pub` file to the remote server's `~/.ssh/authorized_keys` file.

### Disable password authentication for added security (optional):

On the remote machine, edit `/etc/ssh/sshd_config`:

```bash
PasswordAuthentication no
```

Then restart the SSH service:

```bash
sudo systemctl restart ssh
```

## SSH Configurations for Convenience

Create a `~/.ssh/config` file to simplify SSH commands:

```bash
Host myserver
   HostName 192.168.1.100
   User username
   IdentityFile ~/.ssh/id_rsa
   Port 22
```

Now you can simply run:

```bash
ssh myserver
```

## Automation Tools

SSH is the foundation for automating tasks across different machines using tools such as:

- Terraform
- Ansible
- Chef
- Puppet

These tools allow you to provision, manage, and automate server setups and configurations.

For network devices, SSH can be automated using Python libraries like Paramiko, which is especially useful for interacting with Cisco and Linux systems.

```python
import paramiko

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hostname', username='user', password='pass')

stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read().decode())
client.close()
```

## Setting Up a Virtual Environment for Python Automation

### Navigate to your project directory:

```bash
cd week5
```

### Create a virtual environment:

```bash
python3 -m venv env
```

### Activate the virtual environment:

- On Linux/macOS:

```bash
source env/bin/activate
```

- On Windows:

```bash
.\env\Scriptsctivate
```

### To deactivate the virtual environment:

```bash
deactivate
```

This guide covers the essentials for connecting to Linux machines, Cisco devices, using SSH for public key and password authentication, and automation tools for SSH-based interactions.
