# load environment
import os
from dotenv import load_dotenv
from axios import Axios
import logging

# load .env
load_dotenv()

# configure logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# expose .env so linting can pick up
Config = {
  'port': os.getenv('PORT'),
  'telegram_token': os.getenv('TELEGRAM_TOKEN'),
  'webhook_url': os.getenv('WEBHOOK_URL'),
}

# setup function
def setup():
  try:
    assasin = Axios(
      url = 'https://api.telegram.org/bot{token}'.format(token=Config['telegram_token']),
      customHeaders = {}
    )
    res = assasin.get(path='/setWebhook', params={'url': Config['webhook_url']})
    print(res.status_code)
    print(res.json())
  except err:
    print(err)