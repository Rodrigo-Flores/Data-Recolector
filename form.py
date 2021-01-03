from colorama import init
from colorama import Fore, Back, Style
import datetime
import csv

def form():
    try:
        while True:
            fist_name = input('Enter the First Name: ')
            last_name = input('Enter the Last Name: ')
            city_country = input('Enter City, Country: ')
            age = input('Enter the Age: ')

            current_date = str(datetime.datetime.today()).split()[0]

            with open('Data/form.csv', 'w', newline='') as file:
                fieldnames = ['Time', 'First Name', 'Last Name', 'City/Country', 'Age']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
               	writer.writerow({'Time': current_date, 'First Name': fist_name,
                'Last Name': last_name, 'City/Country': city_country, 'Age': age})

            print(Fore.GREEN + '\nThe data has been saved successfully!\n')
            print(Style.RESET_ALL)

    except KeyboardInterrupt:
        print('\nStoping the program...')

form()
