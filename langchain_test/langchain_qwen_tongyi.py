import streamlit as st
from langchain_community.llms import Tongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 配置
API_KEY = "sk-1c69fe1c01024a75bd1aae7d86f86146"

# 初始化模型
llm = Tongyi(
    model="qwen-turbo",
    dashscope_api_key=API_KEY,
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，回答简洁、准确、有用。"),
    ("user", "{input}")
])
chain = prompt | llm | StrOutputParser()

# ---------------------
# 界面
# ---------------------
st.title('智能机器人')
st.divider()

# 初始化聊天记录
if 'message' not in st.session_state:
    st.session_state['message'] = []

# 用户输入
prompt_text = st.chat_input('请输入问题：')

if prompt_text:
    # 1. 把用户消息加入历史
    st.session_state['message'].append({
        "role": "user",
        "content": prompt_text
    })

    # 2. AI 思考
    with st.spinner("思考中..."):
        response = chain.invoke({"input": prompt_text})

    # 3. 把AI回复加入历史
    st.session_state['message'].append({
        "role": "assistant",
        "content": response
    })

# ———— 最后统一显示所有消息（这才是正确位置！） ————
for message in st.session_state['message']:
    st.chat_message(message['role']).markdown(message['content'])