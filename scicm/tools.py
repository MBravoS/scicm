'''This module contain auxiliary functions for easy manipulation of the scicm colour maps.'''


import numpy as _np
import matplotlib as _mpl
from matplotlib.colors import LinearSegmentedColormap as _LSC

### TODO: Need to figure out with merge is not producing a perfect match to the input colour maps

def crop(cmapin, vmin=0.0, vmax=1.0, name_newcmap=None):
    '''Takes a colour map and from a subset of colours generates a new map.
    
    From the input colour map, selects all colours that lie between the given vmin/vmax values and
    returns a new colour map that includes only the selected subset of colours. Can also register
    the new colour map with matplotlib if a name for the new colour map is given.
    
    Parameters
    ----------
    cmapin : str or object
        A string with the name of the colour map or the colour map object.
    vmin/vmax : float, optional
        If given, the normalised low/high limits to select from the source colour map. Values must
        be in the [0, 1] range and vmin<vmax. Defaults to vmin = 0 and vmax = 1 (i.e., returns the
        input colourmap).
    name_newcmap : str, optional
        If given, defines the name to register with matplotlib.
    
    Returns
    -------
    newcmap
        Colourmap object with the new colour map.
    
    Example
    -------
    Generate a new colour map that only spans the brighter half of matplolib's viridis:
    
    >>> from matplotlib.cm import viridis
    >>> from scicm.tools import crop
    
    >>> short_viridis = crop(viridis, vmin=0.5)
    
        Check that the first colour in the new colour map corresponds to the mid-point of viridis.
    >>> viridis(128)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> short_viridis(0)
    (0.127568, 0.566949, 0.550556, 1.0)
    
        Check that the last colour in the new colour map corresponds to the last colour of viridis.
    >>> viridis(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    >>> short_viridis(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    
    '''
    
    if vmin > vmax:
        raise ValueError('The value of vmin must be lower than vmax')
    if vmin < 0.0 or vmax > 1.0:
        raise ValueError('The values of vmin/vmax must be in the closed range [0, 1]')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    if isinstance(cmapin, str):
        cmapin = _mpl.colormaps[cmapin]
    try:
        test = cmapin(0.5)
    except TypeError:
        raise TypeError('cmapin does not behave like a colour map')
    try:
        if len(test)!=4:
            raise TypeError('cmapin does not behave like a colour map')
    except TypeError:
        raise TypeError('cmapin does not behave like a colour map')
    
    cmap_data = cmapin(_np.linspace(vmin, vmax, 256))
    
    if name_newcmap:
        newcmap = _LSC.from_list(name_newcmap, cmap_data, N=cmap_data.shape[0])
        _mpl.colormaps.register(name_newcmap, newcmap)
    else:
        newcmap = _LSC.from_list('newcmap', cmap_data, N=cmap_data.shape[0])
    
    return newcmap


