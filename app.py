import streamlit as st

st.title("2의 제곱수 카운트")

if 'count' not in st.session_state:
    st.session_state.count = 2

if st.button("X2"):
    st.session_state.count += int(st.session_state.count)*1

if st.buttom("리셋"):
    st.session_state.count = 2
st.markdown(f"## 현재숫자: {st.session_state.count}")
