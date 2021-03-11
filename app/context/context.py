import requests
from session import Session
from typing import Optional, Dict
from type_s import Media, Message
from axios import Axios
from config import Config

class Context:

  def __init__(self):
    self.session = Session()
    self.assasin = Axios(
      url = 'https://api.telegram.org/bot{token}'.format(token=Config['telegram_token']),
      customHeaders = {}
    )

  def sendMessage(self, text: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendPhoto(self, photo: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendAudio(self, audio: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendDocument(self, document: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendSticker (self, sticker: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendVideo (self, video: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendVoice (self, voice: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendVideoNote (self, videoNote: str, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendMediaGroup (self, media: Media, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendLocation (self, location: Location, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendVenue (self, venue: Venue, options: Optional[Dict[str, any]] = {}) -> None:
    pass

  def sendContact (self, contact: Contact, options: Optional[Dict] = {}) -> None:
    pass

  def sendChatAction(self, action: str) -> None:
    pass
