# SciCM: Scientific Colour Maps

[![Github release](https://img.shields.io/github/release/MBravoS/scicm.svg?label=tag&colorB=54ebff)](https://github.com/MBravoS/scicm/releases) [![PyPI version](https://img.shields.io/pypi/v/scicm.svg?colorB=ff0080)](https://pypi.python.org/pypi/scicm)

<p align="center">
    <img src="https://raw.githubusercontent.com/MBravoS/scicm/master/images/logo.png" width="300">
</p>

**_SciCM_** is a small Python package aimed at providing a large set of good (i.e. perceptually linear) colour maps, constructed with a consistent design philosophy. This package expands and complements the already existent selection of similar colour maps (e.g., [_matplotlib_](https://matplotlib.org/stable/tutorials/colors/colormaps.html), [_ColorCET_](https://github.com/holoviz/colorcet), [_cmocean_](https://github.com/matplotlib/cmocean) and [_CMasher_](https://github.com/1313e/CMasher)). All colour maps in this package have been created using [_viscm_](https://github.com/matplotlib/viscm). Also included are utilities for colour map manipulation.

### Installation and use
The package is available for installation using pip:

    >pip install scicm

Although you may wish to install it directly from GitHub using:

    >pip install git+https://github.com/MBravoS/splotch.git@master

Upon importing _SciCM_, the colour maps are registered with matplotlib, so they can be used by passing `cmap='scicm.cmapname'` to any plotting function that accepts a colour map (e.g. the `cmap` keyword in matplotlib). The colour map objects can also be explicitly accessed using `scicm.cm.cmapname`. Reversed versions of the colour maps are also included, accessible through the same naming convention used by matplotlib (i.e. `cmapname_r`).

### Included Colour Maps

<p align="center">
    <img src="https://raw.githubusercontent.com/MBravoS/scicm/master/images/scicm_all.png" width="800">
</p>
