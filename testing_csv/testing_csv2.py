import csv 

with open('testing_folder/example_csv.csv', 'w', newline='') as file:
    fieldnames = ['Time', 'Data']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(0, 100):
    	writer.writerow({'Time': i, 'Data': (i + 5)})    	

