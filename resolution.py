def run(args):
	fin = open(args[0],'r')
	fout = open(args[1], 'w')

	cell_a = float(args[2])
	cell_b = float(args[3])
	cell_c = float(args[4])

	res = float(args[5])

	x_cut = int(cell_a/res)
	y_cut = int(cell_b/res)
	z_cut = int(cell_c/res)

	lines = fin.readlines()

	for line in lines:
		data = line.split()

		x = abs(int(data[0]))
		y = abs(int(data[1]))
		z = abs(int(data[2]))

		if x < x_cut:
			if y < y_cut:
				if z < z_cut:
					fout.write(line)

	fin.close()
	fout.close()


if __name__ == '__main__':
	import sys
	run(sys.argv[1:])