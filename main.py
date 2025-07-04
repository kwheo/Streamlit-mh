import streamlit as st
from datetime import date, time
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="축제 아이디어 설문", layout="wide")

# 1. 제목 및 설명
st.title("🎉 우리 학교 축제 부스 & 공연 아이디어 설문")
st.write("축제 부스 기획과 공연 아이디어를 함께 수집합니다. 아래 양식을 작성해 주세요.")
st.divider()

# 2. 기본 정보
st.header("1. 기본 정보")
name = st.text_input("• 이름을 입력하세요")
grade = st.selectbox("• 학년을 선택하세요", ["1학년", "2학년", "3학년"])
agree = st.checkbox("• 개인정보 수집 및 이용에 동의합니다")
st.divider()

# 3. 부스 아이디어
st.header("2. 부스 아이디어")
booth_types = ["먹거리", "놀이/게임", "전시", "체험", "기타"]
booth = st.selectbox("• 부스 종류 선택", booth_types)
if booth == "기타":
    booth = st.text_input("  - 기타 부스 아이디어를 입력하세요")

booth_desc = st.text_area("• 부스 아이디어 상세 설명", height=100)
budget = st.slider("• 예상 예산 (만원 단위)", 0, 100, (10, 30))
color = st.color_picker("• 부스 디자인 대표 색상 선택", "#FFD700")
st.divider()

# 4. 공연 아이디어
st.header("3. 공연 아이디어")
perf_genres = ["댄스", "밴드/음악", "마술", "퍼포먼스 아트", "기타"]
genres = st.multiselect("• 공연 장르 선택 (복수 선택 가능)", perf_genres)
if "기타" in genres:
    other = st.text_input("  - 기타 공연 장르를 입력하세요")
    genres = [g for g in genres if g != "기타"] + [other]

perf_title = st.text_input("• 공연 제목 제안")
perf_date = st.date_input("• 공연 희망 날짜", min_value=date.today())
perf_time = st.time_input("• 공연 희망 시간", value=time(18, 0))
participants = st.number_input("• 참여 인원 예상", min_value=1, max_value=50, value=5, step=1)
st.divider()

# 5. 홍보 자료 업로드
st.header("4. 홍보 자료 업로드 (선택)")
poster = st.file_uploader("• 부스/공연 홍보 포스터 이미지 업로드", type=["png","jpg"])
if poster:
    st.image(poster, caption="업로드된 포스터 미리보기", width=200)
st.divider()

# 6. 제출
st.header("5. 제출 및 요약")
submitted = st.button("✅ 아이디어 제출하기")

if submitted:
    if not name or not agree:
        st.error("이름 입력과 개인정보 동의가 필요합니다.")
    else:
        # 결과 요약 테이블
        result = {
            "이름": name,
            "학년": grade,
            "부스 종류": booth,
            "부스 설명": booth_desc,
            "예산(만원)": f"{budget[0]} ~ {budget[1]}",
            "디자인 색상": color,
            "공연 장르": ", ".join(genres),
            "공연 제목": perf_title,
            "공연 일시": f"{perf_date} {perf_time}",
            "참여 인원": participants,
            "포스터 업로드": "예" if poster else "아니오"
        }
        st.success("💡 아이디어가 제출되었습니다! 감사합니다.")
        st.table(pd.DataFrame([result]))
        # 다운로드 버튼
        df = pd.DataFrame([result])
        csv = df.to_csv(index=False).encode('utf-8-sig')
        st.download_button("결과 CSV로 다운로드", csv, file_name="idea_submission.csv", mime="text/csv")
