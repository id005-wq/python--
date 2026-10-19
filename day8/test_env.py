import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("DEEPSEEK_API_KEY")
print("读到的 Key：", key)