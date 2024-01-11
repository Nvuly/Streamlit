### 필요한 라이브러리 임폴트
import streamlit as st
import pandas as pd

### sidebar 설치 + selectbox 추가
add_sidebar = st.sidebar.selectbox(
    'Favorite food?',
    ('Apple', 'Banana', 'Pop corn')    
)

### selecbox 선택에 따른 텍스트 출력
if add_sidebar == 'Apple':
    st.write('YOU CHOOSE APPLE!')
elif add_sidebar == 'Banana':
    st.write('YOU CHOOSE BANANA!')
else:
    st.write('YOU CHOOSE POP CORN!')