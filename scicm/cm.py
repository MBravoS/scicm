########################################
# Set up the colour maps
########################################
import os
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

cmaps=['B2C','B2P','BkG','BkR','Blue','BwG','BwR','C2G',
       'CkO','CwO','Cyan','Day','Edges','G2Y','Garnet','GkP','Green',
       'GwP','M2R','Magenta','Night','O2Y','Orange',
       'P2M','PkO','Purple','PwO','Quartile','R2O','Red',
       'Ripe','Stone','Tropical','Yellow','YkB','YkM']

diverging={'BkG':'GkB','BkR':'RkB','BwG':'GwB','BwR':'RwB','CkO':'OkC','CwO':'OwC',
           'GkP':'PkG','GwP':'PwG','PkO':'OkP','PwO':'OwP','YkM':'MkY','YkB':'BkY'}

cmap_dict={}
data_path=os.path.join(os.path.split(__file__)[0],'cm_data')
for cmap in cmaps:
    cmap_path=os.path.join(data_path,f'{cmap}.txt')
    cmap_data=np.loadtxt(cmap_path)
    cmap_dict[cmap]=LinearSegmentedColormap.from_list(cmap,cmap_data,N=cmap_data.shape[0])
    cmap_dict[f'{cmap}_r']=LinearSegmentedColormap.from_list(f'{cmap}_r',cmap_data[::-1,:],N=cmap_data.shape[0])
    if cmap in diverging.keys():
        cmap_dict[f'{diverging[cmap]}_r']=LinearSegmentedColormap.from_list(cmap,cmap_data,N=cmap_data.shape[0])
        cmap_dict[diverging[cmap]]=LinearSegmentedColormap.from_list(f'{cmap}_r',cmap_data[::-1,:],N=cmap_data.shape[0])

for cmap in cmap_dict.keys():
    cm.register_cmap(f'scicm.{cmap}',cmap_dict[cmap])

locals().update(cmap_dict)
