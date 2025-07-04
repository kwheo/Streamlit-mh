import streamlit as st
from datetime import datetime
from utils import append_response

st.title("📋 실시간 만족도 설문")
user = st.user or {"id": st.session_state.get("fallback_ip", "anon")}

with st.form("survey_form", clear_on_submit=True):
    grade = st.slider("강의 만족도 (1:불만족 ~ 5:매우만족)", 1, 5, 3)
    comment = st.text_area("추가 의견이 있다면 적어주세요")
    submitted = st.form_submit_button("제출")

if submitted:
    append_response({
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user["id"],
        "grade": grade,
        "comment": comment,
        "class_identifier": st.query_params.get("class", "A")
    })
    st.success("의견 감사합니다! 🎉")
