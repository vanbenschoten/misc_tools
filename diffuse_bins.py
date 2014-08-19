import math

def run(args):


def make_miller(file):

  fin = open(file.'r')

  lines = fin.readlines()
  indices = flex.miller_index()
  i_obs = flex.double()
  sig_i = flex.double()


  for line in lines:
   	data = line.split()
   	h = int(data[0])
   	k = int(data[1])
   	l = int(data[2])
   	intensity = float(data[3])
    sig_i_ = math.sqrt(intensity)


   	indices.append([h,k,l])
   	i_obs.append(intensity)
    sig_i.append(sig_i_)

  fin.close()

  #NOTE: get symmetry object!!!
  cs = self.symmetry
  ma = miller.array(miller_set=miller.set(cs, indices), data=i_obs, sigmas=sig_i)

  return ma


def get_bin_data(array):
	


if __name__ == '__main__':
	import sys

	run(sys.argv[1:])

