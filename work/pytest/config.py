from dotenv import load_dotenv
import os

load_dotenv('.env')

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
