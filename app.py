import streamlit as st

st.markdown("# 앱 UI만들기")
st.markdown("---")
user_id = st.text_input("이름", placeholder="이름")



ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
tone = st.selectbox("반", ["1", "2", "3"])
features = st.multiselect("난이도", ["쉬움", "보통", "어려움",])
creativity = st.slider("AI의 창의성 수준을 설정하세요", 0, 100, 50)
ai_speed = st.select_slider("점수",options=["0", "25", "50", "75", "100"],value="50")

st.markdown("---")

