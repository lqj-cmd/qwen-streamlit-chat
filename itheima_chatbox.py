# 1. 导入需要用到的工具库
import streamlit as st  # 核心：做网页界面、聊天窗口
import time             # 延时工具（这里只是演示，实际可以删掉）
import ollama           # 核心：调用本地Ollama大模型（deepseek）

# 2. 创建Ollama客户端，连接本地运行的AI模型
# 本地Ollama默认地址就是 http://localhost:11434
client = ollama.Client('http://localhost:11434')

# 3. 设置网页的大标题（显示在页面最上方）
st.title('测试用例')

# 4. 初始化【永久存储的聊天记录容器】（重点！）
# 如果 st.session_state 里没有叫 message 的数据，就创建一个空列表
if 'message' not in st.session_state:
     st.session_state['message'] = []  # 空列表，用来存所有对话（用户+AI）

# 5. 画一条水平分割线，美化界面
st.divider()

# 6. 创建网页底部的【聊天输入框】
# 括号里是提示文字：请输入你的问题
prompt = st.chat_input(f'请输入你的问题')

# 7. 判断：用户是否在输入框里写了内容
# 只有用户输入文字并发送，prompt 才有值，这段代码才会执行
if prompt:
    # 8. 把用户说的话，保存到【永久聊天记录】里
    # 格式固定：字典，role=user（用户），content=用户输入的内容
    st.session_state['message'].append({"role": "user", "content": prompt})

    # 9. 循环遍历所有聊天记录，把历史消息显示在页面上
    # 每一条消息都是一个字典，message 是循环的每一条数据
    for message in st.session_state['message']:
        # 根据角色（用户/AI）显示对应的聊天气泡
        st.chat_message(message['role']).markdown(message['content'])

    # 10. 显示加载动画：Ai思考中...
    with st.spinner('Ai思考中...'):
        time.sleep(1)  # 延时1秒（模拟AI思考速度）
        
        # 11. 调用本地大模型，发送用户的问题，获取AI回复
        response = client.chat(
                  model='deepseek-r1:7b',  # 指定用的模型名称
                  # 发送给AI的消息格式（固定要求）
                  messages=[{'role':'user','content':prompt}]
        )

        # 12. 把AI的回复，保存到【永久聊天记录】里
        # response['message']['content'] 是AI返回的回答文本
        st.session_state["message"].append({"role": "assistant", "content": response['message']['content']})
        
        # 13. 把AI的回复，显示在页面的聊天气泡里
        st.chat_message('assistant').markdown(response['message']['content'])
