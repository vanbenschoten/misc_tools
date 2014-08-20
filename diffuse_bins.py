from cctbx import crystal
from cctbx import miller
from iotbx import scalepack
from cctbx.array_family import flex
import sys
import iotbx
from iotbx import pdb
import math
from cctbx.array_family import flex
from cctbx import xray
from iotbx.scalepack import merge
from libtbx.utils import Sorry


def run(args):

  make_miller(args[1])

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

  #Input symmetry object

  #NOTE: get symmetry object!!!
  cs = cs = crystal.symmetry(unit_cell=(x,y,z,90,90,90), space_group='P 21 21 21')
  ma = miller.array(miller_set=miller.set(cs, indices), data=i_obs, sigmas=sig_i)
  ma.set_observation_type_xray_intensity()
  ma_anom = ma.customized_copy(anomalous_flag=false)

  return ma_anom


def get_bin_data(array):

  d_star_power = 1.618034

  n_bins=50
  binner= array.setup_binner(n_bins=n_bins)
  I = array.intensities()
  selections = [binner.selection(i) for i in binner.range_used()]
  means = [I.select(sel).mean() for sel in selections]
  log_means = math.log(m) for m in means]
  centers = binner.bin_centers(d_star_power)
  d_centers = centers**(-1/d_star_power)

  plot = pygmyplot.xy_plot(centers, log_means, master=tk)
  plot.axes.set_xticks(centers[::3])
  plot.axes.set_xticklabels(x_labels[::3])
  plot.axes.set_xlabel('Resolution ($\\AA$)')
  plot.axes.set_ylabel('log intensity')
  plot.canvas.draw()

  TK.Button(tk, text="Quit", command=tk.destroy).pack()
  tk.mainloop()


if __name__ == '__main__':
	import sys

	run(sys.argv[1:])

