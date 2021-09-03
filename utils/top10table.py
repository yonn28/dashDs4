import pandas as pd
# Visualization:
import plotly.io as pio
import plotly.figure_factory as ff
import plotly.express as px
from functools import reduce
import numpy as np
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

"""
Cleans the top 10% table, reversing one hot encoding and selecting columns of interest
"""
def table_to_show(df):

    def nvals(row, cols):
        sum = 0
        for item in cols:
            sum += row[item]
        if sum == 0:
            return 1
        else:
            return 0

    cols = ['MIN_ZScorePesoTalla_12M', 'AVG_ZScorePesoTalla_12M', 'MAX_ZScorePesoTalla_12M', 'Veces_DesnutricionSM_12M',
         'Veces_SobrePeso_12M', 'Veces_Normal_12M', 'TienePasado', 'Veces_Normal_12M', 'sexo_persona_1.0',
         'tip_cuidado_niños_2.0', 'tip_cuidado_niños_3.0', 'tip_cuidado_niños_4.0', 'tip_cuidado_niños_5.0',
         'tip_cuidado_niños_6.0', 'tip_cuidado_niños_7.0', 'tip_cuidado_niños_8.0', 'tip_cuidado_niños_9.0',
         'ingresos_promp_imp', 'gasto_ppers_imp', 'gasto_alim_ppers_imp', 'uni_dias_agua', 'cod_clase_2.0',
         'cod_clase_3.0', 'noprivaciones', 'ind_estudia_1.0', 'estrato_1.0', 'estrato_2.0', 'estrato_3.0',
         'estrato_4.0', 'estrato_5.0', 'estrato_6.0']
    df_f = df[cols]

    cols1 = ['tip_cuidado_niños_2.0', 'tip_cuidado_niños_3.0', 'tip_cuidado_niños_4.0', 'tip_cuidado_niños_5.0',
             'tip_cuidado_niños_6.0', 'tip_cuidado_niños_7.0', 'tip_cuidado_niños_8.0', 'tip_cuidado_niños_9.0']
    df_f1 = df_f[cols1].copy()
    df_f1['tipo_cuidado_0.0'] = df_f1.apply(lambda row: nvals(row, cols1), axis=1)
    df_f1['tipo_cuidado'] = df_f1.idxmax(1).apply(lambda s: s[-3])
    df_f2 = pd.DataFrame(df_f1['tipo_cuidado'])

    cols2 = ['cod_clase_2.0', 'cod_clase_3.0']
    df_f3 = df_f[cols2].copy()
    df_f3['cod_clase_0.0'] = df_f3.apply(lambda row: nvals(row, cols2), axis=1)
    df_f3['cod_clase'] = df_f3.idxmax(1).apply(lambda s: s[-3])
    df_f4 = pd.DataFrame(df_f3['cod_clase'])

    df_f5 = df_f[['ind_estudia_1.0']].copy()
    df_f5['ind_estudia_0.0'] = df_f5['ind_estudia_1.0'].apply(lambda row: int(row == 0))
    df_f5['ind_estudia'] = df_f5.idxmax(1).apply(lambda s: s[-3])
    df_f6 = pd.DataFrame(df_f5['ind_estudia'])

    df_f7 = df_f[['sexo_persona_1.0']].copy()
    df_f7['sexo_persona_0.0'] = df_f7['sexo_persona_1.0'].apply(lambda row: int(row == 0))
    df_f7['sexo_persona'] = df_f7.idxmax(1).apply(lambda s: s[-3])
    df_f7['sexo_persona'] = df_f7['sexo_persona'].map({'0': 'M', '1': 'F'})
    df_f8 = pd.DataFrame(df_f7['sexo_persona'])

    cols3 = ['estrato_1.0', 'estrato_2.0', 'estrato_3.0', 'estrato_4.0', 'estrato_5.0', 'estrato_6.0']
    df_f11 = df_f[cols].copy()
    df_f11['estrato_0.0'] = df_f11.apply(lambda row: nvals(row, cols3), axis=1)
    df_f11['estrato'] = df_f11.idxmax(1).apply(lambda s: s[-3])
    df_f12 = pd.DataFrame(df_f11['estrato'])

    data_frames = [df_f2, df_f4, df_f6, df_f8, df_f12]
    df_9 = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True,
                                               how='outer'), data_frames)
    df_f10 = df[['Probability', 'MIN_ZScorePesoTalla_12M', 'AVG_ZScorePesoTalla_12M', 'MAX_ZScorePesoTalla_12M',
                 'Veces_DesnutricionSM_12M', 'Veces_SobrePeso_12M', 'Veces_Normal_12M', 'TienePasado',
                 'ingresos_promp_imp', 'gasto_ppers_imp', 'gasto_alim_ppers_imp', 'uni_dias_agua', 'noprivaciones']]

    df_show = pd.merge(df_f10, df_9, left_index=True, right_index=True, how='outer')
    df_show['Probability'] = df_show['Probability'].apply(lambda x: round(x, 2))
    df_show['MIN_ZScorePesoTalla_12M'] = df_show['MIN_ZScorePesoTalla_12M'].apply(lambda x: round(x, 2))
    df_show['AVG_ZScorePesoTalla_12M'] = df_show['AVG_ZScorePesoTalla_12M'].apply(lambda x: round(x, 2))
    df_show['MAX_ZScorePesoTalla_12M'] = df_show['MAX_ZScorePesoTalla_12M'].apply(lambda x: round(x, 2))
    df_show['noprivaciones'] = df_show['noprivaciones'].apply(lambda x: round(x, 2))
    df_show['uni_dias_agua'] = df_show['uni_dias_agua'].apply(lambda x: round(x, 1))
    df_show.reset_index(inplace=True)
    df_show = df_show.rename(columns={'index': 'Child ID', 'MIN_ZScorePesoTalla_12M': 'MIN ZScore',
                                      'MAX_ZScorePesoTalla_12M': 'MAX ZScore', 'AVG_ZScorePesoTalla_12M': 'AVG ZScore',
                                      'Veces_DesnutricionSM_12M': 'Malnutrition Count',
                                      'Veces_Normal_12M': 'Appropiate Count'})

    df_table = df_show[['Child ID', 'MIN ZScore', 'MAX ZScore', 'AVG ZScore', 'Malnutrition Count', 'Appropiate Count', 'Probability']].copy()

    df_plots = df_show[['Child ID', 'ind_estudia', 'ingresos_promp_imp', 'uni_dias_agua', 'noprivaciones',
                        'tipo_cuidado', 'cod_clase', 'sexo_persona', 'estrato']].copy()

    return df_table, df_plots