import pandas as pd
# Visualization:
import plotly.io as pio
import plotly.figure_factory as ff
import plotly.express as px
from functools import reduce
import numpy as np
pio.renderers.default = 'browser'

def zscore_distplot(df):
    colors = ["#1CBE4F","#3366CC"]
    x1 = np.random.randn(1000)
    group_labels = ['General', 'Risk']  # name of the dataset
    l = list(df['AVG ZScore'].dropna())

    # Create distplot with custom bin_size
    fig = ff.create_distplot([x1, l], group_labels, bin_size=.1,
                             colors=colors, show_rug=False)
    fig.update_layout(autosize=True, xaxis_title="AVG ZScore", yaxis_title="Density")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig