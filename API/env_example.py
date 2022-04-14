import os
from dotenv import load_dotenv

load_dotenv('./.env')

key = "NAME"
result1 = os.environ[key]

result2 = os.environ.get(key, default=42)
result3 = os.getenv(key)

print()