import requests

default_headers = {

}

class Axios:
  def __init__(self, url: str, customHeaders: dict = {}):
    self.headers: dict = default_headers.update(customHeaders)
    self.url: str = url

  def get(self, path: str = "/", params: dict = {}, **args):
    return requests.get(
      url = self.url + path,
      headers = self.headers,
      params = params,
    )

  def post(self, path: str = "/", data: dict = {}, **args):
    return requests.post(
      url = self.url + path,
      headers = self.headers,
      data = data,
    )

  def put(self, path: str = "/", data: dict = {}, **args):
    return requests.put(
      url = self.url + path,
      headers = self.headers,
      data = data,
    )

  def patch(self, path: str = "/", data: dict = {}, **args):
    return requests.patch(
      url = self.url + path,
      headers = self.headers,
      data = data,
    )

  def delete(self, path: str = "/", **args):
    return requests.delete(
      url = self.url + path,
      headers = self.headers,
    )

  def head(self, path: str = "/", **args):
    return requests.head(
      url = self.url + path,
      headers = self.headers,
    )