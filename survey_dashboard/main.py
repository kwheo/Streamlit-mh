import streamlit as st
from pages import survey, analysis    # 각 파일에서 StreamlitPage 객체 반환
def main():
    selected = st.navigation([survey.page, analysis.page]).run()

if __name__ == "__main__":
    main()