def stitch(cmapinlist, vlims, tpoints, name_newcmap=None):
    '''Takes a list of colour maps and generates a new one that includes stretched/compressed
    segments from each.
    
    From the input list of colour maps, selects all colours that lie between the given transition
    points and returns a new colour map that includes only the selected subsets of colours. The
    colour subsets drawn from each colour map on the list are defined by the list of value limits.
    Can also register the new colour map with matplotlib if a name for the new colour map is given.
    
    
    Parameters
    ----------
    cmapinlist : list
        Each element must be either a string with the name of each colour map or the
        colour map objects.
    vlims : numpy.ndarray
        A (N, 2) array that contains the vmin and vmax values used for cropping the colour maps
        and setting the ranges that each crop will take on the new colour map. vlims[:, 0] are
        the low limits (vmin) and vlims[:, 1] the high limits (vmax).
    tpoints : list, tuple or numpy.ndarray
        Contains the transition points where the new colour map will transition from one input
        colour map to the next.
    name_newcmap : str, optional
        If given, defines the name to register with matplotlib.
    
    Returns
    -------
    newcmap
        Colourmap object with the new colour map.
    
    Example
    -------
    Generate a new colour map where the first half are viridis colours and the second half are magma
    colours:
    
    >>> from matplotlib.cm import viridis, magma
    >>> from scicm.tools import stitch
    
    >>> viridis_magma = stitch([viridis,magma], tpoints=[0.5])
    
        Check that the first colour in the new colour map corresponds to the first of viridis.
    >>> viridis(0)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(0)
    (0.127568, 0.566949, 0.550556, 1.0)
    
        Check that the the new colour map switched from viridis to magma at the mid-point.
    >>> viridis(127)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(127)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> magma(128)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(128)
    (0.127568, 0.566949, 0.550556, 1.0)
    
        Check that the last colour in the new colour map corresponds to the last colour of magma.
    >>> magma(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    >>> viridis_magma(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    
    '''
    
    if not isinstance(cmapinlist, list):
        raise TypeError('cmapinlist must be a list')
    if len(cmapinlist)<2:
        raise ValueError('cmapinlist must contain at least two colour maps')
    if not isinstance(vlims, _np.ndarray):
        vlims = _np.array(vlims)
    if vlims.shape!=(len(cmapinlist),2):
        raise ValueError('vlims shape does not match expectation of (N,2)')
    for vcheck in vlims:
        if vcheck[0] > vcheck[1]:
            raise ValueError('The value of vmin must be lower than vmax')
    if _np.sum((vlims < 0.0) | (vlims > 1.0)) > 0:
        raise ValueError('The values in vlims must be in the closed range [0, 1]')
    if not isinstance(tpoints, _np.ndarray):
        tpoints = _np.array(tpoints)
    if _np.sum(_np.diff(tpoints) < 0) > 0:
        raise ValueError('tpoints must be monotonically increasing in value')
    if _np.sum((tpoints <= 0.0) | (tpoints >= 1.0)):
        raise ValueError('The values of tpoints must be in the open range (0, 1)')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    cmapinlist = [_mpl.colormaps[cmapin] if isinstance(cmapin, str) else cmapin for cmapin in cmapinlist]
    try:
        test = [c(0.5) for c in cmapinlist]
    except TypeError:
        raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    try:
        if _np.sum([len(t)==4 for t in test])<len(test):
            raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    except TypeError:
        raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    
    tpoints = _np.array([0]+list(tpoints)+[1])
    nstep = _np.empty(len(cmapinlist))
    test_range = _np.linspace(0, 1, 256)
    for i in range(len(cmapinlist)):
        nstep[i] = _np.sum((test_range > tpoints[i]) & (test_range < tpoints[i+1])) + 1
    nstep = _np.where(nstep < 1, 1, nstep)
    if _np.sum(nstep) != 256:
        nstep[-1] += 256-_np.sum(nstep)
    nstep = nstep.astype('int')
    
    cmaplist_data = [cmapinlist[i](_np.linspace(vlims[i, 0], vlims[i, 1], nstep[i]))
                     for i in range(len(cmapinlist))]
    cmap_data = _np.concatenate(cmaplist_data, axis=0)
    
    if name_newcmap:
        newcmap = _LSC.from_list(name_newcmap, cmap_data, N=cmap_data.shape[0])
        _mpl.colormaps.register(name_newcmap, newcmap)
    else:
        newcmap = _LSC.from_list('newcmap', cmap_data, N=cmap_data.shape[0])
    
    return newcmap


def merge(cmapinlist, tpoints, name_newcmap=None):
    '''Takes a list of colour maps and generates a new one that includes segments from each.
    
    From the input list of colour maps, selects all colours that lie between the given transition
    points and returns a new colour map that includes only the selected subsets of colours. The
    colour subset drawn from the first colour map on the list goes from the first colour up to the
    first transition point, and the subset drawn from the last colour map goes from the last
    transition point up to the last colour in the map. Can also register the new colour map with
    matplotlib if a name for the new colour map is given.
    
    Parameters
    ----------
    cmapinlist : list
        Each element must be either a string with the name of each colour map or the
        colour map objects.
    tpoints : list, tuple or numpy.ndarray
        Contains the transition points where the new colour map will transition from one input
        colour map to the next.
    name_newcmap : str, optional
        If given, defines the name to register with matplotlib.
    
    Returns
    -------
    newcmap
        Colourmap object with the new colour map.
    
    Example
    -------
    Generate a new colour map where the first half are viridis colours and the second half are magma
    colours:
    
    >>> from matplotlib.cm import viridis, magma
    >>> from scicm.tools import merge
    
    >>> viridis_magma = merge([viridis,magma], tpoints=[0.5])
    
        Check that the first colour in the new colour map corresponds to the first of viridis.
    >>> viridis(0)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(0)
    (0.127568, 0.566949, 0.550556, 1.0)
    
        Check that the the new colour map switched from viridis to magma at the mid-point.
    >>> viridis(127)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(127)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> magma(128)
    (0.127568, 0.566949, 0.550556, 1.0)
    >>> viridis_magma(128)
    (0.127568, 0.566949, 0.550556, 1.0)
    
        Check that the last colour in the new colour map corresponds to the last colour of magma.
    >>> magma(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    >>> viridis_magma(255)
    (0.993248, 0.906157, 0.143936, 1.0)
    
    '''
    
    if not isinstance(cmapinlist, list):
        raise TypeError('cmapinlist must be a list')
    if not isinstance(tpoints, _np.ndarray):
        tpoints = _np.array(tpoints)
    if _np.sum(_np.diff(tpoints) < 0) > 1:
        raise ValueError('tpoints must be monotonically increasing in value')
    if _np.sum((tpoints <= 0.0) | (tpoints >= 1.0)):
        raise ValueError('The values of tpoints must be in the open range (0, 1)')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    vlims = _np.array([0]+list(tpoints)+[1])
    vlims = _np.array([[vlims[i], vlims[i+1]] for i in range(len(cmapinlist))])
    newcmap = stitch(cmapinlist, vlims, tpoints, name_newcmap)
    
    for vcheck in vlims:
        if vcheck[0] > vcheck[1]:
            raise ValueError('The value of vmin must be lower than vmax')
    
    return newcmap
