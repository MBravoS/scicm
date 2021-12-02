'''This module reads the colour map data from the cm folder, set ups the corresponding colour
maps and their corresponding reverse order maps, and registers them with matplotlib '''

from os import path
from glob import glob
from numpy import loadtxt
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap as LSC

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
    cmap_dict[cmap]=LSC.from_list(cmap,cmap_data,N=cmap_data.shape[0])
    cmap_dict[f'{cmap}_r']=LSC.from_list(f'{cmap}_r',cmap_data[::-1,:],
                                         N=cmap_data.shape[0])
    if cmap in diverging.keys():
        cmap_dict[f'{diverging[cmap]}_r']=LSC.from_list(cmap,cmap_data,
                                                        N=cmap_data.shape[0])
        cmap_dict[diverging[cmap]]=LSC.from_list(f'{cmap}_r',cmap_data[::-1,:],
                                                 N=cmap_data.shape[0])

# Registering the maps with matplotlib
for cmap in cmap_dict:
    cm.register_cmap(f'scicm.{cmap}',cmap_dict[cmap])

locals().update(cmap_dict)
