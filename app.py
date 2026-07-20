import streamlit as st

st.markdown("# AI 챗봇 만들기")
st.markdown("---")
st.markdown("## 질문을 하시면 AI 친구가 응답합니다.")
st.header("1. 기본 정보 입력")
user_id = st.text_input("아이디(ID)를 입력하세요", placeholder="example_user")
age = st.number_input("나이를 입력하세요", min_value=1, max_value=100, value=17)
question = st.text_area("AI에게 보낼 질문을 입력하세요", placeholder="여기에 질문을 작성해 주세요.")

st.header("2. 챗봇 설정")
ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
tone = st.selectbox("반", ["1", "2", "3"])
features = st.multiselect("난이도", ["쉬움", "보통", "어려움",])
creativity = st.slider("AI의 창의성 수준을 설정하세요", 0, 100, 50)
ai_speed = st.select_slider("점수",options=["0", "25", "50", "75", "100"],value="50")

st.markdown("---")

