%pip install pandas numpy matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
%matplotlib inline
mpl.style.use('ggplot')

car=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv')

car.head()
car.shape
car.info()

backup=car.copy()

car=car[car['year'].str.isnumeric()]

car['year']=car['year'].astype(int)

car=car[car['Price']!='Ask For Price']

car['Price']=car['Price'].str.replace(',','').astype(int)

car['kms_driven']=car['kms_driven'].str.split().str.get(0).str.replace(',','')

car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype(int)

car=car[~car['fuel_type'].isna()]
car.shape

car['name']=car['name'].str.split().str.slice(start=0,stop=3).str.join(' ')
car=car.reset_index(drop=True)
