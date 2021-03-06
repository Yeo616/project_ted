import streamlit as st
import webbrowser
from PIL import Image
from app_analizing import run_analizing
from app_speechers import run_speechers
from app_title import run_title
from app_top import run_top
from app_year import run_year

def main():


    menu = ['Home', 'Top Ted 강연', '연사별 강연내용', '강연 타이틀 분석', 'Ted 강연 빈도수' ,'데이터간 관계 분석']
    choice = st.sidebar.radio('메뉴 선택',menu)
    
    col1,col2,col3 = st.columns([2,1,1])
    with col1:
        st.subheader("Ted 관련 데이터 분석")
    
    with col3:
        if st.button('Ted 페이지로 이동'):
            url = 'https://www.ted.com/'
            webbrowser.open_new_tab(url)


  
    if choice == menu[0]:
        

        url1 = 'https://media-exp1.licdn.com/dms/image/C4D1BAQGRCL25mnKg7g/company-background_10000/0/1519798430700?e=2147483647&v=beta&t=K82J81Djn2IRUlHASTPsclcw3qdZd-w10ZeRTv5Z7NY'
        st.image(url1)

        with st.expander('데이터 컬럼 설명'):
            st.write('- TItle: 타이틀')
            st.write('- author: 연사')
            st.write('- views: 조회수')
            st.write('- likes: 좋아요')
            st.write('- link: 링크')
            st.write('- year: 강연 연도')
            st.write('- month: 강연달')
  
        st.markdown('****')

        st.write('출처: Ted.com')
        st.write('취지:ted 관련 데이터 셋으로 연도별 강연 빈도수, 연사별, 강연 타이틀 분석  ')
        st.write('총 데이터 개수: 5440')





    elif choice == menu[1]:
        run_top()
    elif choice == menu[2]:
        col1,col2,col3 = st.columns(3)
        with col1:
            st.image('https://sopadehormigas.files.wordpress.com/2013/09/stanton.jpg')
        with col2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjL0bIeHHcJ1qfqYqwQGeOYBjMUtjH2vw0UMZR3pyfhm1btL5fBWp0Oz6QNup6IQuM1RM&usqp=CAU')
        with col3:
            st.image('data:image/jpeg;base64,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')
        st.markdown('****')
        run_speechers()
    elif choice == menu[3]:
        run_title()
    elif choice == menu[4]:
        st.image('https://cdn.mos.cms.futurecdn.net/Xfwn3VUhmDttDsxXmEqbw6.jpg')
  
        run_year()
    elif choice == menu[5]:
        st.image('https://helloendless.com/wp-content/uploads/2016/03/image00.jpg')
        st.markdown('****')
        run_analizing()

if __name__ == '__main__':
    main()