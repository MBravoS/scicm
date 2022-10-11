'''This module reads the colour map data from the cm folder, set ups the corresponding colour
maps and their corresponding reverse order maps, and registers them with matplotlib'''

from os import path
import pkg_resources
from glob import glob
from numpy import loadtxt
from matplotlib.colors import LinearSegmentedColormap as LSC

# Check for matplotlib version
mpl_ver=pkg_resources.get_distribution('matplotlib').version
mpl_ver=[int(s) for s in mpl_ver.split('.')]
mpl_ver=mpl_ver[0]*10+mpl_ver[1]
if mpl_ver>=35:
    from matplotlib import colormaps as cm
else:
    from matplotlib import cm

# Grab the path to the colour map data
data_path=path.join(path.split(__file__)[0],'cm_data')

# List of all colour maps in scicm
cmaps=[c.split('/')[-1].split('.')[0] for c in sorted(glob(f'{data_path}/*.txt'))]

# List of diverging colour maps, this separate list is used
# to generate the mirror name copies (i.e. RwB)
diverging=[c for c in cmaps if len(c)==3 and c[1]=='k']
diverging+=[c for c in cmaps if len(c)==3 and c[1]=='w']
diverging={c:c[::-1] for c in diverging}

# Reading in the colour map data and setting up the cm objects
cmap_dict={}
for cmap in cmaps:
    cmap_path=path.join(data_path,f'{cmap}.txt')
    cmap_data=loadtxt(cmap_path)
    cmap_dict[cmap]=LSC.from_list(f'scicm.{cmap}',cmap_data,N=cmap_data.shape[0])
    cmap_dict[f'{cmap}_r']=LSC.from_list(f'scicm.{cmap}_r',cmap_data[::-1,:],
                                         N=cmap_data.shape[0])
    if cmap in diverging.keys():
        cmap_name=diverging[cmap]
        cmap_dict[cmap_name]=LSC.from_list(f'scicm.{cmap_name}',cmap_data[::-1,:],
                                           N=cmap_data.shape[0])
        cmap_dict[f'{cmap_name}_r']=LSC.from_list(f'scicm.{cmap_name}_r',cmap_data,
                                                  N=cmap_data.shape[0])

# Registering the maps with matplotlib
if mpl_ver>=35:
    for cmap in cmap_dict:
        cm.register(cmap_dict[cmap])
else:
    for cmap in cmap_dict:
        cm.register_cmap(f'scicm.{cmap}',cmap_dict[cmap])

locals().update(cmap_dict)
