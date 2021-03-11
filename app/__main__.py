from config import config
from axios import Axios

assasin = Axios(
  url = "https://api.telegram.org/bot{token}".format(token=config["telegram_token"]),
  customHeaders = {}
)

res = assasin.get(path="/setWebhook")
print(res)
print(res.json())

import api
#from session import Session
#from context import Context
#from event import Event
#from handler import Handler

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world")

def createApp():
  return tornado.web.Application([
    (r"/", MainHandler),
  ])

if __name__ == "__main__":
  app = createApp()
  app.listen(5000)
  tornado.ioloop.IOLoop.current().start()