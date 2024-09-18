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
        print(f"IP address and domains saved to {file_name}")

class IPAddressApp:
    def __init__(self):
        self.collector = IPAddressCollector()
    def run(self):
        self.collector.get_user_input()
        if self.collector.ip_addresses:
            csv_writer = CSVWriter(self.collector.ip_addresses)
            csv_writer.save_to_csv()
        else:
            print("No data entered!")

if __name__ == '__main__':
    app = IPAddressApp()
    app.run()






