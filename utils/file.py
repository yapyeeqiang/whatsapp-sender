def read_file(file, array=False):
	f = open(file, "r")
	lines = f.read()

	if array:
		lines = lines.split('\n')

	f.close()

	return lines
