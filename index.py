import json
import csv

with open('fixed_database_1.json', 'r') as json_file:
    data = json.load(json_file)

with open('fixed_database_1.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(data[0].keys())
  
    for row in data:
        csv_writer.writerow(row.values())


with open('fixed_database_2.json', 'r') as json_file:
    data = json.load(json_file)

with open('fixed_database_2.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(data[0].keys())
    for row in data:
        csv_writer.writerow(row.values())
