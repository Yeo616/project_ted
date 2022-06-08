import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_year():
    
    st.write('연도별로 있었던 강연 수 체크 데이터')

    st.markdown('****')
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
    month_selected = st.selectbox('월 선택', month)
        
    if month_selected is not None:

        df_month = df.loc[df['month']== month_selected,].sort_values('views',ascending = False)
        st.dataframe(df_month)

    # 연도별 빈도수
    st.text(' ')
    with st.expander('연도별 강연 빈도수 그래프'):
        st.write('(2022년은 현재 진행형)')

        b = df['year'].value_counts().to_frame().reset_index().sort_values('index')
        b.columns = ['year','counts']

        fig1 = plt.figure()
        plt.plot(b['year'], b['counts'],'r--')
        plt.xlabel('year')
        plt.ylabel('ted_counts')
        plt.title('Yearly ted frequency')
        plt.show()
        st.pyplot(fig1)

        

    with st.expander('연도별 강연 빈도 수치 데이터 테이블'):
        b = df['year'].value_counts().to_frame().reset_index().sort_values('index')
        b.columns = ['year','counts']
        b = b.set_index('year')
        st.dataframe(b)

    # 월별 강의 빈도수
    with st.expander('월별 강연 빈도 그래프 '):
  
        a = df['month'].value_counts().to_frame().reset_index().sort_values('index')
        a.columns = ['month','counts']

        fig2 = plt.figure()
        plt.plot(a['month'], a['counts'],'r--')
        plt.xlabel('month')
        plt.xticks(range(1,13))
        plt.ylabel('ted_counts')
        plt.title('Monthly ted frequency')
        st.pyplot(fig2)

    with st.expander('월별 강연 빈도 수치 데이터 테이블'):
        a = df['month'].value_counts().to_frame().reset_index().sort_values('index')
        a.columns = ['month','counts']
        a = a.set_index('month')
        st.dataframe(a)


       