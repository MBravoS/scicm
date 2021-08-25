'''This module reads the colour map data from the cm folder, set ups the corresponding colour
maps and their corresponding reverse order maps, and registers them with matplotlib '''

import os
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap as LSC

# List of all colour maps in scicm
cmaps=['B2P','B2T','BkG','BkR','Blue','BwG','BwR','Cyan',
       'Day','Edges','G2Y','Garnet','GkP','Green','GwP',
       'M2R','Magenta','Night','O2Y','Orange','P2M','PkO',
       'Purple','Quartile','R2O','Red','Ripe','SoftBlue',
       'SoftGreen','SoftMagenta','SoftOrange','SoftPurple',
       'SoftRed','SoftTeal','SoftYellow','Stone','T2G',
       'Teal','TkO','Tropical','Yellow','YkB','YkM']

# List of diverging colour maps, this separate list is used
# to generate the mirror name copies (i.e. RwB)

diverging={'BkG':'GkB','BkR':'RkB','BwG':'GwB','BwR':'RwB','GkP':'PkG',
           'GwP':'PwG','PkO':'OkP','TkO':'OkT','YkM':'MkY','YkB':'BkY'}

# Reading in the colour map data and setting up the cm objects
cmap_dict={}
data_path=os.path.join(os.path.split(__file__)[0],'cm_data')
for cmap in cmaps:
    cmap_path=os.path.join(data_path,f'{cmap}.txt')
    cmap_data=np.loadtxt(cmap_path)
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
