# Week 09


## for Windows
```bash
python -m pip install --upgrade pip
```




## for Linux
```bash
pip install --upgrade pip
```

## Update Packages
```bash
pip install --upgrade paramiko
pip install --upgrade
```



Ultimate fixes for those Netmiko is not working:
```bash
deactivate  # First exit the virtual environment
rm -rf venv  # Delete the virtual environment
python3 -m venv venv  # Create a new virtual environment
source venv/bin/activate  # Activate it
pip install paramiko  # Install paramiko fresh
```
