import pandas as pd
import streamlit as st
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image


def run_title():
    df = pd.read_csv('data/ted_data_modified.csv',index_col=0)

    my_stopwords = STOPWORDS
    my_stopwords.add('make')

    # 타이틀에서 가장 많이 쓰인 단어
    with st.expander('타이틀에서 가장 많이 쓰인 단어'):
        img = Image.open('data/title_total.png')
        st.image(img)

        # title_list = df['title'].to_list()
        # titles = ''.join(title_list)    
        # wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(titles)
    
        # fig1 = plt.figure()
        # plt.imshow(wc)
        # plt.axis('off')
        # plt.show()
        # st.pyplot(fig1)

    # 조회수 top100개에서 많이 쓰인 단어
    with st.expander('조회수 top100 타이틀에서 많이 쓰인 단어'):
        img = Image.open('data/title_views_top100.png')
        st.image(img)
 
    # with st.expander('조회수 top100 타이틀에서 가장 많이 쓰인 단어'):
    #     df_views_top100 = df.sort_values('views',ascending = False).head(100)

    #     title_views_list = df_views_top100['title'].to_list()
    #     views_titles = ''.join(title_views_list)
    #     wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(views_titles)
 
    #     fig2 = plt.figure()
    #     plt.imshow(wc)
    #     plt.axis('off')
    #     plt.show()
    #     st.pyplot(fig2)
    
    # 조회수 top500개에서 많이 쓰인 단어
    with st.expander('조회수 top500 타이틀에서 많이 쓰인 단어'):
        img = Image.open('data/title_views_top500.png')
        st.image(img)

    # with st.expander('조회수 top500 타이틀에서 가장 많이 쓰인 단어'):
    #     df_views_top500 = df.sort_values('views',ascending = False).head(500)

    #     title_views500_list = df_views_top500['title'].to_list()
    #     views_titles500 = ''.join(title_views500_list)
    #     wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(views_titles500)
 
    #     fig3 = plt.figure()
    #     plt.imshow(wc)
    #     plt.axis('off')
    #     plt.show()
    #     st.pyplot(fig3)

    # 좋아요 top100개에서 많이 쓰인 단어
    with st.expander('좋아요 top100 타이틀에서 많이 쓰인 단어'):
        img = Image.open('data/title_likes_top100.png')
        st.image(img)

    # with st.expander('좋아요 top100 타이틀에서 가장 많이 쓰인 단어'):
    #     df_likes_top100 = df.sort_values('likes',ascending = False).head(100)

    #     title_likes_list = df_likes_top100['title'].to_list()
    #     likes_titles = ''.join(title_likes_list)
    #     wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(likes_titles)
 
    #     fig4 = plt.figure()
    #     plt.imshow(wc)
    #     plt.axis('off')
    #     plt.show()
    #     st.pyplot(fig4)
    
    # 좋아요 top500개에서 많이 쓰인 단어
    with st.expander('좋아요 top500 타이틀에서 많이 쓰인 단어'):
        img = Image.open('data/title_likes_top500.png')
        st.image(img)

    # with st.expander('좋아요 top500 타이틀에서 가장 많이 쓰인 단어'):
    #     df_likes_top500 = df.sort_values('likes',ascending = False).head(500)

    #     title_likes500_list = df_likes_top500['title'].to_list()
    #     likes_titles500 = ''.join(title_likes500_list)
    #     wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(likes_titles500)
 
    #     fig5 = plt.figure()
    #     plt.imshow(wc)
    #     plt.axis('off')
    #     plt.show()
    #     st.pyplot(fig5)

   # 연도별 가장 많이 쓰인 단어
    year = sorted(df['year'].unique())
    year.sort(reverse=True)
    year_selected = st.selectbox('연도 선택', year)
    
    if year_selected is not None:

        df_year = df.loc[df['year']== year_selected,]
        title_year_list = df_year['title'].to_list()
        df_year_titles = ''.join(title_year_list)
        wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(df_year_titles)

        fig6 = plt.figure()
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        st.pyplot(fig6) 


    # 월별 가장 많이 쓰인 단어
    month = sorted(df['month'].unique())
    month_selected = st.selectbox('월 선택', month)
    
    if month_selected is not None:

        df_month = df.loc[df['month']== month_selected,]
        title_month_list = df_month['title'].to_list()
        df_month_titles = ''.join(title_month_list)
        wc = WordCloud(background_color= 'white', stopwords=my_stopwords).generate(df_month_titles)

        fig7 = plt.figure()
        plt.imshow(wc)
        plt.axis('off')
        plt.show()
        st.pyplot(fig7) 


