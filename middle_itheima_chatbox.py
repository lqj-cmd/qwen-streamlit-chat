import streamlit as st
import ollama
import time 
client=ollama.Client(host='http://localhost:11434')
st.title('智能机器人')
if 'message' not in  st.session_state:
        st.session_state['message']=[]
st.divider()
prompt=st.chat_input('请输入问题:')
if prompt:
    st.session_state['message'].append({'role':'user','content':prompt})
    for  message in st.session_state['message']:
          st.chat_message(message['role']).markdown(message['content'])
    with st.spinner('思考中...'):
          time.sleep(1)
          response=client.chat(
                model='deepseek-r1:7b',
                messages=[{'role':'user','content':prompt}]
                               )
          st.session_state['message'].append({'role':'assistant','content':response['message']['content']})
          st.chat_message('assistant').markdown(response['message']['content'])

