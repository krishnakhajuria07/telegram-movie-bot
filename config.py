import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URL = os.getenv("MONGO_URL")

SHORTIFY_KEY = os.getenv("SHORTIFY_KEY")
SHORTIFY_API = "https://shortify.in/api"

FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL")
