import asyncio

import panel as pn
import numpy as np
import pandas as pd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from panel.io.pyodide import show

df = pd.DataFrame(np.random.randn(10, 4),  columns=list('ABCD')).cumsum()
p = figure(height=450, width=600)

cds = ColumnDataSource(data=ColumnDataSource.from_df(df))

p.line('index', 'A', source=cds, line_color='firebrick')
p.line('index', 'B', source=cds, line_color='dodgerblue')
p.line('index', 'C', source=cds, line_color='goldenrod')
p.line('index', 'D', source=cds, line_color='purple')

await show(p, 'plot')