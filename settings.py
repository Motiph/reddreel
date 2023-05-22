import os
import logging

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", None)
SECRET = os.getenv("REDDIT_SECRET", None)
SUB_REDDIT = os.getenv("REDDIT_CLIENT_ID", None)
USERNAME = os.getenv("REDDIT_USERNAME", None)
PASSWORD = os.getenv("REDDIT_PASSWORD", None)
REDIRECT_URI = os.getenv("REDDIT_REDIRECT_URI", None)
USER_AGENT = os.getenv("REDDIT_USER_AGENT", None)
