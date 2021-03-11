# Context

## Send
### sendMessage: (text [, options])
### sendPhoto: (photo [, options])
### sendAudio: (audio [, options])
### sendDocument: (document [, options])
### sendSticker: (sticker [, options])
### sendVideo: (video [, options])
### sendVoice: (voice [, options])
### sendVideoNote: (videoNote [, options])
### sendMediaGroup: (media [, options])
### sendLocation: (location [, options])
### sendVenue: (venue [, options])
### sendContact: (contact [, options])
### sendChatAction: (action)

## Get
### getUserProfilePhotos: ()
### getChat: ()
### getChatAdministrators: ()
### getChatMembersCount: ()
### getChatMember: (userId)

## Update
### editMessageText: (text [, options])
### editMessageCaption: (text [, options])
### editMessageReplyMarkup: (replyMarkup [, options])
### deleteMessage: (messageId)
### editMessageLiveLocation: (location [, options])
### stopMessageLiveLocation: (options)

## Group
### kickChatMember: (userId [, options])
### unbanChatMember: (userId)
### restrictChatMember: (userId [, options])
### promoteChatMember: (userId [, options])
### exportChatInviteLink: ()
### setChatPhoto: (photo)
### deleteChatPhoto: ()
### setChatTitle: (title)
### setChatDescription: (description)
### setChatStickerSet: (stickerSetName)
### deleteChatStickerSet: ()
### pinChatMessage: (messageId [, options])
### unpinChatMessage: ()
### leaveChat: ()

## Game
### sendGame: (gameShortName [, options])
### setGameScore: (score [, options])
### getGameHighScores: ()

## Others
### forwardMessageFrom: (fromChatId, messageId [, options])
### forwardMessageTo: (toChatId, messageId [, options])
### answerInlineQuery: (results [, options])