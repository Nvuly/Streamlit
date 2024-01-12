### 필요한 라이브러리 임폴트
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np
#--------------------

### 데이터로드
df = pd.read_csv('iris_dataset.csv')

## 제목 설정
st.header('graph generation')


### Layout 설정
col1, col2 = st.columns(2)

### plt.subplots() 함수 실행

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


### col1 --> 그래프 생성
with col1:
    # sns.histplot() 실행
    st.subheader('label 컬럼에 대한 countplot')
    sns.countplot(data=df, x='label', ax=ax1)
    st.pyplot(fig1)


## col2 --> 그래프 생성
with col2:
    # sns.scatterplot() 실행
    st.subheader('정답 예측에 대한 컬럼의 중요도')
    sns.scatterplot(data=df, x='petal length (cm)', y='petal width (cm)', hue='label', ax=ax2)
    st.pyplot(fig2)
    
    
    
















