import streamlit as st
import ollama

# ===================== 【1】页面全局配置（美化核心） =====================
st.set_page_config(
    page_title="AI智能助手",
    page_icon="🤖",
    layout="wide",      # 宽屏布局
    initial_sidebar_state="collapsed"  # 收起侧边栏
)

# ===================== 【2】自定义CSS样式（大气美观） =====================
st.markdown("""
<style>
/* 全局背景 */
.stApp {
    background-color: #f8f9fa;
}
/* 标题样式 */
.main-title {
    text-align: center;
    font-size: 2.5rem;
    color: #2c3e50;
    margin-bottom: 20px;
    font-weight: 700;
}
/* 聊天气泡样式 */
.chat-message {
    padding: 15px;
    border-radius: 18px;
    margin-bottom: 10px;
    max-width: 75%;
}
/* 用户气泡（右侧 蓝色） */
.user-message {
    background-color: #007bff;
    color: white;
    margin-left: auto;
}
/* AI气泡（左侧 灰色） */
.assistant-message {
    background-color: #e9ecef;
    color: #2c3e50;
    margin-right: auto;
}
/* 输入框样式 */
.stChatInput {
    border-radius: 25px !important;
    padding: 10px 15px;
}
/* 分割线 */
.divider {
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# ===================== 【3】初始化AI连接 =====================
client = ollama.Client('http://localhost:11434')

# ===================== 【4】页面标题 =====================
st.markdown('<p class="main-title">🤖 AI智能对话助手</p>', unsafe_allow_html=True)

# ===================== 【5】初始化聊天记录 =====================
if 'message' not in st.session_state:
    st.session_state['message'] = []

# 清空聊天按钮
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🗑️ 清空聊天记录", use_container_width=True):
        st.session_state['message'] = []
        st.rerun()

st.divider()

# ===================== 【6】展示所有聊天记录（优化版，无重复渲染） =====================
for msg in st.session_state['message']:
    with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])

# ===================== 【7】聊天输入框 =====================
prompt = st.chat_input("请输入你的问题...")

# ===================== 【8】核心对话逻辑 =====================
if prompt:
    # 保存用户消息
    st.session_state['message'].append({"role": "user", "content": prompt})
    
    # 实时显示用户消息
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # AI思考加载动画
    with st.spinner("🧠 AI思考中..."):
        # 调用Ollama模型
        response = client.chat(
            model='deepseek-r1:7b',
            messages=st.session_state['message']  # 发送完整对话历史，支持上下文！
        )
        
        ai_reply = response['message']['content']
        
        # 保存AI回复
        st.session_state['message'].append({"role": "assistant", "content": ai_reply})
        
        # 显示AI回复
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(ai_reply)