import streamlit as st

st.title("카운터 앱")

if 'count' not in st.session_state:
    st.session_state.count = 2

if st.button("증가"):
    st.session_state.count += int(st.session_state.count)*2

st.markdown(f"## 현재 숫자: {st.session_state.count}")
