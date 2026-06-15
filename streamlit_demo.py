import streamlit
import time
streamlit.title('测试用例')
if 'count' not in streamlit.session_state:
        streamlit.session_state['count']=1
streamlit.divider()
prompt=streamlit.chat_input('请输入你的问题：')
if prompt:
    #我的想管你问题
    streamlit.chat_message('user').markdown(prompt)
    #ai的想关回答
    with streamlit.spinner('思考中...'):
        time.sleep(5) 
        streamlit.chat_message('assistant').markdown(f'我不会{streamlit.session_state['count']}')
        streamlit.session_state['count']+=1

