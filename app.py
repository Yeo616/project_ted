import streamlit as st
import webbrowser
from PIL import Image
from app_analizing import run_analizing
from app_speechers import run_speechers
from app_title import run_title
from app_top import run_top
from app_year import run_year

def main():


    menu = ['Home', 'Top Ted 강연', '연사별 강의내용', '강의 타이틀 분석', 'Ted 강연 빈도수' ,'데이터 추가 분석']
    choice = st.sidebar.radio('메뉴 선택',menu)
    
    col1,col2,col3 = st.columns([2,1,1])
    with col1:
        st.subheader("Ted 관련 데이터 분석")
    
    with col3:
        if st.button('Ted 페이지로 이동'):
            webbrowser.open_new_tab(url)

 
    
    if choice == menu[0]:
        

        url = 'https://media-exp1.licdn.com/dms/image/C4D1BAQGRCL25mnKg7g/company-background_10000/0/1519798430700?e=2147483647&v=beta&t=K82J81Djn2IRUlHASTPsclcw3qdZd-w10ZeRTv5Z7NY'
        st.image(url)

        
        st.markdown('****')

        st.write('출처: Ted.com')
        st.write('목적: 인기 ted 듣고싶은 사람, 키워드 검색')
        st.write('총 데이터 개수: 5440')

        url = 'https://www.ted.com/'



    elif choice == menu[1]:
        run_top()
    elif choice == menu[2]:
        run_speechers()
    elif choice == menu[3]:
        run_title()
    elif choice == menu[4]:
        run_year()
    elif choice == menu[5]:
        run_analizing()

if __name__ == '__main__':
    main()