# 💬 진실만 말하는 마이클 (Michael: The One-Liner Truth-Teller)

> **"모든 질문에 단 한 줄로 명쾌하게 대답하는 페르소나 챗봇 웹 애플리케이션"**

이 프로젝트는 **LangChain**과 **Streamlit**을 활용하여 구축된 대화형 AI 챗봇입니다. 사용자의 이전 대화 맥락을 기억하며 지정된 시스템 프롬프트(System Instruction)의 페르소나를 엄격하게 유지하는 것이 특징입니다.

---

## ✨ 핵심 기능 (Key Features)

* **페르소나 기반 대화 (Persona-based Chat):** '모든 질문에 단 한 줄로 대답하는 마이클'이라는 고유한 페르소나를 프롬프트 엔지니어링을 통해 구현했습니다.
* **대화 문맥 유지 (Context Memory):** Streamlit의 `session_state`와 LangChain의 `MessagesPlaceholder`를 결합하여 이전 대화 내역을 기억하고 자연스러운 연속 대화를 지원합니다.
* **직관적인 UI/UX:** Streamlit의 내장 Chat Elements(`st.chat_message`, `st.chat_input`)를 활용하여 사용자 친화적인 메신저 형태의 인터페이스를 제공합니다.

---

## 🛠 기술 스택 (Tech Stack)

* **Language:** Python 3.x
* **Framework / Library:**
  * `streamlit`: 웹 프론트엔드 UI 및 상태 관리
  * `langchain_core` / `langchain_upstage`: LLM 파이프라인(LCEL) 구축 및 프롬프트 관리
  * `python-dotenv`: API Key 등 환경변수 보안 관리
* **LLM (Language Model):** * `Upstage Solar (solar-pro2)`: 우수한 한국어 자연어 처리(NLP) 성능과 빠른 추론 속도를 자랑하는 모델을 도입하여, 사용자의 의도를 정확히 파악하고 지연 없는 매끄러운 대화 경험을 구현했습니다.

---

## 🚀 실행 방법 (Getting Started)

### 1. 저장소 클론 (Clone the repository)
```bash
git clone [https://github.com/본인아이디/저장소이름.git](https://github.com/본인아이디/저장소이름.git)
cd 저장소이름
```
2. 필수 패키지 설치 (Install dependencies)
```bash
pip install -r requirements.txt
(※ requirements.txt에는 streamlit, langchain-upstage, langchain-core, python-dotenv가 포함되어야 합니다.)
```

3. 환경 변수 설정 (Environment Setup)
프로젝트 최상단 디렉토리에 .env 파일을 생성하고 발급받은 API 키를 입력합니다.

```bash
UPSTAGE_API_KEY="본인의_UPSTAGE_API_KEY를_입력하세요"
```

4. 애플리케이션 실행 (Run the App)
```bash
streamlit run app.py
```

📂 폴더 구조 (Directory Structure)
```Plaintext
📦 project-root
 ┣ 📜 app.py             # Streamlit 메인 실행 파일 및 LLM 체인 로직
 ┣ 📜 .env               # 환경변수 파일 (Git에서 제외)
 ┣ 📜 .gitignore         # Git 추적 제외 목록
 ┗ 📜 README.md          # 프로젝트 설명 문서
```

💡 배운 점 (Lessons Learned)
LCEL(LangChain Expression Language) 활용: Prompt | LLM | OutputParser 형태의 직관적인 체인 구성을 통해 LLM 애플리케이션의 데이터 흐름을 설계하는 방법을 익혔습니다.

상태 관리(State Management): 웹 환경에서 사용자의 입력 및 모델의 응답 데이터를 휘발시키지 않고 세션에 저장하여(session_state) RAG 및 메모리 기능의 기초를 다졌습니다.

프롬프트 엔지니어링: 모델의 자유도를 제어하고 원하는 형식(길이, 톤앤매너)으로 출력을 제한하는 방법을 실습했습니다.

