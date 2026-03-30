from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

# 1. API 키 로드
load_dotenv()

st.title("진실만 말하는 마이클")

# 2. 세션 상태에 메시지 저장소 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. 프롬프트 설정: 대화 이력을 위한 MessagesPlaceholder 추가
system_instruction = "당신은 모든 질문을 단 한 줄로 대답하는 마이클입니다."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_instruction),
    MessagesPlaceholder("messages"), # 이전 대화들이 들어갈 자리
    ("human", "{input}")
])

# 4. 모델 및 체인 설정
llm = ChatUpstage(model="solar-pro2")
chain = prompt | llm | StrOutputParser()

# 5. 저장된 이전 대화 내용을 화면에 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. 사용자 입력 처리
if user_input := st.chat_input("무엇이든 물어보세요."):
    # 사용자 메시지를 세션에 저장 및 화면 표시 
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 마이클(AI)의 응답 생성 및 표시
    with st.chat_message("assistant"):
        # 대화 이력(st.session_state.messages)을 함께 전달하여 맥락 유지 
        response = chain.invoke({
            "input": user_input, 
            "messages": st.session_state.messages
        })
        st.markdown(response)
        
        # AI의 답변도 세션에 저장 
        st.session_state.messages.append({"role": "assistant", "content": response})
