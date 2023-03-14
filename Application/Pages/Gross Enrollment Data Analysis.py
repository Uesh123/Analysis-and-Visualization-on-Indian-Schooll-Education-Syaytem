import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

st.set_page_config(
    page_icon='📈',
    page_title="Gross Enrollment Data Analysis",
    layout='wide'
)

@st.cache
def load_data():
    df=pd.read_csv('C://Users//saroj//Documents//mini project//Application//Data//gross-enrollment-ratio-2013-2016.csv')
    country=df['State_UT'].unique()
    all_columns=df.columns.to_list()
    imputer=SimpleImputer(missing_values='NR', strategy='constant', fill_value=0)
    imp=SimpleImputer(missing_values='@', strategy='constant',fill_value=0)
    df=imputer.fit_transform(df)
    df=pd.DataFrame(imp.fit_transform(df),columns=all_columns)
    
    df[ 'Primary_Boys']=df[ 'Primary_Boys'].astype(np.float32)
    df['Primary_Girls']=df['Primary_Girls'].astype(np.float32)
    df['Upper_Primary_Boys']=df['Upper_Primary_Boys'].astype(np.float32)
    df['Upper_Primary_Girls']=df['Upper_Primary_Girls'].astype(np.float32)
    df['Secondary_Boys']=df['Secondary_Boys'].astype(np.float32)
    df['Secondary_Girls']=df['Secondary_Girls'].astype(np.float32)
    df['Higher_Secondary_Boys']=df['Higher_Secondary_Boys'].astype(np.float32)
    df['Higher_Secondary_Girls']=df['Higher_Secondary_Girls'].astype(np.float32)
        
    years=df['Year'].unique().tolist()
    return df

st.title('Gross Enrollment Ratio')
df = load_data()
st.dataframe(df,use_container_width=True)

data1=df.groupby('Year')[[ 'Primary_Boys','Primary_Girls']].sum()
st.title('Comparision of Primary Boys and Primary Girls of Gross Enrollment 2013 to 2016')
st.bar_chart(data1)

data2=df.groupby('Year')[['Upper_Primary_Boys','Upper_Primary_Girls']].sum()
st.title('Comparision of Upper Primary Boys and Upper Primary Girls of Gross Enrollment 2013 to 2016')
st.bar_chart(data2)

data3=df.groupby('Year')[[ 'Secondary_Boys','Secondary_Girls']].sum()
st.title('Comparision of Secondary Boys and Secondary Girls of Gross Enrollment 2013 to 2016')
st.bar_chart(data3)

data4=df.groupby('Year')[['Higher_Secondary_Boys','Higher_Secondary_Girls']].sum()
st.title('Comparision of Higher Secondary Boys and Higher Secondary Girls of Gross Enrollment 2013 to 2016')
st.bar_chart(data4)











