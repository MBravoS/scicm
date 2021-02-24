########################################
# Set up the colour maps
########################################
import os
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

cmaps=['BkG','blue2cyan','blue','CkO','cyan','green2yellow','GwP','magenta','orange','purple2magenta',
       'quartile','red2orange','stone','yellow','BkR','blue2purple','BwR','cyan2green','GkP','green',
       'magenta2red','orange2yellow','PkO','purple','red','YkM']

cmap_dict={}
data_path=os.path.join(os.path.split(__file__)[0],'cm_data')
for cmap in cmaps:
    cmap_path=os.path.join(data_path,f'{cmap}.txt')
    cmap_data=np.loadtxt(cmap_path)
    cmap_dict[cmap]=LinearSegmentedColormap.from_list(cmap,cmap_data,N=cmap_data.shape[0])
    cmap_dict[f'{cmap}_r']=LinearSegmentedColormap.from_list(f'{cmap}_r',cmap_data[::-1,:],N=cmap_data.shape[0])

for cmap in cmap_dict.keys():
    cm.register_cmap(f'scicm.{cmap}',cmap_dict[cmap])

locals().update(cmap_dict)
