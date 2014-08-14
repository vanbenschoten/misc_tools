# Read a file listing diffraction spot intensity data as a 3-d density map.
# File has 4 columns: h,k,l,intensity.
#
# Example Chimera command to use this hkl.py script
#
#       runscript hkl.py final_signal.hkl
#
def read_hkl_map(path):

    # Sum values for h,k,l grid points
    f = open(path, 'r')
    m = {}
    c = 0
    while True:
        line = f.readline()

        if c % 1000000 == 0 and c > 0:
            print c
        c += 1
        if line == '':
            break
        fields  = line.split()
        ijk = tuple(int(i) for i in fields[:3])
        v = float(fields[3])
        if ijk in m:
            m[ijk] += v
        else:
            m[ijk] = v
    f.close()

    # Find h,k,l bounds
    from numpy import array, int32, zeros, float32
    ijk = array(tuple(m.keys()), int32)
    ijk_min = ijk.min(axis = 0)
    ijk_max = ijk.max(axis = 0)
    print ijk_min, ijk_max

    # Create numpy array
    isz,jsz,ksz = ijk_max - ijk_min + 1
    a = zeros((ksz,jsz,isz), float32)
    imin, jmin, kmin = ijk_min
    for (i,j,k),v in m.items():
        a[k-kmin,j-jmin,i-imin] = v

    # Create volume model
    import VolumeData, VolumeViewer
    g = VolumeData.Array_Grid_Data(a, origin = tuple(ijk_min))
    v = VolumeViewer.volume_from_grid_data(g)
    from os.path import basename
    v.name = basename(path)

#path = 'diffuse_signal.txt'
#path = 'final_signal.hkl'
path ='refmac_pre_symmetry.hkl'
v = read_hkl_map(path)
