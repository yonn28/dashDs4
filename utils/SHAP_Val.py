import plotly.io as pio
import shap  # package used to calculate Shap values
import matplotlib.pyplot as plt
import io
import base64
import plotly.express as px

#pio.renderers.default='svg'
pio.renderers.default = 'browser'

def plotShapValuesTop(objeto_modelo, base_variables):
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
    buf = io.BytesIO()
    shap.summary_plot(shap_values[1],
                             base_variables, show=False)
    plt.savefig(buf, format="png", dpi=150, bbox_inches='tight')  # save to the above file object
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8")  # encode to html elements
    return "data:image/png;base64,{}".format(data)