'''
This file will house the data scientists model.
It should be framed as in the example to take inputs and produce an output.

The output should be data (array, pandas dataframe, csv, etc) which are
consumable by the dash application (wsgi.py).

The dash application will recieve the output of the model and use it to produce graphs (graph.py).
If there are no graphs this is unnecessary.

If there is more than one graph,
create more 'graph.py'-type files, each being able to take an input and produce a chart.
'''

import numpy as np
import pandas as pd

def gen_data(numdots):
    df = pd.DataFrame(np.random.randint(0, 100, size=(numdots, 2)), columns=list('XY'))
    print(df)
    return df
