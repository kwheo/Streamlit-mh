import streamlit as st
from datetime import datetime

st.set_page_config("창원시 관광 안내", "🏙️", layout="wide")

# 1) 데이터 정의
streets = {
    "중앙대로": {
        "용지호수공원": {
            "기본정보": "용지호수공원은 창원의 대표 휴식 공간으로, …",
            "사진": "images/중앙대로/용지호수공원.jpg",
            "지도": {"lat": 35.216, "lon": 128.681}
        },
        "창원시청": {
            "기본정보": "창원시청은 시민의 중심 행정 기관이며, …",
            "사진": "images/중앙대로/창원시청.jpg",
            "지도": {"lat": 35.217, "lon": 128.681}
        },
    },
    "상남대로": {
        "상남시장": {
            "기본정보": "상남시장은 50년 전통의 재래시장으로, …",
            "사진": "images/상남대로/상남시장.jpg",
            "지도": {"lat": 35.222, "lon": 128.681}
        },
        "창원컨벤션센터": {
            "기본정보": "대형 전시·컨퍼런스 시설이며, …",
            "사진": "images/상남대로/창원컨벤션센터.jpg",
            "지도": {"lat": 35.223, "lon": 128.685}
        },
    },
    # 필요한 만큼 거리와 명소를 추가하세요
}

# 2) 사이드바: 1단계 아코디언(거리 선택)
with st.sidebar.expander("🥾 1. 거리 선택", expanded=True):
    sel_street = st.radio(
        label="어느 거리를 둘러보시겠어요?",
        options=list(streets.keys()),
        key="sel_street"
    )

# 3) 사이드바: 2단계 아코디언(명소 선택) – 거리 선택 후
if st.session_state.get("sel_street"):
    with st.sidebar.expander("📍 2. 명소 선택", expanded=True):
        sel_place = st.radio(
            label=f"{st.session_state.sel_street}의 명소를 고르세요",
            options=list(streets[st.session_state.sel_street].keys()),
            key="sel_place"
        )
else:
    sel_place = None

# 4) 사이드바: 3단계 아코디언(메뉴 선택) – 명소 선택 후
if sel_place:
    with st.sidebar.expander("📖 3. 메뉴 선택", expanded=True):
        sel_detail = st.radio(
            label="보고 싶은 내용을 선택하세요",
            options=["기본정보", "사진", "지도"],
            key="sel_detail"
        )
else:
    sel_detail = None

# 5) 메인 화면 출력
st.markdown("---")
if sel_street and sel_place and sel_detail:
    # 헤더
    st.header(f"🌆 {sel_street} ▶ {sel_place} ▶ {sel_detail}")
    # 실제 데이터
    data = streets[sel_street][sel_place]

    if sel_detail == "기본정보":
        st.write(data["기본정보"])
    elif sel_detail == "사진":
        st.image(data["사진"], caption=sel_place, use_column_width=True)
    elif sel_detail == "지도":
        st.map({
            "lat": [data["지도"]["lat"]],
            "lon": [data["지도"]["lon"]]
        })

else:
    st.title("🌆 창원시 관광 안내에 오신 것을 환영합니다!")
    st.write("왼쪽 사이드바에서 1▶2▶3단계로 메뉴를 펼쳐가며\n"
             "관심 있는 거리를 선택해 보세요.")

# 6) 푸터
st.markdown("---")
st.write("© 2025 Changwon Tourism Authority")