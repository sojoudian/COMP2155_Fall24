import csv
import datetime

from Week02.Lecture_02.e05 import filename


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

class CSVWriter:
    def __init__(self, data):
        self.data = data
    def save_to_csv(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = f"ip_addresses_{current_date}.csv"

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow("IP Address/Domain")
            for ip in self.data:
                writer.writerow(ip)


class IPAddressApp:

if __name__ == '__main__':
    app = IPAddressApp()
    app.run()






