import streamlit as st

st.title("카운터 앱")
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button("증가"):
    st.session_state.count +=119298575778737372525948759437598437593759843759847598745943875492074912
st.markdown(f"## 현재 숫자: `{st.session_state.count}`")
