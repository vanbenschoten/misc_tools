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
	map_conversion(args)


def map_conversion(args):

  from cctbx import crystal
  #Read in hkl file and populate miller array
  name = args[0]
  name_adjusted = name[:-4]
  inf = open(name, "r")
  indices = flex.miller_index()
  i_obs = flex.double()
  sig_i = flex.double()
  count = 2
  for line in inf.readlines():
    
    assert len(line.split())==4
    line = line.strip().split()
    i_obs_ = float(line[3])#/10000 #10000 is a uniform scale factor meant to re-size all diffuse intensities (normally too large for scalepack)
    sig_i_ = math.sqrt(i_obs_)
    #if(abs(i_obs_)>1.e-6): # perhaps you don't want zeros
    if count%2 == 0:
      indices.append([int(line[0]),int(line[1]),int(line[2])])
      i_obs.append(i_obs_)
      sig_i.append(sig_i_)
    count += 1
  inf.close()
  print indices

  # get miller array object
  cs = crystal.symmetry(unit_cell=(float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]), float(args[6])), space_group=args[7])
  miller_set=miller.set(cs, indices, anomalous_flag=False)
  ma = miller.array(miller_set=miller_set, data=i_obs, sigmas=None)
  #ma.set_observation_type_xray_intensity()
  #ma_final = ma.customized_copy(anomalous_flag=False)
  #ma_final = ma_anom.customized_copy(sigmas=None)
  #help(ma.as_mtz_dataset)
  mtz_dataset = ma.as_mtz_dataset(column_root_label="I")
  mtz_dataset.mtz_object().write("data_rgb.mtz")

  print 'hello!'
  #scalepack.merge.write(file_name= name_adjusted + '.sca', miller_array=ma_final)


if __name__ == '__main__':
	import sys
	run(sys.argv[1:])