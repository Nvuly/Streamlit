### 필요한 라이브러리 임폴트
import streamlit as st

### sidebar 설치 + selectbox 추가
add_sidebar = st.sidebar.selectbox(
    '서울시 자전거 연도별 대여 및 반납건수',# 사이드바의 설명글
    ('2015년', '2016년', '2017년') #사이드바의 항목
)

add_sidebar2 = st.sidebar.selectbox(
    '서울시 자전거 연도별 대여 및 반납건수 시각화',
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
    if add.radio =='2015년':
        st.write('2015년의 서울시 자전거 대여건수')
    elif add_radio == '2016년':
        st.write('2016년의 서울시 자전거 대여건수')
    else:
        st.write('2017년의 서울시 자전거 대여건수')
# with 구문을 써줘야 본문이 아닌 사이드바에 출력된다. 
