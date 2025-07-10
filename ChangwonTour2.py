import streamlit as st

# 1) 페이지 설정
st.set_page_config(
    page_title="창원시 관광 안내",
    page_icon="🏙️",
    layout="wide"
)

# 2) 사이드바: 거리별 버튼 메뉴
st.sidebar.title("📍 창원시 거리 메뉴")

# 거리 → 명소 매핑
streets = {
    "중앙대로": ["용지호수공원", "창원시청", "경남도청"],
    "상남대로": ["상남시장", "창원컨벤션센터", "창원중부경찰서"],
    "팔용산길": ["팔용산 등산로", "팔용산 케이블카", "성주사"],
    "반송로": ["반송저수지", "반송전통시장"]
}

# 초기 선택값 세팅
if "selected_street" not in st.session_state:
    st.session_state.selected_street = None

# 거리별 버튼 생성
for street in streets:
    if st.sidebar.button(street):
        st.session_state.selected_street = street

# 3) 선택된 거리의 명소 목록을 접이식(expander)으로 표시
if st.session_state.selected_street:
    title = st.session_state.selected_street
    with st.sidebar.expander(f"🏞️ {title} 주요 명소", expanded=True):
        for place in streets[title]:
            st.write(f"- {place}")

# 4) 메인 화면: 선택된 거리 소개
if st.session_state.selected_street:
    sel = st.session_state.selected_street
    st.title(f"🌆 {sel} 탐방")
    st.write(f"여기는 **{sel}** 지역입니다. 주요 명소를 아래에서 확인해 보세요.\n")

    # expander를 이용해 각 명소 상세정보 표시
    for place in streets[sel]:
        with st.expander(place):
            st.write(f"**{place}** 은(는) …에 위치하고 있으며, … 특징이 있습니다.")
            # 예: 이미지
            # st.image(f"images/{sel}/{place}.jpg", caption=place, use_column_width=True)

else:
    st.title("🌆 창원시 관광 안내에 오신 것을 환영합니다!")
    st.write("좌측 메뉴에서 거리를 클릭하면 해당 거리의 주요 명소 목록이 나타납니다.")

# 5) 푸터
st.markdown("---")
st.write("© 2025 Changwon Tourism Authority")