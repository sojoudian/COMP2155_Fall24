
# Cisco IOS Overview

## Cisco Three-Layer Hierarchical Model

The Cisco three-layer hierarchical model is a fundamental architecture for designing networks. It consists of the following layers:

1. **Access Layer**: Incorporates Layer 2 switches and access points that provide connectivity between workstations and servers.
2. **Distribution Layer**: Serves as the communication point between the access layer and the core layer. It provides routing, filtering, WAN access, and determines how packets access the core.
3. **Core Layer**: Also referred to as the network backbone. It provides interconnectivity between distribution layer devices and typically consists of high-speed devices like high-end routers and switches with redundant links.

## Cisco IOS Overview

### Accessing the IOS

There are three primary methods to access the IOS for configuration:

1. **Console Access**: Used for configuring newly acquired devices that don't have an IP address configured. A rollover cable is used to connect a computer to the console port of the device.
2. **Telnet Access**: Allows remote access, but less secure compared to SSH.
3. **SSH Access**: Similar to Telnet but adds encryption using public-key cryptography for secure remote configuration.

### Router Modes

Cisco routers have different modes for various levels of configuration:

- **User Mode**: Limited access for monitoring and basic tasks.
- **Privileged Mode**: Offers access to all commands, including those for configuring the router.
- **Global Configuration Mode**: Allows the user to apply configurations that affect the system as a whole.

### CLI Command Modes

Cisco IOS uses different command modes for different configuration tasks:

- **Global Configuration Mode**: Used to apply configurations to the entire router. Commands like `configure terminal` (or `config t`) are used to enter this mode.
- **Specific Configuration Modes**: Entered depending on the type of configuration required (e.g., interface configuration).

### Configuring a Router's Name

To set a unique hostname for a router, use the following commands in global configuration mode:

```bash
Router(config)#hostname Tokyo
```

### Configuring a Console Password

To restrict access to a router via the console, set a password with the following commands:

```bash
Router(config)#line console 0
Router(config-line)#password <password>
Router(config-line)#login
```

### No Shutdown Command

By default, interfaces on Cisco routers are turned off. To enable an interface, use the `no shutdown` command:

```bash
Router(config)#interface <interface>
Router(config-if)#no shutdown
```

### Configuring Interfaces

Each interface requires an IP address and subnet mask. Serial interfaces also need a clock rate at the DCE (Data Communications Equipment) end.

### Show Commands

- `show version`: Displays important device information such as software version, uptime, memory, and interfaces.
- `show running-configuration`: Displays the current configuration stored in RAM.
- `show startup-configuration`: Displays the configuration stored in NVRAM.
- `show ip int brief`: Displays interface information, including IP addresses and operational status.

### Pipe Character in IOS

The pipe character (`|`) can be used to filter the output of `show` commands. For example:

```bash
show running-configuration | begin interface
```

This filters the output to start displaying from the first occurrence of the word "interface."

---
