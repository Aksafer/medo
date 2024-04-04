from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url= "https://t.me/YR_HC"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مٓ ـطؤر آلسؤرس", url= "https://t.me/Y_D_ll"),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/YR_HC"), 
        ],
        [
            
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/SOURCE_SOM3A") , 
        ],
    ]
    return buttons
