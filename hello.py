# from langchain import PromptTemplate, LLMChain
# from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
import os

load_dotenv()   

print(os.getenv('name'))
print(os.getenv('age'))
