import csv
from os import write

with open('writeData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Header
    writer.writerow(['Student Name', 'ID', 'GPA', 'SSN'])

    # Write data rows
    writer.writerow(['Maziar', '10223344', '2', '13456789'])
    writer.writerow(['Fendi', '10665577', '3', '13406789'])
    writer.writerow(['Alfi', '10887799', '4', '10456789'])