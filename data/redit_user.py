from dotenv import load_dotenv
import os

class ReditUser:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv("REDDIT_USERNAME")
        self.password = os.getenv("REDDIT_PASSWORD")
