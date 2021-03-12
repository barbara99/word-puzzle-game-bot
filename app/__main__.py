import os
from config import Config, setup
import tornado.ioloop
from bot import Bot

port: str = Config['port']

if __name__ == '__main__':
  setup()
  bot = Bot()
  bot.listen(port)
  print('Application started on {port}'.format(port = port))
  tornado.ioloop.IOLoop.current().start()