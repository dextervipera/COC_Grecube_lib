import re
import pandas as pd

def print_inventory(dct):
    print("List cute print:")
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        print("{} ({})".format(item, amount))

def parse_filename(filename:str, material_len = 3):
    # COC1_P1 C_4021 001.csv
    result = re.split('_|, ,| ', filename)
    parsed = {'material': result[0][:material_len],
              'index': int(result[0][material_len:]),
              'take': int(result[1][1:]),
              'width': int(result[3])},
    
    return parsed[0]

def read_COC(fname:str):
    data =  pd.read_csv(fname, decimal='.', skiprows=1)
    name_alias = ['Sample Time Domain Signal x axis', 'X',
       'WaveNumber', 'Sample Spectrum', 'Sample Phase x axis',
       'Sample Phase', 'Reference Time Domain Signal x axis',
       'Reference Time Domain Signal', 'Reference Spectrum x axis',
       'Reference Spectrum', 'Reference Phase x axis', 'Reference Phase',
       'Transmittance x axis', 'Transmittance', 'Transmittance Phase x axis',
       'Transmittance Phase', 'Absorbance x axis', 'Absorbance',
       'Refractive Indices x axis', 'Refractive',
       'Absorption Co-efficient x axis', 'Absorption',
       'Dielectric Constant (Real) x axis', 'Dielectric Constant (Real)',
       'Dielectric Constant (Imag) x axis', 'Dielectric Constant (Imag)']
    
    data.columns = name_alias
    return data