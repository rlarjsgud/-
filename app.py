import streamlit as st

st.markdown("# 앱 UI만들기")
st.markdown("---")
user_id = st.text_input("이름", placeholder="이름")



ai_model = st.radio("학년", ["1", "2", "3"], horizontal=True)
tone = st.selectbox("반", ["1", "2", "3"])

creativity = st.slider("난이도", 0, 50, 100)
ai_speed = st.select_slider("점수",options=["0", "25", "50", "75", "100"],value="50")

st.markdown("---")

