### 필요한 라이브러리 임폴트
import streamlit as st
import pandas as pd

### 제목 설정
st.header('공공 데이터 분석')

### 파일 업로드 기능 설정
uploaded_file = st.file_uploader('choose a file')
kdlfjjdkk
### 파일 업로드 후 결과를 생성할 코드 작성
if uploaded_file is not None : 
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame 생성')
    st.write(df)
    print('\n')
    st.subheader('요약 통계량 추출')
    stats = df.describe()
    st.write(stats)
else: 
    st.info('upload a csv file')