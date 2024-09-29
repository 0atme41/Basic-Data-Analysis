import math
import collections
import numpy as np
import pandas as pd
import matplotlib as pp
import zipfile

zipfile.ZipFile("names.zip").extractall(".")

allyears = pd.concat(pd.read_csv(f'names/yob{year}.txt', names=['name', 'sex', 'number']).assign(year=year) for year in range(1880, 2019))

allyears.to_csv('allyears.csv.gz', index=False)