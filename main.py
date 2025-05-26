import pandas as pd
import plotly.express as px
import streamlit as st

# 데이터 불러오기
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

# 데이터 구조 확인
st.write("데이터 미리보기:")
st.dataframe(df.head())

# 예시: 시계열 데이터가 있다고 가정하고 시각화
if "date" in df.columns and "value" in df.columns:
    df["date"] = pd.to_datetime(df["date"])
    fig = px.line(df, x="date", y="value", title="시간에 따른 값 변화")
    st.plotly_chart(fig)
else:
    st.write("시각화할 적절한 열이 없습니다.")
