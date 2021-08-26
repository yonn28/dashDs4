import pandas as pd
# Visualization:
import plotly.io as pio

pio.renderers.default = 'browser'


def createTable_top(objeto_modelo, base_variables):
    # Create a new column with the predicted probability:

    base_variables.loc[:, "Probability"] = objeto_modelo.predict_proba(base_variables)[:, 1]
    base_variables = base_variables.sort_values("Probability", ascending=False)

    # Create a column with the range of the probability:

    base_variables.loc[:, "Range_probability"] = pd.qcut(base_variables['Probability'], q=10, precision=0,
                                                         duplicates='drop')

    # Top 10%

    a = pd.DataFrame(base_variables.groupby(["Range_probability"]).size().reset_index()).rename(columns={0: 'Total'})
    buscado = a.loc[9, "Range_probability"]

    c_df = base_variables[base_variables["Range_probability"] == buscado]

    return (c_df)