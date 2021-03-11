import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("Hello, world")

def createApp():
  return tornado.web.Application([
    (r"/", MainHandler),
  ])

#if __name__ == "__main__":
app = createApp()
app.listen(5000)
tornado.ioloop.IOLoop.current().start()