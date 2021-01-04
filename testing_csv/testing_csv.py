import time, datetime
from time import *
import csv

current_time = datetime.datetime.now()

with open('example_csv.csv', 'w', newline='') as file:
    fieldnames = ['Time', 'Data']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Time': current_time, 'Data': 'Data output'})