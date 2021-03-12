from .helpers import hasKey, Object

class Event:

  def __init__(self, event):
    event = Object(event)
    self.rawself = event
    self.isMessage: bool = True if hasKey(event, 'message') else False
    self.message = event['message'] if self.isMessage else None

    message = event['message']

    self.isText: bool = True if hasKey(message, 'text') else False
    self.text = message['text'] if self.isText else None 

    self.isAudio: bool = True if hasKey(message, 'audio') else False
    self.audio = message['audio'] if self.isAudio else None

    self.isDocument: bool = True if hasKey(message, 'document') else False
    self.document = message['document'] if self.isDocument else None

    self.isGame: bool = True if hasKey(message, 'game') else False
    self.game = message['game'] if self.isGame else None

    self.isPhoto: bool = True if hasKey(message, 'photo') else False
    self.photo = message['photo'] if self.isPhoto else None

    self.isSticker: bool = True if hasKey(message, 'sticker') else False
    self.sticker = message['sticker'] if self.isSticker else None

    self.isVideo: bool = True if hasKey(message, 'video') else False
    self.video = message['video'] if self.isVideo else None

    self.isVoice: bool = True if hasKey(message, 'voice') else False
    self.voice = message['voice'] if self.isVoice else None

    self.isVideoNote: bool = True if hasKey(message, 'video_note') else False
    self.videoNote = message['video_note'] if self.isVideoNote else None

    self.isContact: bool = True if hasKey(message, 'contact') else False
    self.contact = message['contact'] if self.isContact else None

    self.isLocation: bool = True if hasKey(message, 'location') else False
    self.location = message['location'] if self.isLocation else None

    self.isVenue: bool = True if hasKey(message, 'venue') else False
    self.venue = message['venue'] if self.isVenue else None

    self.isEditedMessage: bool = True if hasKey(event, 'edited_message') else False
    self.editedMessage = event['edited_message'] if self.isEditedMessage else None

    self.isChannelPost: bool = True if hasKey(event, 'channel_post') else False
    self.channelPost = event['channel_post'] if self.isChannelPost else None

    self.isEditedChannelPost: bool = True if hasKey(event, 'edited_channel_post') else False
    self.edittedChannelPost = event['edited_channel_post'] if self.isEditedChannelPost else None

    self.isInlineQuery: bool = True if hasKey(event, 'inline_query') else False
    self.inlineQuery = event['inline_query'] if self.isInlineQuery else None

    self.isChosenInlineResult: bool = True if hasKey(event, 'chosen_inline_result') else False
    self.chosenInlineResult = event['chosen_inline_result'] if self.isChosenInlineResult else None

    self.isCallbackQuery: bool = True if hasKey(event, 'callback_query') else False
    self.callbackQuery = event['callback_query'] if self.isCallbackQuery else None

    self.isPayload: bool = True
    self.payload: any = 'DEVELOPER_DEFINED_PAYLOAD'

    if self.isMessage:
      print(self.message["chat"])
      self.chat = self.message["chat"]
    elif self.isEditedMessage:
      self.chat = self.editedMessage.chat
    elif self.isChannelPost:
      self.chat = self.channelPost.chat
    elif self.isEditedChannelPost:
      self.chat = self.edittedChannelPost.chat
    else:
      self.chat = None