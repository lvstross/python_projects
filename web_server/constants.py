import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
VIEWS_DIR = os.getenv('VIEWS_DIR')
