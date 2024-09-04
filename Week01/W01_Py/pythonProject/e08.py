ciscoDevices = ["2960", "4221", "3750", "nx9000"]
print("The original list of Cisco Devices: ", ciscoDevices)
ciscoDevices.append("1900")
print("The new list of Cisco Devices with Faiz suggestion: ", ciscoDevices)
ciscoDevices.remove("1900")
print("After removing the 1900", ciscoDevices)

router = ciscoDevices[1]
print("The router details: ", router)

numberOfDevices = len(ciscoDevices)
print("Number of Cisco Devices: ", numberOfDevices)

print("The following is the list of Cisco Devices: ")
for device in ciscoDevices:
    print(device)