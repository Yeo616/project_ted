import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_year():
    df = pd.read_csv('data/ted_data_modified.csv',index_col=0)
    
    # 연도별 강의 보는 법
    year = sorted(df['year'].unique())
    year.sort(reverse = True)
    year_selected = st.selectbox('연도 선택', year)
    
    if year_selected is not None:
        df_year = df.loc[df['year']== year_selected,].sort_values('views',ascending = False)
        st.dataframe(df_year)

    # 월별 강의 보는 법
    month = sorted(df['month'].unique())
    month_selected = st.selectbox('연도 선택', month)
        
    if month_selected is not None:

        df_month = df.loc[df['month']== month_selected,].sort_values('views',ascending = False)
        st.dataframe(df_month)


       