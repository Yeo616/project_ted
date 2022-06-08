import streamlit as st
import pandas as pd

def run_speechers():
    st.subheader('연사별 강의내용 분류')
    st.write('연사마다 강의한 횟수 통계 데이터')

    df = pd.read_csv('data/ted_data_modified.csv', index_col=0)
    # 연사별 강의 수
    with st.expander('연사별 강의수'):
        df_author = df['author'].value_counts().to_frame()
        df_author.columns=['강의수']
        st.dataframe(df_author)

    speechers = df_author.index
    choice = st.selectbox('연사 선택 (조회수 내림차수로 정렬)',speechers)

    df_best = df.loc[df['author'] == choice,].sort_values('views',ascending = False)
    st.dataframe(df_best)

    # 판다스 데이터프레임 변수명[컬럼명]. sort_values(컬럼명)
    