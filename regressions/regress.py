
import numpy as np
import pandas as pd
from pandas.stats.api import ols

from rawdata import df

result = ols(y=df['understanding'], x=df[['condition0', 'age','english','education']])
print result
