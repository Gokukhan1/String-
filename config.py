from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","21803165"))
API_HASH = getenv("API_HASH","05e5e695feb30e25bef47484cc006da7")

BOT_TOKEN = ""
OWNER_ID = int(getenv("OWNER_ID","7078181502"))

MONGO_DB_URI = getenv("mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN","PiratesMainchat")
