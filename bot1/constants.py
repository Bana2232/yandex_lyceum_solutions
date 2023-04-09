from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN_API = "5963535908:AAFRu7h6hyDbCtJXbYtfBrT-O_2Qt91EosY"
keyb_start = ReplyKeyboardMarkup([[KeyboardButton("/timer"), KeyboardButton("/dice")]], resize_keyboard=True)
keyb_timer = ReplyKeyboardMarkup(
    [[KeyboardButton("/set_30_seconds")], [KeyboardButton("/set_1_minute"),
                                           KeyboardButton("/set_5_minutes")
                                           ],
     [KeyboardButton("/back")]],
    resize_keyboard=True)

keyb_cancel = ReplyKeyboardMarkup([[KeyboardButton("/close")]], resize_keyboard=True)
keyb_dice = ReplyKeyboardMarkup([[KeyboardButton("/roll_one_hexagon_dice"), KeyboardButton("/roll_two_hexagon_dice"),
                                  KeyboardButton("/roll_the_20-sided_dice")], [KeyboardButton("/back")]],
                                resize_keyboard=True)
