import streamlit as st
import pandas as pd
import seaborn as sb

def run_analizing():
    
    df = pd.read_csv('data/ted_data_modified.csv',index_col=0)
    # 좋아요/조회수 상관계수

    with st.expander('좋아요/조회수 관계'):
        
        st.text('1에 가까워질수록 관계 有，0에 가까워질수록 관계 없음')
        df_corr = df[['likes', 'views']].corr()
        st.dataframe(df_corr)

        fig1 = sb.pairplot(data = df[['likes', 'views']])
        st.pyplot(fig1)