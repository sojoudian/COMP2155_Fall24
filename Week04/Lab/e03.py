import  subprocess
class Pinger:
    def __init__(self, ip_address="8.8.4.4"):
        self.ip_address = ip_address

    def ping(self):
        try:
            # Execute the ping command windows -n, Linux and macOS -c
            output = subprocess.check_output(["ping", "-c", "1", self.ip_address]).decode("utf-8")
            print(f"Ping result for {self.ip_address}")
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Ping failed for {self.ip_address}. Error: {e}")
        except Exception as e:
            print(f"An error occurred for {self.ip_address}. Error: {e}")

if __name__ == "__main__":
    pinger = Pinger()
    pinger.ping()