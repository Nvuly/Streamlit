### 필요한 라이브러리 임폴트
import pandas as pd
import numpy as np
import streamlit as st

### sidebar 설치 + selectbox 추가
add_sidebar = st.sidebar.selectbox(
    '서울시 자전거 연도별 대여건수',# 사이드바의 설명글
    ('2015년', '2016년', '2017년') #사이드바의 항목
)

add_sidebar2 = st.sidebar.selectbox(
    '서울시 자전거 연도별 반납건수 시각화',
    ('2015년', '2016년', '2017년')
)

### selectbox 선택에 따른 텍스트 출력
if add_sidebar == '2015년':
    st.write('2015년도의 서울시 자전거 대여 및 반납건수')
elif add_sidebar == '2016년':
    st.write('2016년도의 서울시 자전거 대여 및 반납건수')
else:
    st.write('2017년도의 서울시 자전거 대여 및 반납건수')

### with 구문 사용, sidebar + radio 버튼 추가
with st.sidebar:
    add_radio = st.radio(
        '연도별 대여건수',
        ('2015년', '2016년', '2017년')
    )
    if add_radio =='2015년':
        st.write('2015년의 서울시 자전거 대여건수')
    elif add_radio == '2016년':
        st.write('2016년의 서울시 자전거 대여건수')
    else:
        st.write('2017년의 서울시 자전거 대여건수')
# with 구문을 써줘야 본문이 아닌 사이드바에 출력된다. 


### layout 생성 --> 3칸 생성 --> 각 칸에 수치 정보 출력
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Temperature', value='70F', delta='1.2F')
with col2:
    st.metric(label='Wind', value='2m/s', delta='-8%')
with col3:
    st.metric(label='Humidity', value='86%', delta='4%')

print('\n') #웹상에서 한칸 뜬다



#### DataFrame 생성 및 출력

# 제목 생성

st.header('DataFrame 생성하기')

# DataFrame 생성

df = pd.read_csv('iris_dataset.csv')

# st.write(df) # 이렇게 해도 출럭이 되지만

# 버튼을 눌렀을 때 나오게 하고 싶다. 버튼을 만들면 됨

# 버튼을 생성해서 버튼을 클릭하면 --> if st.button():
### button 생성
if st.button('데이터프레임 생성'):
    st.write(df)


















  