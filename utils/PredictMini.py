# -*- coding: utf-8 -*-
"""

Creado el 23/08/21


"""

'''

1. Librerias

'''

#Tratamiento de datos:

import pandas as pd

# Cargar y guardar modelos sklearn:

import joblib

# Visualization:

import plotly.graph_objects as go
import plotly.io as pio
import shap  # package used to calculate Shap values

import matplotlib.pyplot as plt

#pio.renderers.default='svg'
pio.renderers.default = 'browser'

'''

2. Parámetros de corrida


'''

# 1. Path a los modelos:

#pathModeloRelapse = "./Modelo_relapse_subset.sav"
#pathModeloMalnutrition = "./Modelo_malnutrition_subset.sav"

'''

3. Decidir el valor de las variables:


'''




'''

4. Cargar los modelos:


'''

#modelo_relapse = joblib.load(pathModeloRelapse)
#modelo_malnutrition = joblib.load(pathModeloMalnutrition)

'''

5. Función para convertir los valores de las variables en la base para el modelo:
    

'''

def convertirDicEnBase(valoresIngresados):
    
    # Crear un nuevo diccionario:
        
    valoresFinales = {}
    
    # Los primeros 5 valores son los mismos:
        
    for i in ["AVG_ZScorePesoTalla_12M","MAX_ZScorePesoTalla_12M","Veces_DesnutricionSM_12M","Veces_SobrePeso_12M","MIN_ZScorePesoTalla_12M"]:
        
        valoresFinales[i] = [valoresIngresados[i]]
        
    # Para tip_cuidado_niños:
        
    if valoresIngresados["tip_cuidado_niños"] == 2.0:
        valoresFinales["tip_cuidado_niños_2.0"] = [1]
    else:
        valoresFinales["tip_cuidado_niños_2.0"] = [0]
    
    if valoresIngresados["ind_discap"] == "ninguna":
        valoresFinales["ind_discap_ninguna_1.0"] = [1]
    else:
        valoresFinales["ind_discap_ninguna_1.0"] = [0]
        
    if valoresIngresados["ind_leer_escribir"] == 9.0:
        valoresFinales["ind_leer_escribir_9.0"] = [1]
    else:
        valoresFinales["ind_leer_escribir_9.0"] = [0]
        
    if valoresIngresados["ind_estudia"] == 1.0:
        valoresFinales["ind_estudia_1.0"] = [1]
    else:
        valoresFinales["ind_estudia_1.0"] = [0]
       
    if valoresIngresados["ind_recibe_comida"] == 1.0:
        valoresFinales["ind_recibe_comida_1.0"] = [1]
    else:
        valoresFinales["ind_recibe_comida_1.0"] = [0]
        

    return(pd.DataFrame.from_dict(valoresFinales,orient='columns'))
    




'''

5. Función para crear un grafico con los shap values:


'''


def plotShapValues(objeto_modelo,base_variables):

    # Select some random rows:

    base_variables_p = base_variables.copy()

    # Create object that can calculate shap values

    explainer = shap.TreeExplainer(objeto_modelo)

    # Calculate Shap values

    shap_values = explainer.shap_values(base_variables_p)

    # Shap values summary:

    plt.figure(0)

    shap.plots._waterfall.waterfall_legacy(explainer.expected_value[1], shap_values[1][0],feature_names = base_variables.columns,show=True)
    #shap.plots.force(explainer.expected_value[1], shap_values[1][0],feature_names = base_variables.columns,matplotlib=True,show=False,features=base_variables)

    


'''

5. Función para obtener la probabilidad

'''

def obtenerProbabilidad(objeto_modelo,base_variables):
    return(objeto_modelo.predict_proba(base_variables)[:,1])

    
# Ejemplo de como usarla:

print(obtenerProbabilidad(modelo_relapse,base_variables))
