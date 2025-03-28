import os
from dotenv import load_dotenv

load_dotenv()
MY_ENV_VAR = os.getenv('TOKEN')
print(MY_ENV_VAR)
