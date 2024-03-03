from DAXXMUSIC import app
from config import OWNER_ID
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DAXXMUSIC.utils.daxx_ban import admin_filter
from DAXXMUSIC.misc import SUDOERS

BOT_ID = app.me.id  # Corrected this line

@app.on_message(filters.command("banall") & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                await app.ban_chat_member(chat_id, member.user.id)
                await msg.reply_text(f"**‣ ᴏɴᴇ ᴍᴏʀᴇ ʙᴀɴɴᴇᴅ.**\n\n➻ {member.user.mention}\n\n**Bsᴅᴋ ᴀᴘɴᴇ  ʙᴀᴀᴘ MR CUTE X sᴇ ᴘᴀɴɢᴀ ʟᴏɢᴇ ᴛᴏʜ ᴘɪʟᴇɢᴇ ʜɪ ʙᴇᴛᴇ😌**")                    
            except Exception:
                pass
    else:
        await msg.reply_text("ʟᴀᴡᴅᴇ ᴘʜʟᴇ ᴀᴘɴᴇ ʙᴀᴀᴘ MR CUTE X sᴇ sᴜᴅᴏ ᴛᴏ ʟᴇʟᴇ ᴠᴀʀɴᴀ ᴀsᴇ ʜɪ ᴘᴇʟᴀ Jᴀʏᴇɢᴀ 🥱🤧.")
