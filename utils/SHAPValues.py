#Tratamiento de datos:
import pandas as pd
import joblib # Cargar y guardar modelos sklearn

# Visualization:

import plotly.graph_objects as go
import plotly.io as pio
import shap  # package used to calculate Shap values

import matplotlib.pyplot as plt
import plotly.express as px

#pio.renderers.default='svg'
pio.renderers.default = 'browser'

def plotShapValuesTop(objeto_modelo, base_variables):
    # Create a new column with the predicted probability:

    base_variables.loc[:, "Probability"] = objeto_modelo.predict_proba(base_variables)[:, 1]

    # Create a column with the range of the probability:

    base_variables.loc[:, "Range_probability"] = pd.qcut(base_variables['Probability'], q=10, precision=0,
                                                         duplicates='drop')

    # Top 10%

    a = pd.DataFrame(base_variables.groupby(["Range_probability"]).size().reset_index()).rename(columns={0: 'Total'})
    buscado = a.loc[9, "Range_probability"]

    base_variables = base_variables[base_variables["Range_probability"] == buscado]
    base_variables = base_variables.drop("Range_probability", axis=1)
    base_variables = base_variables.drop("Probability", axis=1)

    # Select some random rows:

    if base_variables.shape[0] > 1000:
        base_variables = base_variables.sample(n=1000)

    # Create object that can calculate shap values

    explainer = shap.TreeExplainer(objeto_modelo)

    # Calculate Shap values

    shap_values = explainer.shap_values(base_variables)

    # Shap values summary:

    plt.figure(0)
    shap.summary_plot(shap_values[1],
                      base_variables)  # ,max_display=400) #Este parametro permite jugar con cuantas variables mostrar