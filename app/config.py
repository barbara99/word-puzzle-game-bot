# load environment
import os
from dotenv import load_dotenv
load_dotenv()

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

config = {
  "telegram_token": os.getenv('TELEGRAM_TOKEN')
}