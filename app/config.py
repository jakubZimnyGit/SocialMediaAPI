from dotenv import load_dotenv
import os

load_dotenv()

class Settings():
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORYTHM = os.getenv("ALGORYTHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    DATABASE_URL = os.getenv("DATABASE_URL")