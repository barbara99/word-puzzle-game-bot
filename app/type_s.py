# work on types

from typing import Optional, List

Message: dict = {}

Chat: dict = {}

User: dict = {}

Animation: dict = {}

Document: dict = {}

PhotoSize: dict = {}

Sticker: dict = {}

Video: dict = {}

VideoNote: dict = {}

Voice: dict = {}

Dice: dict = {}

Game: dict = {}

Poll: dict = {}

PollAnswer: dict = {}

Location: dict = {
  "logitude": float,
  "latitude": float,
}

Venue: dict = {
  "latitude": float,
  "longitude": float,
  "title": str,
  "address": str,
}

# MessageEntityType = enumerate(("mention", "hashtag", "cashtag", "bot_command", "url", "email", "phone_number", "bold", "italic", "underline", "strikethrough", "code", "pre", "text_link", "text_mention"))

MessageEntity: dict = {
  "type": str,
  "offset": int,
  "length": int,
  "url": str,
  "user": any,
  "language": str,
}

#CaptionEntity = List[MessageEntity]

Media: dict = {
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

Contact: dict = {
  "phoneNumber": str,
  "firstName": str,
}

MessageAutoDeleteTimerChanged: dict = {}

Invoice: dict = {}

SuccessfulPayment: dict = {}

PassportData: dict = {}

ProximityAlertTriggered: dict = {}

VoiceChatStarted: dict = {}

VoiceChatEnded: dict = {}

VoiceChatParticipantsInvited: dict = {}

InlineKeyboardMarkup: dict = {}

InlineQuery: dict = {}

ChosenInlineResult: dict = {}

CallbackQuery: dict = {}

ChatMemberUpdated: dict = {}

ShippingQuery: dict = {}

PreCheckoutQuery: dict = {}

Message: dict = {
  "message_id": int,
  "from": User,
  "sender_chat": Chat,
  "date": int,
  "chat": Chat,
  "forward_from": User,
  "forward_from_chat": Chat,
  "forward_from_message_id": int,
  "forward_signature": str,
  "forward_sender_name": str,
  "forward_date": int,
  "reply_to_message": Message,
  "via_bot": User,
  "edit_date": int,
  "media_group_id": str,
  "author_signature": str,
  "text": str,
  "entities": List[MessageEntity],
  "animation": Animation,
  "audio": Audio,
  "document": Document,
  "photo": List[PhotoSize],
  "sticker": Sticker,
  "video": Video,
  "video_note": VideoNote,
  "voice": Voice,
  "caption": str,
  "caption_entities": List[MessageEntity],
  "contact": Contact,
  "dice": Dice,
  "game": Game,
  "poll": Poll,
  "venue": Venue,
  "new_chat_members": List[User],
  "left_chat_member": User,
  "new_chat_title": str,
  "new_chat_photo": List[PhotoSize],
  "delete_chat_photo": bool,
  "group_chat_created": bool,
  "supergroup_chat_created": bool,
  "channel_chat_created": bool,
  "message_auto_delete_timer_changed": MessageAutoDeleteTimerChanged,
  "migrate_to_chat_id": int,
  "migrate_from_chat_id": int,
  "pinned_message": Message,
  "invoice": Invoice,
  "successful_payment": SuccessfulPayment,
  "connected_website": str,
  "passport_data": PassportData,
  "proximity_alert_triggered": ProximityAlertTriggered,
  "voice_chat_started": VoiceChatStarted,
  "voice_chat_ended": VoiceChatEnded,
  "voice_chat_participants_invited": VoiceChatParticipantsInvited,
  "reply_markup": InlineKeyboardMarkup,
}

Update: dict = {
  "update_id": int,
  "message": Message,
  "edited_message": Message,
  "channel_post": Message,
  "edited_channel_post": Message,
  "inline_query": InlineQuery,
  "chosen_inline_result": ChosenInlineResult,
  "callback_query": CallbackQuery,
  "poll": Poll,
  "poll_answer": PollAnswer,
  "my_chat_member": ChatMemberUpdated,
  "chat_member": ChatMemberUpdated,
  "shipping_query": ShippingQuery,
  "pre_checkout_query": PreCheckoutQuery,
}
