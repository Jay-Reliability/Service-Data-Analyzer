import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Streamlit 페이지 기본 레이아웃을 wide로 설정
st.set_page_config(
    page_title="SVC Data Pro-Analyzer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 상단 여백 및 기본 패딩 제거용 CSS 주입
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {
            display: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML 파일 로드 및 렌더링
html_file_path = Path(__file__).parent / "02_SVC_Pro_Analyzer_Final.html"

if html_file_path.exists():
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    # 뷰포트 높이 100vh에 맞춰 렌더링 (scrolling 활성화)
    components.html(html_code, height=960, scrolling=True)
else:
    st.error("02_SVC_Pro_Analyzer_Final.html 파일을 찾을 수 없습니다.")