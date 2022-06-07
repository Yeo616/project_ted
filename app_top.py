import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# top ted 강연
def run_top():
    df = pd.read_csv('data/ted_data_modified.csv', index_col=0)
    st.image('https://cdn.mos.cms.futurecdn.net/Xfwn3VUhmDttDsxXmEqbw6-1200-80.jpg')
    st.markdown('****')

    # 조회수 기준 top 100
    with st.expander('조회수 기준 top 100'):
        df_views_top100 = df.sort_values('views',ascending = False).head(100)
        st.dataframe(df_views_top100)

    # 좋아요 기준 top 100
    with st.expander('좋아요 기준 top 100'):
        df_likes_top100 = df.sort_values('likes',ascending = False).head(100)
        st.dataframe(df_likes_top100)
    
    # 좋아요 제일 많이 받은 강의
    with st.expander('좋아요 제일 많이 받은 강의'):
        df_likes = df.loc[df['likes'] == df['likes'].max(),]
        st.dataframe(df_likes)

    # 조회수 제일 많이 받은 강의
    with st.expander('조회수 제일 많이 받은 강의'):
        df_view = df.loc[df['views'] == df['views'].max(),]
        st.dataframe(df_view)

    # 좋아요/조회수 가장 많이 받은 연사의 강의
    with st.expander('좋아요/조회수 가장 많이 받은 연사의 강의'):
        df_best = df.loc[df['author'] == 'Sir Ken Robinson',]
        st.dataframe(df_best)
        
    # 조회수 대비 좋아요 효율이 좋은 것
    with st.expander('조회수 대비 좋아요 효율이 좋은 강의'):
        df2 = pd.read_csv('data/ted_data_modified(likes,views).csv',index_col=0)
        df_likesviews = df2.sort_values(['likes/views(%)','views'],ascending = False)
        st.dataframe(df_likesviews.head(100))