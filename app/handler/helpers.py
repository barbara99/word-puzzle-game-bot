import re

def isRegex(pattern: any) -> bool:
  try:
    re.compile(pattern)
    return True
  except:
    return False

def matchPattern(pattern: any, text: str) -> bool:
  if(isRegex(pattern)) {
    return pattern.test(text);
  }
  if(type(pattern) == 'str') {
    return pattern == text;
  }
  return False