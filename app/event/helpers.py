
# checks if a dictionary has a key
def hasKey(obj: dict, key: str):
  return True if key in obj.keys() else False

class Object(dict):
  def __getattr__(self, key):
    try:
      return self[key]
    except KeyError as k:
      raise AttributeError(k)

  def __setattr__(self, key, value):
    self[key] = value

  def __delattr__(self, key):
    try:
      del self[key]
    except KeyError as k:
      raise AttributeError(k)

  def __repr__(self):
    return '<Object ' + dict.__repr__(self) + '>'
