import requests
from session import Session
from event import Event
from typing import Optional, Dict, Union, List
from type_s import Media, Location, Venue, Contact, Update
from axios import Axios
from config import Config


assasin = Axios(
  url = 'https://api.telegram.org/bot{token}'.format(token=Config['telegram_token']),
  customHeaders = {}
)

class Context:

  def __init__(self, update: Update) ->  None:
    self.event = Event(update)
    self.session = Session(session_id=self.event.chat['id'])
    self.state = self.session.state
    self.setState = self.session.setState
    self.resetState = self.session.resetState
    self.chatId: str | int = self.event.chat['id']

  def sendMessage(self, text: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendMessage",
      data={"chat_id": self.chatId, "text": text}
    )

  def sendPhoto(self, photo: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendPhoto",
      data={"chat_id": self.chatId, "photo": photo}
    )

  def sendAudio(self, audio: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendAudio",
      data={"chat_id": self.chatId, "audio": audio}
    )

  def sendDocument(self, document: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendDocument",
      data={"chat_id": self.chatId, "document": document}
    )

  def sendSticker (self, sticker: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendSticker",
      data={"chat_id": self.chatId, "sticker": sticker}
    )

  def sendVideo (self, video: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendVideo",
      data={"chat_id": self.chatId, "video": video}
    )

  def sendVoice (self, voice: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendVoice",
      data={"chat_id": self.chatId, "voice": voice}
    )

  def sendVideoNote (self, videoNote: str, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendVideoNote",
      data={"chat_id": self.chatId, "videoNote": videoNote}
    )

  def sendMediaGroup (self, media: List[Media], options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendMediaGroup",
      data={"chat_id": self.chatId, "media": media}
    )

  def sendLocation (self, location: Location, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendLocation",
      data={"chat_id": self.chatId, "location": location}
    )

  def sendVenue (self, venue: Venue, options: Optional[Dict[str, any]] = {}) -> None:
    assasin.post(
      path="/sendVenue",
      data={"chat_id": self.chatId, "venue": venue}
    )

  def sendContact (self, contact: Contact, options: Optional[Dict] = {}) -> None:
    assasin.post(
      path="/sendContact",
      data={"chat_id": self.chatId, "contact": contact}
    )

  def sendChatAction(self, action: str) -> None:
    assasin.post(
      path="/sendChatAction",
      data={"chat_id": self.chatId, "action": action}
    )
