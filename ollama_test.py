import ollama
#获得ollama的客户端对象
client=ollama.Client(host='http://localhost:11434')
#打印相关模型
'''print(client.list())
#运行相关模型，查看相关信息信息
print(client.show('deepseek-r1:7b'))
#查看运行模型有哪些在运行
print(client.ps())
#构建聊天框和模型进行对话
'''
while True:
          prompt=input('请输入内容：')
          response=client.chat(
                  model='deepseek-r1:7b',
                  messages=[{'role':'user','content':prompt}])
          #你发送请求的键名与ai键名不一样，ai键名是固定的
          print(response['message']['content'])