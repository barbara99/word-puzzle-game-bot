

class Event:

  def __init__(self, event):
    self.rawself: {
      "message": {
        "messageId": int,
        "from": {
          "id": int,
          "isBot": bool,
          "firstName": str,
          "lastName": str,
          "languageCode": str,
        },
        "chat": {
          "id": int,
          "first_name": str,
          "last_name": str,
          "type": str,
        },
        "date": int,
        "text": str,
      },
    } = {}

    self.isMessage: bool = True
    self.message: {
      "text": str
    } = {}

    self.isText: bool = True
    self.text: str = ""

    self.isAudio: bool = True
    self.audio: {
      "file_id": str,
      "duration": int,
      "title": str,
    } = {}

    self.isDocument: bool = True
    self.document: {
      "file_id": str,
      "file_name": str,
    } = {}

    self.isGame: bool = True
    self.game: {
      "title": str,
      "description": str,
      "photo": [
        {
          "file_id": str,
          "width": int,
          "height": int,
        },
        {
          "file_id": str,
          "width": int,
          "height": int,
        },
      ],
    } = {}

    self.isPhoto: bool = True
    self.photo: list[{
      "file_id": str,
      "width": int,
      "height": int,
    }] = []

    self.isSticker: bool = True
    self.sticker: {
      "file_id": str,
      "width": int,
      "height": int,
    } = {}

    self.isVideo: bool = True
    self.video: {
      "file_id": str,
      "width": int,
      "height": int,
      "duration": int,
    } = {}

    self.isVoice: bool = True
    self.voice: {
      "file_id": str,
      "duration": int,
    } = {}

    self.isVideoNote: bool = True
    self.videoNote: {
      "file_id": str,
      "length": int,
      "duration": int,
    } = {}

    self.isContact: bool = True
    self.contact: {
      "phone_number": str,
      "first_name": str,
    } = {}

    self.isLocation: bool = True
    self.location: {
      "longitude": str,
      "latitude": str,
    } = {}

    self.isVenue: bool = True
    self.venue: {
      "location": {
        "longitude": str,
        "latitude": str,
      },
      "title": str,
      "address": str,
    } = {}

    self.isEditedMessage: bool = True
    self.editedMessage: {
      "message_id": str,
      "from": {
        "id": int,
        "is_bot": bool,
        "first_name": str,
        "last_name": str,
        "language_code": str,
      },
      "chat": {
        "id": int,
        "first_name": str,
        "last_name": str,
        "language_code": str,
      },
      "date": int,
      "edit_date": int,
      "text": str,
    } = {}

    self.isChannelPost: bool = True
    self.channelPost: {
      "message_id": str,
      "chat": {
        "id": int,
        "title": str,
        "type": str,
      },
      "date": int,
      "text": str,
    } = {}

    self.isEditedChannelPost: bool = True
    self.editedChannelPost: {
      "message_id": str,
      "chat": {
        "id": int,
        "title": str,
        "type": str,
      },
      "date": int,
      "edit_date": int,
      "text": str,
    } = {}

    self.isInlineQuery: bool = True
    self.inlineQuery: {
      "id": int,
      "from": {
        "id": int,
        "is_bot": bool,
        "first_name": str,
        "last_name": str,
        "language_code": str,
      },
      "query": str,
      "offset": str,
    } = {}

    self.isChosenInlineResult: bool = True
    self.chosenInlineResult: {
      "result_id": '2837258670654537434',
      "from": {
        "id": int,
        "is_bot": bool,
        "first_name": str,
        "last_name": str,
        "language_code": str,
      },
      "inline_message_id": str,
      "query": str,
    }

    self.isCallbackQuery: bool = true
    self.callbackQuery: {
      "id": int,
      "from": {
        'id': int,
        "is_bot": bool,
        "first_name": str,
        "last_name": str,
        "language_code": str,
      },
      "message": {
        "message_id": int,
        "from": {
          "id": int,
          "is_bot": bool,
          "first_name": str,
          "username": str,
        },
        "chat": {
          "id": int,
          "first_name": str,
          "last_name": str,
          "type": str,
        },
        "date": int,
        "text": str,
      },
      "chat_instance": str,
      "data": any,
    } = {}

    self.isPayload: bool = True
    self.payload: any = 'DEVELOPER_DEFINED_PAYLOAD'
