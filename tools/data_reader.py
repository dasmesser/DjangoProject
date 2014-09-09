from parameters import csv_path
import csv

#regresa {fecha, #matrimonios}
def read_file_fecha():
	try:
		fin = open(csv_path, 'rb')
		reader = csv.reader(fin)
		
		r = {}
		#previous_key
		for line in reader:
			if line[3] in r:
				r[line[3]] += int(line[1])
			else:
				try:
					r[line[3]] = int(line[1]) + int(r[previous_key])
				except:
					r[line[3]] = int(line[1])
				previous_key = line[3]
	except:
		r = None
		try:
			fin.close()
		except:
			pass
	
	return r

#regresa {delegacion, #matrimonios}
def read_file_delegaciones():
	try:
		fin = open(csv_path, 'rb')
		reader = csv.reader(fin)
		
		r = {}
		for line in reader:
			if line[0] in r:
				r[line[0]] += int(line[1])
			else:
				r[line[0]] = int(line[1])
	except:
		r = None
		try:
			fin.close()
		except:
			pass
			
	return r

#regresa {juzgados, #matrimonios}
def read_file_delegacion(delegacion):
	try:
		fin = open(csv_path, 'rb')
		reader = csv.reader(fin)
		
		r = {}
		found = False
		real_val = ''
		for line in reader:
			if found:
				if line[0] == real_val:
					if line[2] in r:
						r[line[2]] += int(line[1])
					else:
						r[line[2]] = int(line[1])
			else:
				if line[0].lower().startswith(delegacion.lower()):
					found = True
					real_val = line[0]
					if line[2] in r:
						r[line[2]] += int(line[1])
					else:
						r[line[2]] = int(line[1])
	except:
		r = None
		try:
			fin.close()
		except:
			pass
	
	return (r, real_val)
	
def read_file_juzgado(delegacion, juzgado):
	try:
		fin = open(csv_path, 'rb')
		reader = csv.reader(fin)
		
		r = {}
		found = False
		real_val = ''
		for line in reader:
			if found:
				if line[0] == real_val:
					if juzgado == line[2]:
						if line[3] in r:
							r[line[3]] += int(line[1])
						else:
							r[line[3]] = int(line[1])
			else:
				if line[0].lower().startswith(delegacion.lower()):
					found = True
					real_val = line[0]
					if juzgado == line[2]:	
						if line[3] in r:
							r[line[3]] += int(line[1])
						else:
							r[line[3]] = int(line[1])
	except:
		r = None
		try:
			fin.close()
		except:
			pass
	
	return (r, real_val)

def date_compare(x_tuple, y_tuple):
	(x, a) = x_tuple
	(y, b) = y_tuple

	mesx = int(x[:x.index('/')])
	mesy = int(y[:y.index('/')])
	
	diax = int(x[x.index('/') + 1 : x.index('/', x.index('/') + 1)])
	diay = int(y[y.index('/') + 1 : y.index('/', y.index('/') + 1)])
	
	anox = int(x[x.rfind('/') + 1:])
	anoy = int(y[y.rfind('/') + 1:])
	
	if anox == anoy:
		if mesx == mesy:
			return diax - diay
		else:
			return mesx - mesy
	else:
		return anox - anoy
	
	print mesx, diax, anox
	print mesy, diay, anoy
	
def juzgado_compare(x_tuple, y_tuple):
	(x,a) = x_tuple
	(y, b) = y_tuple
	
	return int(x) - int(y)
	
if __name__ == "__main__":
    pass