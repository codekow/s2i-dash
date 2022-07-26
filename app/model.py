'''
This file will house the data scientists model.
It should be framed as in the example to take inputs and produce an output.

The output should be data (array, pandas dataframe, csv, etc) which are
consumable by the dash application (wsgi.py).

The dash application will recieve the output of the model and use it to produce graphs (layout.py).
If there are no graphs this is unnecessary.

If there is more than one graph,
create more 'layout.py'-type files, each being able to take an input and produce a chart.
'''

import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = pd.read_csv('data/gapminderDataFiveYear.csv')
