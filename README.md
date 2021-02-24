## scicm: Science Colour Maps

**scicm** is a small package containing several colour maps created using viscm.

The package is available for installation using `>pip install scicm`, though you may get directly from GitHub using `>pip install git+https://github.com/MBravoS/splotch.git@master`. On import the colour maps are registered with matplotlib, so they can be used
by passing `cmap='scicm.colour_map_name'` to any plotting function that has `cmap` as one of its keywords.

Available colour maps:
- Linear:
    - 'blue2cyan'
    - 'blue'
    - 'cyan'
    - 'green2yellow'
    - 'magenta'
    - 'orange'
    - 'purple2magenta'
    - 'red2orange'
    - 'stone'
    - 'yellow'
    - 'blue2purple'
    - 'cyan2green'
    - 'green'
    - 'magenta2red'
    - 'orange2yellow'
    - 'purple'
    - 'red'
- Diverging:
    - 'BkG'
    - 'CkO'
    - 'GwP'
    - 'BkR'
    - 'BwR'
    - 'GkP'
    - 'PkO'
    - 'YkM'
- Special:
    - 'quartile'

Current version: 0.0.3
