import streamlit as st
import pandas as pd
from datetime import date, time
import os

# 파일 경로 설정
CSV_PATH = "submissions.csv"

# 1) 기존 submissions.csv 읽기 (없으면 빈 DataFrame)
if os.path.exists(CSV_PATH):
    df_sub = pd.read_csv(CSV_PATH)
else:
    df_sub = pd.DataFrame(columns=[
        "이름","학년","부스 종류","부스 설명","예산_min","예산_max",
        "디자인 색상","공연 장르","공연 제목","공연 일시","참여 인원","포스터 업로드"
    ])

# 페이지 설정
st.set_page_config(page_title="축제 아이디어 설문", layout="wide")
st.title("🎉 우리 학교 축제 아이디어 설문")
st.divider()

# — 여기에 사용자 입력 폼(텍스트, 셀렉트박스, 등) — 
# (생략: 이전 예제와 동일)

# 예시: 최소한의 입력
name = st.text_input("이름")
agree = st.checkbox("동의")
booth = st.selectbox("부스 종류", ["먹거리","놀이","기타"])
booth_desc = st.text_area("부스 설명")
budget = st.slider("예산", 0,50,(10,20))
genres = st.multiselect("공연 장르", ["댄스","음악","기타"])
perf_date = st.date_input("공연일", date.today())
perf_time = st.time_input("공연시간", time(18,0))
participants = st.number_input("참여 인원", 1,50,5)
poster = st.file_uploader("포스터 업로드", type=["png","jpg"])

# 5. 제출 버튼
if st.button("제출"):
    if not name or not agree:
        st.error("이름과 동의 체크가 필요합니다.")
    else:
        # 2) 새 제출 데이터를 dict 형태로 준비
        new = {
            "이름": name,
            "학년": "",              # 필요 시 추가
            "부스 종류": booth,
            "부스 설명": booth_desc,
            "예산_min": budget[0],
            "예산_max": budget[1],
            "디자인 색상": "",       # color_picker 사용 시 여기에
            "공연 장르": ",".join(genres),
            "공연 제목": "",         # perf_title
            "공연 일시": f"{perf_date} {perf_time}",
            "참여 인원": participants,
            "포스터 업로드": bool(poster)
        }
        # 3) 파일에 append
        pd.DataFrame([new]).to_csv(CSV_PATH, mode="a", header=not os.path.exists(CSV_PATH), index=False)
        st.success("제출 완료!")

        # 4) 최신 파일 다시 읽기
        df_sub = pd.read_csv(CSV_PATH)

# — 시각화 (파일에서 읽은 df_sub 사용) —
if not df_sub.empty:
    st.subheader("제출 내역")
    st.table(df_sub)

    st.subheader("부스 종류 분포")
    st.bar_chart(df_sub["부스 종류"].value_counts())
