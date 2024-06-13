'''This module reads the colour map data from the cm folder, set ups the corresponding colour
maps and their corresponding reverse order maps, and registers them with matplotlib'''


from os import path as _path, sep as _sep
import pkg_resources as _pkg_resources
from glob import glob as _glob
from numpy import loadtxt as _loadtxt
from matplotlib.colors import LinearSegmentedColormap as _LSC


# Check for matplotlib version
_mpl_ver = _pkg_resources.get_distribution('matplotlib').version
_mpl_ver = [int(s) for s in _mpl_ver.split('.')]
_mpl_ver = _mpl_ver[0]*10+_mpl_ver[1]
if _mpl_ver >= 35:
    from matplotlib import colormaps as _cm
else:
    from matplotlib import cm as _cm


# Grab the path to the colour map data
_data_path = _path.join(_path.split(__file__)[0], 'cm_data')


# List of all colour maps in scicm
_cmaps = [c.split(_sep)[-1].split('.')[0] for c in sorted(_glob(f'{_data_path}{_sep}*.txt'))]


# List of diverging colour maps, this separate list is used
# to generate the mirror name copies (i.e. RwB)
_diverging = [c for c in _cmaps if len(c) == 3 and c[1] == 'k']
_diverging += [c for c in _cmaps if len(c) == 3 and c[1] == 'w']
_diverging = {c: c[::-1] for c in _diverging}


# Reading in the colour map data and setting up the cm objects
_cmap_dict = {}
for _cmap in _cmaps:
    _cmap_path = _path.join(_data_path, f'{_cmap}.txt')
    _cmap_data = _loadtxt(_cmap_path)
    _cmap_dict[_cmap] = _LSC.from_list(f'scicm.{_cmap}', _cmap_data, N=_cmap_data.shape[0])
    _cmap_dict[f'{_cmap}_r'] = _LSC.from_list(f'scicm.{_cmap}_r', _cmap_data[::-1, :],
                                           N=_cmap_data.shape[0])
    if _cmap in _diverging.keys():
        _cmap_name = _diverging[_cmap]
        _cmap_dict[_cmap_name] = _LSC.from_list(f'scicm.{_cmap_name}', _cmap_data[::-1, :],
                                             N=_cmap_data.shape[0])
        _cmap_dict[f'{_cmap_name}_r'] = _LSC.from_list(f'scicm.{_cmap_name}_r', _cmap_data,
                                                    N=_cmap_data.shape[0])


# Registering the maps with matplotlib
if _mpl_ver >= 35:
    for _cmap in _cmap_dict:
        _cm.register(_cmap_dict[_cmap])
else:
    for _cmap in _cmap_dict:
        _cm.register_cmap(f'scicm.{_cmap}', _cmap_dict[_cmap])

locals().update(_cmap_dict)
