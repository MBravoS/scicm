# _SciCM_: Scientific Colour Maps

[![Github release](https://img.shields.io/github/release/MBravoS/scicm.svg?label=tag&colorB=54ebff)](https://github.com/MBravoS/scicm/releases) [![PyPI version](https://img.shields.io/pypi/v/scicm.svg?colorB=ff0080)](https://pypi.python.org/pypi/scicm) [![License](https://img.shields.io/github/release/MBravoS/scicm.svg)](https://github.com/MBravoS/scicm/blob/main/LICENSE) ![GitHub Actions CI](https://github.com/MBravoS/scicm/actions/workflows/test-scicm.yml/badge.svg)

<p align="center">
    <img src="https://raw.githubusercontent.com/MBravoS/scicm/master/images/logo.png" width="300">
</p>

**_SciCM_** is a Python package aimed at providing a large set of colour maps designed for scientific data visualisation.
The colour maps in _SciCM_ have been designed to be as interchangeable as possible within the same category, e.g., all diverging colour maps included in _SciCM_ do an (almost) equal job of displaying the data.
All colour maps included in _SciCM_ remain readable for people with red-green colour blindness (the most common type).
This design frees the user in their choice of colour map to use for their data visualisation.
_SciCM_ also includes some simple colour map manipulation tools, for users that want to further customise their colour maps.

## Quick start
Upon importing _SciCM_, the colour maps are registered with matplotlib, so they can be accessed by passing `cmap='scicm.cmapname'` to any plotting function that accepts a colour map (e.g. the `cmap` keyword in matplotlib).
The colour map objects themselves can also be explicitly accessed using `scicm.cm.cmapname`.
All colour maps have a reversed version, accessible through the same naming convention used by matplotlib (i.e. `cmapname_r`).


A simple example of _SciCM_ in use:
```python
    import numpy as np, matplotlib.pyplot as plt, scicm
    
    x = np.random.default_rng().normal(size=(200, 200))
    
    plt.imshow(x, cmap='scicm.Stone')
    plt.show()
```

### Included Colour Maps

<p align="center">
    <img src="https://raw.githubusercontent.com/MBravoS/scicm/master/images/scicm_all.png" width="800">
</p>

## Documentation and use guides
_SciCM_'s GitHub Wiki contains an [extended quick start guide](https://github.com/MBravoS/scicm/wiki/Quick-Start), the [full documentation](https://github.com/MBravoS/scicm/wiki/Code-Documentation) of the package, and a [guide on how to choose the best colour map for your data](https://github.com/MBravoS/scicm/wiki/How-to-choose-which-colour-map-to-use).

## _SciCM_ in the broader colour map Python package ecosystem
_SciCM_ is not the first package to include "good" (perceptually-uniform) colour maps, but meaningfully expands the current availabily of such maps.
Compared to other similar packages:
- [_matplotlib_](https://matplotlib.org/stable/tutorials/colors/colormaps.html): Includes only 5 perceptually-uniform maps, which is less than 10% of all the available colour maps. The main aim of _SciCM_ is to provide perceptually-uniform alternatives to the sequential, diverging, and cyclic colour map types in _matplotlib_.
- [_ColorCET_](https://github.com/holoviz/colorcet): Perhaps the closest colour map package to _SciCM_ in both scope and size. The main difference being that _ColorCET_ features a large set of variations for a small number of individual colour maps, whereas _SciCM_ provides a large set of variations for a small number of colour map "types".
- [_cmocean_](https://github.com/matplotlib/cmocean): A relatively small set of perceptually uniform colour maps, with a design clearly catered for geographic and oceanographic use. Of note is the `oxy` colour map included in _cmocean_, which was the main source of inspiration for _SciCM_'s segmented category of colour maps.
- [_CMasher_](https://github.com/1313e/CMasher): While there is some overlap between both packages, _CMasher_ and _SciCM_ are natural companions, as the two focus on offering alternatives to different sets of _matplotlib_'s colour map categories.

## Installation guide
The package is available for installation using pip:

    >pip install scicm

Although you may wish to install it directly from GitHub using:

    >pip install git+https://github.com/MBravoS/splotch.git@master

## How to cite the use of _SciCM_
If you are submitting work that uses _SciCM_ for publication in a scientific journal, please include a mention of your use.
Some journals include a dedicated section for this purpose (e.g., the [_Software_ section in the Astrophysical Journal](https://journals.aas.org/aastexguide/#software)), which would be the natural place to mention SciCM (please include a link to this repository).
If such a section is not included on your journal or choice, please consider adding the following to your acknowledgements:
> The analysis in this work has been performed using the Python programming language, with the open-source package _SciCM_ (https://github.com/MBravoS/scicm).

Feel free to expand the previous statement to include the rest of the sofware used in your work!
Note that we aim to submit _SciCM_ for publication sometime in 2023, so how to acknowledge your use of _SciCM_ will (hopefully) soon change.
