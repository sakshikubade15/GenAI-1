from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)

response = llm.invoke("Who are you?")
print(response)