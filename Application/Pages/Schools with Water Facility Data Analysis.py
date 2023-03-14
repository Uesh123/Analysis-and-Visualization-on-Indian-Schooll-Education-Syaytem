import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
    page_icon='📈',
    page_title="Schools with Water Facility Data Analysis",
    layout='wide'
)

@st.cache
def load_data():
    df=pd.read_csv('Data/percentage-of-schools-with-water-facility-2013-2016.csv')
    df['State/UT'].unique()
    all_columns=df.columns.tolist()
    years=df['Year'].unique().tolist()
    categ=all_columns[2:]
    return df

st.title('Schools Percentage with Water Facility From 2013 - 2016 ')
df = load_data()
st.dataframe(df,use_container_width=True)

Data1=df.groupby('Year')[['Primary_Only','U_Primary_Only']].sum()
st.title('Comparision of Primary and Upper Primary in Percentage of schools with Water Facility over 2013 to 2016')
st.bar_chart(Data1)

Data2=df.groupby('Year')[['Sec_Only','HrSec_Only']].sum()
st.title('Comparision of Secondary and HrSecondary in Percentage of schools with Water Facility over 2013 to 2016')
st.bar_chart(Data2)

Data3=df.groupby('Year')[['Primary_with_U_Primary','Primary_with_U_Primary_Sec']].sum()
st.title('Comparision of (Primary with Upper Primary) and (Primary with Upper Primary Seccondary) in Percentage of schools with Water Facility over 2013 to 2016')
st.bar_chart(Data3)

Data4=df.groupby('Year')[['Primary_with_U_Primary_Sec_HrSec','U_Primary_With_Sec_HrSec']].sum()
st.title('Comparision of (Primary with Upper Primary and Secondary and HrSecondary) and (Upper Primary With Secondary and HrSecondary) Percentage of schools with Water Facility over 2013 to 2016')
st.bar_chart(Data4)

Data5=df.groupby('Year')[['U_Primary_With_Sec','Sec_with_HrSec.']].sum()
st.title('Comparision of (Upper Primary With Secondary) and (Secondary with HrSecondary) in Percentage of schools with Water Facility over 2013 to 2016')
st.bar_chart(Data5)































