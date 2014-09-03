def run(args):

	data = dictionary_conversion(args[0],args[1])

	cell_a = float(args[2])
	cell_b = float(args[3])
	cell_c = float(args[4])

	pearson = true_pcc(data)

	#split_map(data)

	#difference_map(data)
	#print 'hello!'

	print pearson

def single_conversion(map_1):

	f_1 = open(map_1,'r')

	lines_1 = f_1.readlines()

	lattice = dict()

	for line in lines_1:
		signal = line.split()
		if len(signal) == 4:
			h = signal[0]
			k = signal[1]
			l = signal[2]
			intensity = signal[3]

			if h not in lattice:
				lattice[h] = dict()

    		if k not in lattice[h]:
        		lattice[h][k] = dict()

    		if l not in lattice[h][k]:
        		lattice[h][k][l] = dict()

        	lattice[h][k][l]["Signal_1"] = intensity
	return lattice

def dictionary_conversion(map_1, map_2):

	f_1 = open(map_1,'r')
	f_2 = open(map_2,'r')

	lines_1 = f_1.readlines()
	lines_2 = f_2.readlines()

	lattice = dict()

	for line in lines_1:
		signal = line.split()
		if len(signal) == 4:
			h = signal[0]
			k = signal[1]
			l = signal[2]
			intensity = signal[3]

			if h not in lattice:
				lattice[h] = dict()

    		if k not in lattice[h]:
        		lattice[h][k] = dict()

    		if l not in lattice[h][k]:
        		lattice[h][k][l] = dict()

        	lattice[h][k][l]["Signal_1"] = intensity

	for line in lines_2:
		signal_2 = line.split()
		if len(signal_2) == 4:
			h = signal_2[0]
			k = signal_2[1]
			l = signal_2[2]
			intensity = signal_2[3]

			if h not in lattice:
				lattice[h] = dict()

    		if k not in lattice[h]:
        		lattice[h][k] = dict()

    		if l not in lattice[h][k]:
        		lattice[h][k][l] = dict()

        	lattice[h][k][l]["Signal_2"] = intensity

	return lattice



def r_factor(data):

	denominator = 0

	numerator = 0

	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:
						numerator += abs(math.sqrt(float(data[key_h][key_k][key_l]["Signal_1"]))-math.sqrt(float(data[key_h][key_k][key_l]["Signal_2"])))
						denominator += float(data[key_h][key_k][key_l]["Signal_1"])

	print numerator
	print denominator

	r_factor = numerator/denominator

	return r_factor

def difference_map(data):
	fout = open('difference.hkl', 'w')
	fout_p = open('positive.hkl', 'w')
	fout_n = open('negative.hkl', 'w')
	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:
						difference = float(data[key_h][key_k][key_l]["Signal_1"])-float(data[key_h][key_k][key_l]["Signal_2"])

						fout.write(key_h + ' ' + key_k + ' ' + key_l + ' ' + str(difference) + '\n')

						if difference >= 0.0:
							fout_p.write(key_h + ' ' + key_k + ' ' + key_l + ' ' + str(difference) + '\n')
						else:
							fout_n.write(key_h + ' ' + key_k + ' ' + key_l + ' ' + str(abs(difference)) + '\n')

def i1_i2_plot(data, cell_a, cell_b, cell_c):

    import math
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.zeros(1)
    y = np.zeros(1)
    c_list = np.zeros(1)

	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:

						s_1 = float("Signal_1")
						s_2 = float("Signal_2")

						resolution = math.sqrt((cell_a/int(key_h))*(cell_a/int(key_h))+(cell_b/int(key_k))*(cell_b/int(key_k))+(cell_c/int(key_l))*(cell_c/int(key_l)))

						if resolution < 2.5:
							color = 'r'

						elif resolution > 2.5 and resolution < 3.0:
							color = 'g'

						elif resolution > 3.0 and resolution < 3.5:
							color = 'b'

						elif resolution > 3.5 and resolution < 4.0:
							color = 'y'

						else:
							color = 'c'

						np.append(x,s_1)
						np.append(y,s_2)
						np.append(c_list,color)

						np.delete(x,0)
						np.delete(y,0)
						np.delete(z,0)


	plt.scatter(x,y,c=c_list)









def split_map(data):
	fout_p = open('positive_one.hkl', 'w')
	fout_n = open('negative_one.hkl', 'w')
	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					difference = float(data[key_h][key_k][key_l]["Signal_1"])

					if difference >= 0.0:
						fout_p.write(key_h + ' ' + key_k + ' ' + key_l + ' ' + str(difference) + '\n')
					else:
						fout_n.write(key_h + ' ' + key_k + ' ' + key_l + ' ' + str(abs(difference)) + '\n')

def pcc(data):

	import math

	denominator_1 = 0

	denominator_2 = 0

	numerator = 0

	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:
						numerator += float(data[key_h][key_k][key_l]["Signal_1"])*float(data[key_h][key_k][key_l]["Signal_2"])
						denominator_1 += float(data[key_h][key_k][key_l]["Signal_1"])*float(data[key_h][key_k][key_l]["Signal_1"])
						denominator_2 += float(data[key_h][key_k][key_l]["Signal_2"])*float(data[key_h][key_k][key_l]["Signal_2"])

	pearson = numerator/math.sqrt(denominator_1*denominator_2)

	return pearson

def true_pcc(data):

	import math

	denominator_1 = 0

	denominator_2 = 0

	numerator = 0

	average_1 = 0

	average_2 = 0

	count = 0

	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:
						average_1 += float(data[key_h][key_k][key_l]["Signal_1"])
						average_2 += float(data[key_h][key_k][key_l]["Signal_2"])
						count += 1

	avg_1 = average_1/count
	avg_2 = average_2/count


	for key_h in data:
		for key_k in data[key_h]:
			for key_l in data[key_h][key_k]:
				if "Signal_1" in data[key_h][key_k][key_l]:
					if "Signal_2" in data[key_h][key_k][key_l]:
						numerator += (float(data[key_h][key_k][key_l]["Signal_1"])-avg_1)*(float(data[key_h][key_k][key_l]["Signal_2"])-avg_2)
						denominator_1 += (float(data[key_h][key_k][key_l]["Signal_1"])-avg_1)*(float(data[key_h][key_k][key_l]["Signal_1"])-avg_1)
						denominator_2 += (float(data[key_h][key_k][key_l]["Signal_2"])-avg_2)*(float(data[key_h][key_k][key_l]["Signal_2"])-avg_2)

	pearson = numerator/math.sqrt(denominator_1*denominator_2)

	return pearson

if __name__ == "__main__":
	import sys
	import math
	args = sys.argv[1:]
	run(args)