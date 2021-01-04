import datetime
import csv 

'''
	#### OUT THE LOOP ####
	current_time = datetime.datetime.now()

with open('Data/loraFunction_output.csv', 'w', newline='') as file:
    fieldnames = ['Time', 'Data']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    #### IN THE LOOP ####
   	writer.writerow({'Time': current_time, 'Data': "MODULE OUTPUT"})  

 # En caso de que el modulo posea mas de una salida de datos, se puede aumentar el numero de "fieldnames" y luego especificar los datos dentro del diccionario.
'''
class CanSat_csv:
	def c_time():
		current_time = datetime.datetime.now()
		return current_time

	def make_csv(current_time, module_output):
		with open('Data/loraFunction_output.csv', 'w', newline='') as file:
			fieldnames = ['Time', 'Data']
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			writer.writeheader()

			writer.writerow({'Time': current_time, 'Data': module_output})