import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="김나윤 프로필",
    page_icon="👋",
    layout="centered"
)

# 프로필 상단 영역 (이미지와 인적사항 배치)
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    
    # 사진이 없다면 깔끔한 아이콘이나 아바타 대체
    st.markdown("### 🧑‍💻")

with col2:
    st.markdown("## 김나윤")
    st.markdown("바이오메디컬공학부 / 화학과 (복수전공)")
    st.markdown("한국외국어대학교") 
st.divider()

# 관심 분야 섹션 (PDF 스타일 반영)
st.subheader("Research Interests")
interests = [
    "인공지능 (AI)",
    "신약 개발 및 표적 발굴",
    "바이오 인포메틱스",
    "데이터 마이닝"
]

for interest in interests:
    st.markdown(f"- {interest}")

st.divider()

# 연구 경험 또는 주요 활동 섹션 (PDF 7페이지 참고)
st.subheader("Research Experience")
st.markdown("- **인공지능 및 바이오 연구 관심**")
st.markdown("- 파이썬 및 딥러닝 기반 데이터 분석")

# 하단 저작권 표시
st.divider()
st.caption("© 2026 Nayoon Kim. All rights reserved.")
