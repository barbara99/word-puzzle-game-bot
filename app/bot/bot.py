import tornado.web
import json
from type_s import Update
from context import Context

class BotHandler(tornado.web.RequestHandler):
  def post(self):
    print('updates')
    update: Update = json.loads(self.request.body)
    context = Context(update)
    if context.event.isText:
      context.sendMessage(text=context.event.text)
    self.set_status(200)
    self.write("All Green!!!")

def Bot():
  return tornado.web.Application([
    (r'/webhook/telegram', BotHandler),
  ])