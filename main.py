import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 URL (Google Drive 공유 링크 -> 다운로드 링크 형태)
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

# CSV 불러오기
df = pd.read_csv(url)

st.title("Google Drive CSV Plotly 시각화")

st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 숫자형 컬럼만 추출해서 y축 선택 옵션 제공
numeric_columns = df.select_dtypes(include='number').columns.tolist()
columns = df.columns.tolist()

x_axis = st.selectbox("X축 선택", options=columns)
y_axis = st.selectbox("Y축 선택", options=numeric_columns)

if x_axis and y_axis:
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig)
