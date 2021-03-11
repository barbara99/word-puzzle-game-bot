import tornado.web
import json
from event import Event
from context import Context

class BotHandler(tornado.web.RequestHandler):
  def post(self):
    print('updates')
    rawEvent = json.loads(self.request.body)
    transEvent = Event(rawEvent)
    print(transEvent.isChannelPost)
    self.write('Hello, world')

def Bot():
  return tornado.web.Application([
    (r'/webhook/telegram', BotHandler),
  ])