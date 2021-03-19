# scicm: Science Colour Maps

**scicm** is a small package containing several colour maps, aimed at filling gaps in availability of good (i.e. perceptually linear) in both [matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) as in other available packages (like [cmocean](https://github.com/matplotlib/cmocean) and [CMasher](https://github.com/1313e/CMasher)). All colour maps in this package have been created using [viscm](https://github.com/matplotlib/viscm). The full viscm visualisations are available in the [viscm_files/visualisation_samples](https://github.com/MBravoS/scicm/tree/master/viscm_files/visualisation_samples) folder of this repository.

### Installation and use

The package is available for installation using pip:

    >pip install scicm
    
though you may get directly from GitHub using

    >pip install git+https://github.com/MBravoS/splotch.git@master

On import the colour maps are registered with matplotlib, so they can be used by passing `cmap='scicm.colour_map_name'` to any plotting function that has `cmap` as one of its keywords. The colour maps objects are also accessible suing `scim.cm.colour_map_name`.

### Included colour maps

The first two sets of colour maps are meant as a replacement for the sequential colour maps from matplotlib. All are designed with the same dynamic range in lightness, which means that small value changes are equally distinct. The first set contains the colour maps designed as general-purpose, being not only perceptually linear but also lacking strong hue changes, which could lead the eye to certain value ranges. This near-constant hue also ensures that all are colourblind-friendly.
![cmaps0](/docs/scicm_linear1.png)
The colour maps in the second set possess a small and simple hue change as a function of lightness, intended to transition from one hue to the other roughly halfway in the value range. These colour maps should be used when a greater differentiation between low and high values is desired. Currently not all of them are equally colourblind-friendly, so we recomend checking the viscm visualisations before choosing one.
![cmaps1](/docs/scicm_linear2.png)
The third set is composed of diverging colour maps, which are intended to be use only when visualising data that ranges around a critical value. In most of them the middle point is the darkest, as this clearly distinguishes the middle values from lack of data without the need to set the figure background to a colour other than white. The two colour maps that have a light middle point (*BwR* and *GwP*) add choices for cases where that is not a concern. All these colour maps span the same dynamic range in lightness, both on each side and across maps, and are to a good degree colourblind-friendly.
![cmaps2](/docs/scicm_diverging.png)
The last set is composed of colour maps with special use cases:
- *Day* and *Night*: These are cyclic maps, linear versions of the *twiligfht_shifted* and *twilight* maps from matplotlib, respectively. Cyclic maps should only be used for cyclic data, an easy example being angles, where for example -180° is the same as 180°.
- *Tropical*: a linear map that has been designed for plots where the intention is to highlight broad regions of the data, through the use of a wide range of hues. For this purpose also it has been designed with a less than hlaf of the lightness dynamic range than our other linear maps. Due to these design choices, is not very colourblind-friendly, but for red-green colourblindness it appears as two regions with the transition near the middle of the map, so it is not the worst compromise.
- *Edges*: a linear map inspired by cmocean's Oxy. It has *Stone* as a base, but with the notable distinction that for \[normalised\] values below 0.2 and above 0.8 it changes colour (to blue an yellow, respectively). This is meant to highlight extreme values of the data.
- *Quartile*: an experimental colour map, composed of four linear segments of significantly different hues, though still perfectly linear in greyscale. This colour map is meant as an option instead of filled contours, as it displays information inside the contours which would be otherwise lost, or to be used to sample colours from.
![cmaps3](/docs/scicm_miscellaneous.png)

### Example

Here is an example application of **scicm**:

```python
#Importing libraries
import scicm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

# Generating random data
rng=np.random.default_rng()
x=np.concatenate([rng.normal(-1,0.5,60000),rng.normal(1,0.8,40000)],axis=0)
y=x+np.cos(x/3)*rng.normal(0,1,100000)

# Plotting
fig=plt.figure(figsize=(12,8))
spec=gs.GridSpec(nrows=2,ncols=2,figure=fig,wspace=0,hspace=0,left=0.0,
                 right=0.999,bottom=0.001,top=1.0)
fax=[fig.add_subplot(spec[0,0]),fig.add_subplot(spec[0,1]),
     fig.add_subplot(spec[1,0]),fig.add_subplot(spec[1,1])]

for f in fax:
    f.set_xticks([])
    f.set_yticks([])

fax[0].hexbin(x,y,lw=0,cmap='scicm.Cyan',mincnt=1) # Using the registered names with matplotlib
fax[0].text(-3.3,4.6,'Cyan',fontsize=20)
fax[1].hexbin(x,y,lw=0,cmap='scicm.C2G',mincnt=1)
fax[1].text(-3.3,4.6,'C2G',fontsize=20)
fax[2].hexbin(x,y,lw=0,cmap=scicm.cm.YkM,mincnt=1) # Using the colour map objects
fax[2].text(-3.3,4.6,'YkM',fontsize=20)
fax[3].hexbin(x,y,lw=0,cmap=scicm.cm.Edges,mincnt=1)
fax[3].text(-3.3,4.6,'Edges',fontsize=20)

plt.show()
```

This is the resulting image:
![example](/docs/README_ex.png)

Current version: 0.0.8
