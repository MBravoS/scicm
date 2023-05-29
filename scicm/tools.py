'''This module contain auxiliary functions for easy manipulation of the scicm colour maps.'''


import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap as LSC


def crop(cmapin, vmin=0.0, vmax=1.0, name_newcmap=None):
    '''Crop colour map between vmin/vmax values. Can also register the new colour map with matplotlib.
    
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
    '''
    
    if vmin > vmax:
        raise ValueError('The value of vmin must be lower than vmax')
    if vmin < 0.0 or vmax > 1.0:
        raise ValueError('The values of vmin/vmax must be in the closed range [0, 1]')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    if isinstance(cmapin, str):
        cmapin = cm.get_cmap(cmapin)
    try:
        test = cmapin(0.5)
    except TypeError:
        raise TypeError('cmapin does not behave like a colour map')
    try:
        if len(test)!=4:
            raise TypeError('cmapin does not behave like a colour map')
    except TypeError:
        raise TypeError('cmapin does not behave like a colour map')
    
    cmap_data = cmapin(np.linspace(vmin, vmax, 256))
    
    if name_newcmap:
        newcmap = LSC.from_list(name_newcmap, cmap_data, N=cmap_data.shape[0])
        cm.register_cmap(name_newcmap, newcmap)
    else:
        newcmap = LSC.from_list('newcmap', cmap_data, N=cmap_data.shape[0])
    
    return newcmap


def stitch(cmapinlist, vlims, tpoints, name_newcmap=None):
    '''Stich together the selected crops from the given list of colour maps. Can also register the
    new colour map with matplotlib.
    
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
    '''
    
    if not isinstance(cmapinlist, list):
        raise TypeError('cmapinlist must be a list')
    if len(cmapinlist)<2:
        raise ValueError('cmapinlist must contain at least two colour maps')
    if not isinstance(vlims, np.ndarray):
        vlims = np.array(vlims)
    if vlims.shape!=(len(cmapinlist),2):
        raise ValueError('vlims shape does not match expectation of (N,2)')
    for vcheck in vlims:
        if vcheck[0] > vcheck[1]:
            raise ValueError('The value of vmin must be lower than vmax')
    if np.sum((vlims < 0.0) | (vlims > 1.0)) > 0:
        raise ValueError('The values in vlims must be in the closed range [0, 1]')
    if not isinstance(tpoints, np.ndarray):
        tpoints = np.array(tpoints)
    if np.sum(np.diff(tpoints) < 0) > 0:
        raise ValueError('tpoints must be monotonically increasing in value')
    if np.sum((tpoints <= 0.0) | (tpoints >= 1.0)):
        raise ValueError('The values of tpoints must be in the open range (0, 1)')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    cmapinlist = [cm.get_cmap(cmapin) if isinstance(cmapin, str) else cmapin for cmapin in cmapinlist]
    try:
        test = [c(0.5) for c in cmapinlist]
    except TypeError:
        raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    try:
        if np.sum([len(t)!=4 for t in test])<len(test):
            raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    except TypeError:
        raise TypeError('One of the elements in cmapinlist does not behave like a colour map')
    
    tpoints = np.array([0]+list(tpoints)+[1])
    nstep = np.empty(len(cmapinlist))
    test_range = np.linspace(0, 1, 256)
    for i in range(len(cmapinlist)):
        nstep[i] = np.sum((test_range > tpoints[i]) & (test_range < tpoints[i+1])) + 1
    nstep = np.where(nstep < 1, 1, nstep)
    if np.sum(nstep) != 256:
        nstep[-1] += 256-np.sum(nstep)
    nstep = nstep.astype('int')
    
    cmaplist_data = [cmapinlist[i](np.linspace(vlims[i, 0], vlims[i, 1], nstep[i]))
                     for i in range(len(cmapinlist))]
    cmap_data = np.concatenate(cmaplist_data, axis=0)
    
    if name_newcmap:
        newcmap = LSC.from_list(name_newcmap, cmap_data, N=cmap_data.shape[0])
        cm.register_cmap(name_newcmap, newcmap)
    else:
        newcmap = LSC.from_list('newcmap', cmap_data, N=cmap_data.shape[0])
    
    return newcmap


def merge(cmapinlist, tpoints, name_newcmap=None):
    '''Merge together the selected crops from the given list of colour maps. Can also register the
    new colour map with matplotlib. This is a light wrapper around scicm.tools.stitch, which uses
    the transition points as the vmin/vmax values to crop each input colour map.
    
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
    '''
    
    if not isinstance(cmapinlist, list):
        raise TypeError('cmapinlist must be a list')
    if not isinstance(tpoints, np.ndarray):
        tpoints = np.array(tpoints)
    if np.sum(np.diff(tpoints) < 0) > 1:
        raise ValueError('tpoints must be monotonically increasing in value')
    if np.sum((tpoints <= 0.0) | (tpoints >= 1.0)):
        raise ValueError('The values of tpoints must be in the open range (0, 1)')
    if not isinstance(name_newcmap, str) and name_newcmap is not None:
        raise TypeError('name_newcmap must be a string')
    
    vlims = np.array([0]+list(tpoints)+[1])
    vlims = np.array([[vlims[i], vlims[i+1]] for i in range(len(cmapinlist))])
    newcmap = stitch(cmapinlist, vlims, tpoints, name_newcmap)
    
    for vcheck in vlims:
        if vcheck[0] > vcheck[1]:
            raise ValueError('The value of vmin must be lower than vmax')
    
    return newcmap
