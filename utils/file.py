def clean_file(file):
	file = open(file,"r+")

	file.truncate(0)
	
	file.close()

def read_file(file, array=False):
	f = open(file, "r")
	lines = f.read()

	if array:
		lines = lines.split('\n')

	f.close()

	return lines

def write_file(file, message):
	f = open(file, "a")
	f.write(f"{message}\n")

	f.close()

	return "Success"