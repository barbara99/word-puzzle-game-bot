# work on types
import sys

if sys.version_info >= (3, 8):
  from typing import TypedDict, List, Optional
else:
  from typing import List, Optional
  from typing_extensions import TypedDict

class Chat(TypedDict, total=False):
  pass

class User(TypedDict, total=False):
  pass

class Animation(TypedDict, total=False):
  pass

class Document(TypedDict, total=False):
  pass

class PhotoSize(TypedDict, total=False):
  pass

class Sticker(TypedDict, total=False):
  pass

class Audio(TypedDict, total=False):
  pass

class Video(TypedDict, total=False):
  pass

class VideoNote(TypedDict, total=False):
  pass

class Voice(TypedDict, total=False):
  pass

class Dice(TypedDict, total=False):
  pass

class Game(TypedDict, total=False):
  pass

class Poll(TypedDict, total=False):
  pass

class PollAnswer(TypedDict, total=False):
  pass

class Location(TypedDict, total=False):
  logitude: float
  latitude: float

class Venue(TypedDict, total=False):
  latitude: float
  longitude: float
  title: str
  address: str

# MessageEntityType: enumerate((mention hashtag cashtag bot_command url email phone_number bold italic underline strikethrough code pre text_link text_mention))

class MessageEntity(TypedDict, total=False):
  type: str
  offset: int
  length: int
  url: str
  user: User
  language: str

class Media(TypedDict, total=False):
  type: str #animation | document | audio | video | photo
  media: str
  caption: Optional[str]
  parse_mode: Optional[str]
  caption_entities: Optional[List[MessageEntity]]
  thumb: Optional[str]
  width: Optional[int]
  height: Optional[int]
  duration: Optional[int]
  supports_streaming: Optional[bool]
  performer: Optional[str]
  title: Optional[str]
  disable_content_type_detection: Optional[bool]

class Contact(TypedDict, total=False):
  phoneNumber: str
  firstName: str

class MessageAutoDeleteTimerChanged(TypedDict, total=False):
  pass

class Invoice(TypedDict, total=False):
  pass

class SuccessfulPayment(TypedDict, total=False):
  pass

class PassportData(TypedDict, total=False):
  pass

class ProximityAlertTriggered(TypedDict, total=False):
  pass

class VoiceChatStarted(TypedDict, total=False):
  pass

class VoiceChatEnded(TypedDict, total=False):
  pass

class VoiceChatParticipantsInvited(TypedDict, total=False):
  pass

class InlineKeyboardMarkup(TypedDict, total=False):
  pass

class InlineQuery(TypedDict, total=False):
  pass

class ChosenInlineResult(TypedDict, total=False):
  pass

class CallbackQuery(TypedDict, total=False):
  pass

class ChatMemberUpdated(TypedDict, total=False):
  pass

class ShippingQuery(TypedDict, total=False):
  pass

class PreCheckoutQuery(TypedDict, total=False):
  pass

class Message(TypedDict, total=False):
  message_id: int
  _from: User
  sender_chat: Chat
  date: int
  chat: Chat
  forward_from: User
  forward_from_chat: Chat
  forward_from_message_id: int
  forward_signature: str
  forward_sender_name: str
  forward_date: int
  reply_to_message: any
  via_bot: User
  edit_date: int
  media_group_id: str
  author_signature: str
  text: str
  entities: List[MessageEntity]
  animation: Animation
  audio: Audio
  document: Document
  photo: List[PhotoSize]
  sticker: Sticker
  video: Video
  video_note: VideoNote
  voice: Voice
  caption: str
  caption_entities: List[MessageEntity]
  contact: Contact
  dice: Dice
  game: Game
  poll: Poll
  venue: Venue
  new_chat_members: List[User]
  left_chat_member: User
  new_chat_title: str
  new_chat_photo: List[PhotoSize]
  delete_chat_photo: bool
  group_chat_created: bool
  supergroup_chat_created: bool
  channel_chat_created: bool
  message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged
  migrate_to_chat_id: int
  migrate_from_chat_id: int
  pinned_message: any
  invoice: Invoice
  successful_payment: SuccessfulPayment
  connected_website: str
  passport_data: PassportData
  proximity_alert_triggered: ProximityAlertTriggered
  voice_chat_started: VoiceChatStarted
  voice_chat_ended: VoiceChatEnded
  voice_chat_participants_invited: VoiceChatParticipantsInvited
  reply_markup: InlineKeyboardMarkup

class Update(TypedDict, total=False):
  update_id: int
  message: Message
  edited_message: Message
  channel_post: Message
  edited_channel_post: Message
  inline_query: InlineQuery
  chosen_inline_result: ChosenInlineResult
  callback_query: CallbackQuery
  poll: Poll
  poll_answer: PollAnswer
  my_chat_member: ChatMemberUpdated
  chat_member: ChatMemberUpdated
  shipping_query: ShippingQuery
  pre_checkout_query: PreCheckoutQuery
