# 1. 先导入并设置全局API Key（双重保险）
import dashscope
dashscope.api_key = "sk-3f0a28824057482bb68eee3e617bf263"

# 2. 导入LangChain组件
from langchain_community.llms import Tongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 3. 初始化模型，必须传入dashscope_api_key参数！
llm = Tongyi(
    model="qwen-turbo",  # 建议用turbo，更稳定
    dashscope_api_key="sk-3f0a28824057482bb68eee3e617bf263",
    temperature=0.7
)

# 4. 构建对话链
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个乐于助人的助手"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

# 5. 调用函数
def get_response(prompt_text):
    return chain.invoke({"input": prompt_text})

# 6. 主程序
if __name__ == "__main__":
    print("正在请求模型...")
    result = get_response("用Python代码输出1到10的数字")
    print("模型返回：\n", result)