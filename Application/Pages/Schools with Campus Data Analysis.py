import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_icon='📈',
    page_title="Schools with Campus Data Analysis",
    layout='wide'
)

@st.cache
def load_data():
    df=pd.read_csv('Data/percentage-of-schools-with-comps-2013-2016.csv')
    df['State_UT'].unique()
    all_columns=df.columns.tolist()
    categ=all_columns[2:]
    year=df['year'].unique().tolist()
    return df

st.title('Schools Percentage with Campus From 2013 - 2016 ')
df = load_data()
st.dataframe(df,use_container_width=True)





fig1=df.groupby('year')[['Primary_Only','U_Primary_Only']].sum()
st.title('Comparision of Primary and Upper Primary in Percentage of schools with Campus Facility over 2013 to 2016')
st.bar_chart(fig1)

fig2=df.groupby('year')[['Sec_Only','HrSec_Only']].sum()
st.title('Comparision of Secondary and HrSecondary in Percentage of schools with Campus Facility over 2013 to 2016')
st.bar_chart(fig2)

fig3=df.groupby('year')[['Primary_with_U_Primary','Primary_with_U_Primary_Sec']].sum()
st.title('Comparision of Primary with Upper Primary and Primary with Upper Primary Secondary in Percentage of schools with Campus Facility over 2013 to 2016')
st.bar_chart(fig3)

fig4=df.groupby('year')[['Primary_with_U_Primary_Sec_HrSec','U_Primary_With_Sec_HrSec']].sum()
st.title('Comparision of Primary with Upper Primary and Secondary and HrSecondary','Upper Primary With Secondary and HrSecondary Percentage of schools with Campus Facility over 2013 to 2016')
st.bar_chart(fig4)

fig5=df.groupby('year')[['U_Primary_With_Sec','Sec_with_HrSec.']].sum()
st.title('Comparision of Upper Primary With Secondary and Secondary with HrSecondary in Percentage of schools with Campus Facility over 2013 to 2016')
st.bar_chart(fig5)