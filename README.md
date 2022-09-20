![header](https://capsule-render.vercel.app/api?type=waving&text=project_ted&animation=fadeIn&color=timeGradient&fontSize=50&height=180 )

</br>

## 개요
- Streamlit을 위한 파이썬 가상환경을 만들어 웹 서비스 제공
- 전 세계적으로 유명한 Ted는 사람들에게 유익한 강의를 제공하는 강의 플랫폼입니다. 최초 테드 강의가 있는 시점부터 2022년 상반기까지, 어떤 타이틀에, 기간에 사람들이 더 많이 시청하고, 추천을 누르는지 분석을 하였습니다.

</br>

- 하기 분류에 따라 데이터를 분석 및 정리하였고, 유저가 직접 검색을 하여 더 상세한 정보를 참고할 수 있도록 검색 기능도 탑재하였습니다. 
  - Home: 전체적인 개요 설명
  - Top Ted 강연: Top/좋아요/조회수를 기준으로 데이터셋을 나타냈음.
  - 연사별 강연내용: 각 연사별로 어떤 강연을 했는지, 몇개나 했는지에 대한 데이터 정리
  - 강연 타이틀 분석: Wordcloud를 이용하여, 어느 키워드가 많이 쓰였는지 정리
  - Ted 강연 빈도수: 각 연도별/월별로 강연이 얼마나 있는지에 대한 정리
  - 데이터간 관계 분석: 좋아요/조회수의 관계 정리

</br>

- 데이터 셋의 출처는:
- 미국의 익명 직장 및 상사 평가 사이트인 글래스도어이며, Data Analyst에 관련한 모집공고의 데이터입니다.
- 데이터 출처: https://www.kaggle.com/datasets/ashishjangra27/ted-talks?select=data.csv
- 결과물: www.ec2-3-34-129-145.ap-northeast-2.compute.amazonaws.com:8504/

</br>

- Word Cloud를 이용하여 기간/조회수/좋아요별로 많이 사용된 키워드를 시각적으로 나타냈습니다. 
5,440개의 데이터에서 분석하였습니다.
- **AWS** 
  AWS EC2에서 보안(방화벽) 항목에서 포트 허용 작업을 했습니다.
  백그라운드로 실행 설정을 하였습니다: 

`$ nohup streamlit run app.py &`

</br>

</br>

## 사전 데이터 가공

- 가공 전 데이터: (5440 x 6)
- 원본 컬럼명은 각 title, author, date, view, likes, link입니다.
- index를 추가하였고, 년/월로 분리, 좋아요와 조회수 비율 컬럼을 python의 pandas로추가했습니다.
- 가공 후 데이터: (5440 x 8)

</br>

</br>

## 발생 이슈

1. WordCloud의 기능을 사용하여, 단어를 정리하였으나, 여러 WordCloud의 사용으로 로딩이 과부하 되는 것을 방지하여, 사전에 Jupyter Notebook으로 처리하고, 해당 코드는 주석 처리를 하였습니다. 해당 프로젝트에서는 이미지로 표시하였습니다.
2. 최근 데이터까지 있으나, 2022년는 현재 상반기까지 표시되므로, 연도별로 <Ted 강연 빈도수>를 볼 때, 2022년에에 곡선 그래프가 급격히 하락합니다. 해당 그래프 상단에 추가 보충 설명을 하였습니다. 

</br>

</br>



## 작업 환경

- 언어: Python
- 개발 환경: Anaconda, Visual Studio Code, AWS
- 라이브러리 및 프레임워크: pandas, streamlit, image, matplotlib, plotply, seaborn, WordCloud

</br>

</br>

* - 블로그 : https://yeo0616.tistory.com/



</br>

</br>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=100&section=footer)
