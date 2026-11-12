import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="내 프로필",
    page_icon="👋",
    layout="centered"
)

# 헤더 영역
st.title("👋 안녕하세요!")
st.write("저의 프로필 페이지에 오신 것을 환영합니다.")

st.divider()

# 프로필 정보 카드 형태 혹은 컬럼으로 꾸미기
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지가 있다면 추가하거나 아이콘으로 대체할 수 있어요
    st.markdown("### 🧑‍💻")

with col2:
    st.subheader("김나윤")  # 필요에 따라 이름 수정
    st.markdown("**학교:** 대학교")  # 학교 이름 입력
    st.markdown("**전공:** 바이오메디컬공학부 / 화학과 (복수전공)")  # 전공 입력

st.divider()

# 관심 분야 섹션
st.subheader("💡 관심 분야")

# 태그처럼 보여주는 뱃지 형태나 리스트
interests = [
    "인공지능 (AI)",
    "신약 개발 및 표적 발굴",
    "바이오 인포메틱스",
    "데이터 마이닝"
]

for interest in interests:
    st.markdown(f"- {interest}")

# 추가적인 소개나 연락처를 넣고 싶다면 아래에 작성할 수 있어요
st.divider()
st.caption("© 2026 Nayoon Kim. All rights reserved.")