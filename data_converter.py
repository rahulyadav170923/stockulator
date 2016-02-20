import csv
import json

csvfile = open('data/andhra-bank.csv', 'r')
jsonfile = open('data/andhra-bank.json', 'w')

fieldnames = ("Date","Open","High","Low","Close","Volume","Adj Close")
reader = csv.DictReader( csvfile, fieldnames)
output = []

for each in reader:
    row = {}
    for field in fieldnames:
        row[field] = each[field]
    output.append(row)
output.pop(0)
json.dump(output, jsonfile, indent=2, sort_keys=True)
