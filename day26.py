import streamlit as st
import requests
import json

### 제목 설정
st.title('Api App')

### 호출 url
url = "http://data4library.kr/api/loanItemSrch?authKey=9494e177e6cd7818fd4e14985c2fd81ab25eebcdc3d740243b34b9ee37f443a4&startDt=2023-01-01&endDt=2023-05-31&age=20&format=json"

### 호출 url을 통해서 도서관 정보나루 사이트로부터 20대 인기 대출 도서 요청 & 결과 
response = requests.get(url)

### .text 변수 --> 전달받은 데이터 저장
data = response.text

### API 호출을 통해서 획득한 json 문자열 데이터 --> python dict 자료형으로 변환
api_dict = json.loads(data)

### 결과 출력

## layer 설정 --> 2개의 컬럼 생성 
col1, col2 = st.columns(2)

## col1 설정
with col1:
    with st.expander('api 호출 결과'):
        st.write(data)

with col2:
    with st.expander('api 호출 결과 변환'):
        st.write(api_dict)

