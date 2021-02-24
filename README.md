## scicm: Science Colour Maps

**scicm** is a small package containing several colour maps created using viscm.

The package is available for installation using `>pip install scicm`, though you may get directly from GitHub using `>pip install git+https://github.com/MBravoS/splotch.git@master`. On import the colour maps are registered with matplotlib, so they can be used
by passing `cmap='scicm.colour_map_name'` to any plotting function that has `cmap` as one of its keywords.

Available colour maps:
- Monotonic:
    - Single colour:
        - 'Blue'
        - 'Cyan'
        - 'Green'
        - 'Magenta'
        - 'Orange'
        - 'Purple'
        - 'Red'
        - 'Stone'
        - 'Yellow'
    - Two colours:
        - 'B2C'
        - 'B2P'
        - 'C2G'
        - 'G2Y'
        - 'M2R'
        - 'O2Y'
        - 'P2M'
        - 'R2O'
- Diverging:
    - Black centre:
        - 'BkG'
        - 'BkR'
        - 'CkO'
        - 'GkP'
        - 'PkO'
        - 'YkM'
    - White centre:
        - 'BwR'
        - 'GwP'
- Special:
    - 'Quartile'

Current version: 0.0.4
