import pandas as pd
import csv
import plotly.figure_factory as pf

reader = pd.read_csv('height.csv')
fig = pf.create_distplot([reader['Height(Inches)'].tolist()], [
                         'height'], show_hist=False)
fig.show()