import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, time, datetime
st.set_page_config(page_title="🎛️ Streamlit 위젯 종합 데모", layout="wide")

def main():
    #제목과 텍스트트
    st.title("Streamlit-MH")
    st.write("This is a simple streamlit app")

    #버튼
    st.header("st.button")
    if st.button("인사하기"):
        st.write("안녕하세요.")
    else:
        st.write("잘가세요.")

    #슬라이더
    age = st.slider("나이", 0, 100, 25)
    st.write(f"나이: {age}")

    
    st.title("🎛️ Streamlit 위젯 종합 데모 (2025-05)")

    # 01. text_input ────────────────────────────────────────────────────────────────
    st.header("1) st.text_input — 한 줄 텍스트")
    name = st.text_input("이름을 입력하세요", placeholder="홍길동")
    if name:
        st.success(f"반가워요, **{name}** 님!")

    # 02. text_area ─────────────────────────────────────────────────────────────────
    st.header("2) st.text_area — 여러 줄 메모")
    memo = st.text_area("아이디어를 3줄 이내로 적어 주세요", height=120, max_chars=90)
    st.write("▶ 입력 내용:", memo if memo else "_아직 입력 없음_")

    # 03. number_input ─────────────────────────────────────────────────────────────
    st.header("3) st.number_input — 숫자 스피너")
    age = st.number_input("나이", min_value=14, max_value=25, value=17, step=1)
    st.write("내년 나이:", age + 1)

    # 04. date_input ───────────────────────────────────────────────────────────────
    st.header("4) st.date_input — 달력")
    visiting_day = st.date_input("희망 방문 날짜", value=date.today())
    st.write("선택 ▶", visiting_day.strftime("%Y-%m-%d"))

    # 05. time_input ───────────────────────────────────────────────────────────────
    st.header("5) st.time_input — 시간 피커")
    visiting_time = st.time_input("입장 희망 시각", value=time(18, 30))
    st.write("선택 ▶", visiting_time.strftime("%H:%M"))

    # 06. slider ───────────────────────────────────────────────────────────────────
    st.header("6) st.slider — 연속값 슬라이더")
    budget = st.slider("예산(만원)", 0, 200, value=50, step=10)
    st.metric("선택 예산", f"{budget} 만원")

    # 07. select_slider ────────────────────────────────────────────────────────────
    st.header("7) st.select_slider — 옵션 범위 슬라이더")
    start_t, end_t = st.select_slider(
        "부스 운영 시간",
        options=[time(h) for h in range(9, 19)],
        value=(time(10), time(17))
    )
    st.write("시작:", start_t, "종료:", end_t)

    # 08. checkbox ─────────────────────────────────────────────────────────────────
    st.header("8) st.checkbox — 체크박스")
    agree = st.checkbox("규정을 읽고 동의합니다")
    st.info("동의 완료 ✅" if agree else "동의가 필요합니다 🔒")

    # 09. toggle ───────────────────────────────────────────────────────────────────
    st.header("9) st.toggle — 스위치")
    dark = st.toggle("다크 모드")
    st.write("현재 모드:", "🌙 Dark" if dark else "☀️ Light")

    # 10. radio ────────────────────────────────────────────────────────────────────
    st.header("10) st.radio — 단일 선택 라디오")
    genre = st.radio("선호 장르", ["K-POP", "발라드", "힙합"], horizontal=True)
    st.write("선택 ▶", genre)

    # 11. selectbox ────────────────────────────────────────────────────────────────
    st.header("11) st.selectbox — 드롭다운")
    city = st.selectbox("수학여행 희망 도시", ["도쿄", "타이베이", "싱가포르", "방콕"])
    st.write("당첨 도시:", city)

    # 12. multiselect ─────────────────────────────────────────────────────────────
    st.header("12) st.multiselect — 다중 선택")
    foods = st.multiselect(
        "축제 푸드트럭 메뉴 (복수 선택, 최대 3개)",
        ["떡볶이", "츄러스", "타코야키", "버블티"], max_selections=3
    )
    st.write("선택 메뉴:", foods)

    # 13. color_picker ────────────────────────────────────────────────────────────
    st.header("13) st.color_picker — 색상 선택")
    color = st.color_picker("배너 메인 색상", "#ff4b4b")
    st.markdown(
        f"<div style='width:100%;height:40px;border-radius:4px;background:{color}'></div>",
        unsafe_allow_html=True,
    )

    # 14. file_uploader ───────────────────────────────────────────────────────────
    st.header("14) st.file_uploader — 파일 업로드")
    file = st.file_uploader("포스터 이미지(PNG/JPG) 또는 PDF 기획서")
    if file:
        if file.type.startswith("image"):
            st.image(file, caption="업로드한 이미지", use_container_width=True)
        else:
            st.success(f"PDF '{file.name}' 업로드 완료!")

    # 15. camera_input ────────────────────────────────────────────────────────────
    st.header("15) st.camera_input — 웹캠 셀카")
    img = st.camera_input("셀카로 인증샷 남기기")
    if img:
        st.image(img, caption="🖼️ 저장된 셀카")

    # 16. form + form_submit_button ───────────────────────────────────────────────
    st.header("16) st.form — 위젯 묶음 & 제출")
    with st.form(key="vote_form"):
        nickname = st.text_input("닉네임")
        score = st.slider("오늘 기분 지수", 0, 100, 50)
        submit = st.form_submit_button("제출")
    if submit:
        st.success(f"{nickname} 님, 기분 {score}%로 접수되었습니다!")
        st.balloons()

    st.markdown("---")
    st.caption(
        f"마지막 업데이트 : {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"© 2025 Streamlit Widget Demo"
    )

    
# if __name__ == "__main__":
#     main()
