import streamlit as st
import pandas as pd
from utils import load_data

st.title("📊 실시간 결과 대시보드")
df = load_data()

if df.empty:
    st.info("아직 제출된 설문이 없습니다.")
    st.stop()

st.subheader("1) 만족도 분포")
st.bar_chart(df["grade"].value_counts().sort_index())

st.subheader("2) 평균 점수")
st.metric("평균", f"{df['grade'].mean():.2f} / 5")

st.subheader("3) 의견 모음")
st.dataframe(df[["timestamp", "user_id", "grade", "comment"]].sort_values("timestamp", ascending=False))
