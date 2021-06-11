import pandas as pd
import csv
import plotly.figure_factory as pf

reader = pd.read_csv('height.csv')
fig = pf.create_distplot([reader['Weight(Pounds)'].tolist()], [
    'weight'], show_hist=False)
fig.show()
