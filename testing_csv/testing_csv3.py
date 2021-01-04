import datetime
import csv 

	#### OUT THE LOOP ####
	current_time = datetime.datetime.now()

with open('/testing_folder/loraFunction_output.csv', 'w', newline='') as file:
    fieldnames = ['Time', 'Data']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    #### IN THE LOOP ####
   	writer.writerow({'Time': current_time, 'Data': "MODULE OUTPUT"})  

 # En caso de que el modulo posea mas de una salida de datos, se puede aumentar el numero de "fieldnames" y luego especificar los datos dentro del diccionario.