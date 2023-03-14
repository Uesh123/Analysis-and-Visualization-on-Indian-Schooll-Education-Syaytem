import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
    page_icon='📈',
    page_title="Schools with Girls Toilet Data Analysis",
    layout='wide'
)

@st.cache
def load_data():
    df=pd.read_csv('Data/schools-with-girls-toilet-2013-2016.csv')
    df['State_UT'].unique()
    all_columns=df.columns.to_list()
    categ=all_columns[2:]
    df['year'].value_counts()
    years=df['year'].unique().tolist()
    return df

st.title('Schools Percentage with Girls Toilet From 2013 - 2016 ')
df = load_data()
st.dataframe(df,use_container_width=True)

Data1= df.groupby('year')[['Primary_Only','U_Primary_Only']].sum()
st.title('Comparision of Primary Girls and Upper Primary Girls in Percentage of schools with Girls Toilet over 2013 to 2016')
st.bar_chart(Data1)

Data2=df.groupby('year')[['Sec_Only','HrSec_Only']].sum()
st.title('Comparision of Secondary Girls and HrSecondary Girls in Percentage of schools with Girls Toilet over 2013 to 2016')
st.bar_chart(Data2)

Data3=df.groupby('year')[['Primary_with_U_Primary','Primary_with_U_Primary_Sec']].sum()
st.title('Comparision of (Primary with Upper Primary Girls) and (Primary with Upper Primary Seccondary Girls) in Percentage of schools with Girls Toilet over 2013 to 2016')
st.bar_chart(Data3)

Data4=df.groupby('year')[['Primary_with_U_Primary_Sec_HrSec','U_Primary_With_Sec_HrSec']].sum()
st.title('Comparision of (Primary with Upper Primary and Secondary and HrSecondary Girls) and (Upper Primary With Secondary and HrSecondary Girls) Percentage of schools with Girls Toilet over 2013 to 2016')
st.bar_chart(Data4)

Data5=df.groupby('year')[['U_Primary_With_Sec','Sec_with_HrSec.']].sum()
st.title('Comparision of (Upper Primary With Secondary Girls) and (Secondary with HrSecondary Girls) in Percentage of schools with Girls Toilet over 2013 to 2016')
st.bar_chart(Data5)

















