import streamlit as st
import time
st.title('测试标题')
st.write('你好itheima')
st.divider()
name=st.chat_input('请输入你的名字：')
if name: 
     st.write(F'你好{name}')
     #等待提示框
with st.spinner('思考中'):
     time.sleep(5)
     st.write('思考完成')
#消息容器
#角色包括：user,assistant,huamn,ai
st.chat_message('user').markdown('你是谁')
st.chat_message('assistant').markdown('我是黑马聊天机器人')
