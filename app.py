import streamlit as st
import webbrowser
from app_analizing import run_analizing
from app_speechers import run_speechers
from app_title import run_title
from app_top import run_top

def main():
    st.header("Ted 관련 데이터 분석")
    st.subheader('출처: Ted.com')
    st.text('목적: 인기 ted 듣고싶은 사람, 키워드 검색')
    st.text('총 데이터 개수: 5440')

    url = 'https://www.ted.com/'
    if st.button('Ted 페이지로 이동'):
        webbrowser.open_new_tab(url)

    st.text('-----------')

    menu = ['Home', 'Top Ted 강연', '연사별 강의내용', '강의 타이틀 분석', 'Ted 강연 빈도수' ,'데이터 추가 분석']
    choice = st.sidebar.selectbox('메뉴 선택',menu)
    if choice == menu[0]:
        pass
    elif choice == menu[1]:
        run_top()
    elif choice == menu[2]:
        run_speechers()
    elif choice == menu[3]:
        run_title()
    elif choice == menu[4]:
        pass
    elif choice == menu[5]:
        run_analizing()

if __name__ == '__main__':
    main()