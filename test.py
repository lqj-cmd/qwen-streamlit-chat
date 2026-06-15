import ollama
import streamlit

print(f"我现在可以用的模型: {ollama.list()}")
print(f"streamlit的版本是: {streamlit.__version__}")
client=ollama.client('http://localhost:11434')
