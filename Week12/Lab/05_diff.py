######## this is not required for the EXAM, ASSIGNMENT, or LABs ####
import napalm
import difflib

# Initialize the NAPALM driver for Cisco IOS
driver = napalm.get_network_driver("ios")
device = driver(
    hostname="10.0.0.22",
    username="u1",
    password="cisco",
    optional_args={"port": 22, "secret": "cisco"}
)

# Open a connection to the device
device.open()

try:
    # Retrieve the running and startup configurations
    configs = device.get_config()
    running_config = configs.get("running", "")
    startup_config = configs.get("startup", "")

    # Split configurations into lines for comparison
    running_lines = running_config.splitlines()
    startup_lines = startup_config.splitlines()

    # Compare configurations and identify differences
    diff = difflib.unified_diff(
        startup_lines, running_lines,
        fromfile='Startup Configuration',
        tofile='Running Configuration',
        lineterm=''
    )

    # Display differences
    print("Differences between Startup and Running Configurations:")
    differences_found = False
    for line in diff:
        differences_found = True
        print(line)

    if not differences_found:
        print("No differences found. Running and startup configurations match.")

finally:
    # Close the connection to the device
    device.close()

