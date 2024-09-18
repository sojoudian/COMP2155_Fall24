import csv
import datetime

class IPAddressCollector:
    def __init__(self):
        self.ip_addresses = []
    def get_user_input(self):
        print("Please enter your IP addresses or domain names (type 'done' to finish):")
        while True:
            user_input = input("Enter an IP address or domain name: ")
            if user_input.lower() == "done":
                break
            self.ip_addresses.append(user_input)

class csvWriter:

class IPAddressApp:

if __name__ == '__main__':
    app = IPAddressApp()
    app.run()