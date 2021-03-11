import requests
from session import Session
from typing import Optional, Dict

Location = {
  "logitude": float,
  "latitude": float,
}

Venue = {
  "latitude": float,
  "longitude": float,
  "title": str,
  "address": str,
}

# MessageEntityType = enumerate(("mention", "hashtag", "cashtag", "bot_command", "url", "email", "phone_number", "bold", "italic", "underline", "strikethrough", "code", "pre", "text_link", "text_mention"))

MessageEntity = {
  "type": str,
  "offset": int,
  "length": int,
  "url": str,
  "user": any,
  "language": str,
}

#CaptionEntity = list[MessageEntity]

Media = {
  "type": str, #"animation" | "document" | "audio" | "video" | "photo",
  "media": str,
  "caption": Optional[str],
  "parse_mode": Optional[str],
  "caption_entities": Optional[any],
  "thumb": Optional[str],
  "width": Optional[int],
  "height": Optional[int],
  "duration": Optional[int],
  "supports_streaming": Optional[bool],
  "performer": Optional[str],
  "title": Optional[str],
  "disable_content_type_detection": Optional[bool]
}

Contact = {
  "phoneNumber": str,
  "firstName": str,
}

class Context:

  def __init__(self):
    self.session = Session()

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
