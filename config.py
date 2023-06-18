import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

IP = os.getenv('IP')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')
