def read_file(file, arr=False):
	f = open(file, "r")
	lines = f.read()

	if arr:
		lines = lines.split('\n')

	f.close()

	return lines