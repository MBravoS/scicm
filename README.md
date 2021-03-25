# scicm: Science Colour Maps

**scicm** is a small package containing several colour maps, aimed at filling gaps in the availability of good (i.e. perceptually linear) in both [matplotlib](https://matplotlib.org/stable/tutorials/colors/colormaps.html) and in other available packages (like [cmocean](https://github.com/matplotlib/cmocean) and [CMasher](https://github.com/1313e/CMasher)). All colour maps in this package have been created using [viscm](https://github.com/matplotlib/viscm). The full viscm visualisations are available in the [viscm_files/visualisation_samples](https://github.com/MBravoS/scicm/tree/master/viscm_files/visualisation_samples) folder of this repository.

### Installation and use

The package is available for installation using pip:

    >pip install scicm
    
Although you may wish to install it directly from GitHub using:

    >pip install git+https://github.com/MBravoS/splotch.git@master

Upon importing scicm, the colour maps are registered with matplotlib, so they can be used by passing `cmap='scicm.cmapname'` to any plotting function that accepts a colour map (e.g. the `cmap` keyword in matplotlib). The colour map objects can also be explicitly accessed using `scicm.cm.cmapname`. Reversed versions of the colour maps are also included, accessible through the same naming convention used by matplotlib (i.e. `<cmapname>_r`).

### Included Colour Maps

#### Monochromatic colour maps
The first two sets of colour maps are meant as a replacement for the sequential colour maps from matplotlib. All are designed with the same dynamic range in lightness, which means that small value changes are equally distinct. The first set contains the colour maps designed as general-purpose, being not only perceptually linear but also lacking strong hue changes, which could mistakenly lead the eye to certain value ranges. This *near-constant* hue also ensures that they are all colourblind-friendly.
![cmaps0](/examples/scicm_monochromat.png)
<br><br>

#### Dichromatic colour maps
The colour maps in the second set contain small and simple hue changes as a function of lightness, intended to transition from one hue to the other roughly halfway in the value range. These colour maps should be used when a greater differentiation between low and high values is desired. Of course, these colour maps are not equally colourblind-friendly, so we recommend checking the viscm visualisations before choosing one.
![cmaps1](/examples/scicm_dichromat.png)
<br><br>

#### Diverging colour maps
The third set is composed of diverging colour maps, which are intended to be used only when visualising data that is centered around a critical value. In most cases, the middle point is the darkest, as this clearly distinguishes the middle values from lack of data without the need to set the figure background to a colour other than white. The two colour maps that have a light middle point (*BwR* and *GwP*) add choices for cases where that is not a concern. All these colour maps span the same dynamic range in lightness on each side and across maps and are intended to be colourblind-friendly to a good degree.
![cmaps2](/examples/scicm_diverging.png)
<br><br>

#### Miscellaneous colour maps
The last set is composed of colour maps with special use cases:
- *Day* and *Night*: Cyclic colour maps, linear adaptions of the *twilight_shifted* and *twilight* maps from matplotlib, respectively. Cyclic maps should only be used for cyclic data, an easy example being angles where -180° is the same as 180°.
- *Garnet*, *Ripe* and *Tropical*: Linear colour maps that have been designed for plots where the intention is to highlight broad regions of the data through large variations in hue. For this purpose, they have been designed with less than half of the lightness dynamic range than our other linear maps. Due to these design choices, they are inherently less colourblind-friendly than the rest of the colour maps.
- *Edges*: A linear colour map inspired by cmocean's Oxy. It uses *Stone* as a base, but with the notable distinction that for \[normalised\] values below 0.2 and above 0.8 it changes colour (to blue and yellow, respectively). This is intended to selectively highlight the extreme values of the data.
- *Quartile*: An experimental colour map, composed of four linear segments of significantly different hues, though still perfectly linear in greyscale. This colour map is meant as an alternative to filled contours, as it displays information inside the contours that would be otherwise lost.
![cmaps3](/examples/scicm_miscellaneous.png)

### Example

Here is an example application of **scicm**:

```python
#Importing libraries
import scicm
import numpy as np
import matplotlib.pyplot as plt

# Generating random data
rng=np.random.default_rng()
x=np.concatenate([rng.normal(-1,0.5,60000),rng.normal(1,0.8,40000)],axis=0)
y=x+np.cos(x/3)*rng.normal(0,1,100000)

# Plotting
fig, axes = plt.subplots(nrows=2,ncols=2,figsize=(12,8),gridspec_kw=dict(wspace=0.0,hspace=0.0))

axes[0,0].hexbin(x,y,lw=0,mincnt=1, cmap='scicm.Cyan') # Using the registered names with matplotlib
axes[0,1].hexbin(x,y,lw=0,mincnt=1, cmap='scicm.C2G_r') # Reversing the colour map
axes[1,0].hexbin(x,y,lw=0,mincnt=1, cmap=scicm.cm.PkO_r) # Using the colour map objects
axes[1,1].hexbin(x,y,lw=0,mincnt=1, cmap=scicm.cm.Edges)

for ax, txt in zip(axes.flatten(),['Cyan','C2G_r','PkO_r','Edges']):
    ax.text(-3.3,4.6,txt,fontsize=20)
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
```

This is the resulting image:
![example](/examples/README_ex.png)

Current version: 0.2.3
