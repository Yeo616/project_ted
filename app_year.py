import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_year():
    df = pd.read_csv('data/ted_data_modified.csv',index_col=0)
    
    url = 'https://pi.tedcdn.com/r/talkstar-photos.s3.amazonaws.com/uploads/20736b4f-91ec-4016-86e6-965bb944e07d/DickCarpenter_2019x-embed.jpg?quality=89&w=320'
    st.image(url)

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
    with st.expander('연도별 강의 빈도수(2022년은 현제 진행형)'):
        b = df['year'].value_counts().to_frame().reset_index().sort_values('index')
        b.columns = ['year','counts']

        fig1 = plt.figure()
        plt.plot(b['year'], b['counts'],'r--')
        plt.xlabel('year')
        plt.ylabel('ted_counts')
        plt.title('Yearly ted frequency')
        plt.show()
        st.pyplot(fig1)

    with st.expander('연도별 빈도 수치 확인'):
        b = df['year'].value_counts().to_frame().reset_index().sort_values('index')
        b.columns = ['year','counts']
        b = b.set_index('year')
        st.dataframe(b)

    # 월별 강의 빈도수
    with st.expander('월별 강의 빈도수'):
  
        a = df['month'].value_counts().to_frame().reset_index().sort_values('index')
        a.columns = ['month','counts']

        fig2 = plt.figure()
        plt.plot(a['month'], a['counts'],'r--')
        plt.xlabel('month')
        plt.xticks(range(1,13))
        plt.ylabel('ted_counts')
        plt.title('Monthly ted frequency')
        st.pyplot(fig2)

    with st.expander('월별 빈도 수치 확인'):
        a = df['month'].value_counts().to_frame().reset_index().sort_values('index')
        a.columns = ['month','counts']
        a = a.set_index('month')
        st.dataframe(a)


       