import streamlit as st

from openai import OpenAI
ai_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'motto_updated' not in st.session_state:
    st.session_state.motto_updated = False

def add_todo():
    task = st.session_state.todo_input
    if task:
        st.session_state.todo_list.append([task, False])
        st.toast("할 일이 추가되었습니다!")
        st.session_state.todo_input = ""

@st.dialog("오늘의 다짐 수정")
def edit_motto():
    motto = st.text_input("나의 한 줄 좌우명을 적어주세요.")
    if st.button("다짐 저장"):
        st.session_state.user_motto = motto
        st.session_state.motto_updated = True
        st.rerun()

def page_todo():
    st.header("외울단어")
    new_todo = st.text_input("외울단어를 입력하세요", key="todo_input")
    st.button("추가하기", on_click=add_todo)
    if new_todo == "":
        st.warning("외울단어를 입력하고 버튼을 눌러주세요!")
    
    st.markdown("---")
    for i in range(len(st.session_state.todo_list)):
        col_task, col_btn, col_status = st.columns([4, 1, 1])
        with col_task:
            st.write(f"{i+1}. {st.session_state.todo_list[i][0]}")
        with col_btn:
            if st.button("완료", key=f"btn_{i}"):
                st.session_state.todo_list[i][1] = True
                st.rerun()
        with col_status:
            if st.session_state.todo_list[i][1]:
                st.write("✅ **달성!**")
    st.markdown("---")

def page_report():
    st.header("단어")
    if not st.session_state.todo_list:
        st.write("아직 등록된 단어가 없습니다.")
    else:
        total = len(st.session_state.todo_list)
        count = 0
        for item in st.session_state.todo_list:
            if item[1] == True:
                count += 1
        progress = (count / total) * 100
        st.metric("오늘의 달성률", f"{progress:.1f}%")
        st.progress(progress / 100)
        if progress == 100:
            st.balloons()
            st.success("모든 목표를 달성하셨습니다! 🏆")
        if st.button("기록 전체 초기화"):
            st.session_state.todo_list = []
            st.rerun()

def page_ai_coach():
    st.header("🧐 AI 코치와 대화하기")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "너는 사용자의 영어단어 암기를 도와주는 사람이야 잘 설명하고 도와줘야"}
        ]
        
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
    question = st.chat_input("질문을 입력하세요")
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
        with st.chat_message("assistant"):
            status_context = f"현재 나의 단어암기 달성 여부: {st.session_state.todo_list}"
            prompt = st.session_state.messages + [{"role": "system", "content": status_context}]
            with st.spinner("내가 생각 중...🤔"):
                response = ai_client.chat.completions.create(
                    model="gpt-5.4-mini",
                    messages=prompt)
                ai_response = response.choices[0].message.content
                st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

pg = st.navigation([
    st.Page(page_todo, title="모르는 단어", icon="✅"),
    st.Page(page_report, title="외울 단어", icon="📈"),
    st.Page(page_ai_coach, title="단어들", icon="🧐")], position="top")

st.title("단어 암기")
pg.run()
