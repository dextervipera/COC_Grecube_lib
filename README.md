# COC_Grecube_lib

a simple script for plotting TDS data.

## structure

1. [Jupyter Notebooks] - Only for high-level operating
2. [.py] files - Functions inside

## Basic function

```py
def plot_tds(filenames, temperature_map: dict = None, name_map: dict = None, plt_setts: dict = None):
...
```

filenames: a list of files (or a single file) to plot

### maps format
```py
_samp_temperature_map = {
    'COC1':'220',
    'COC2':'225',
    'COC3':'230',
    'COC4':'235',
    'COC5':'240',
    'COC6':'245',
    'COC7':'250',
    'COC8':'255',
    'COC9':'260'}
```

### plot settings
```py
_plt_setts = {
    'title': 'default_title',
    'size': (7,5),
    'ax_size': [.1,.1,1.6,.8]    
}
```