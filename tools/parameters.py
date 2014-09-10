import sys

if sys.platform == 'win32':
	csv_path = 'C:\Users\dasmesser\Documents\ITC\9noSemestre\Sistemas Operativos 2\proyecto\data\mi_registro_matrimonios.csv'
	output_path = 'C:\Users\dasmesser\Documents\ITC\9noSemestre\Sistemas Operativos 2\proyecto\output'
else:
	csv_path = '/home/A01211143/projecto/DjangoProject/data/mi_registro_matrimonios.csv'
	output_path = '/home/A01211143/projecto/DjangoProject/output'