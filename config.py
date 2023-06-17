import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

IP = os.getenv('ip')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')
