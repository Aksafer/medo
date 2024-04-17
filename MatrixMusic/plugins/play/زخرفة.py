
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_photo(message.chat.id,"https://t.me/ifuwufuj/29",caption="""
👋 | مرحباً بك عزيزي في بوت الزخرفة
⛔ | ارسل اسمك الزخرفة 
⚜️ | ملاحظة ارسل الاسم بالانجليزي 
""")
def en(num):
 num = str(num)
 return num.replace("a", "𝗔").replace("b", "𝗕").replace("c", "𝗖").replace("d", "𝗗").replace("e","𝗘").replace("f", "𝗙").replace("g", "𝗚").replace("h", "𝗛").replace("i", "𝗜").replace("j", "𝗝").replace("k", "𝗞").replace("l", "𝗟 ").replace("m", "𝗠").replace("n", "𝗡").replace("o", "𝗢").replace("p", "𝗣").replace("q", "𝗤").replace("r", "𝗥").replace("s", "𝗦").replace("t", "𝗧").replace("u", "𝗨").replace("v", "𝗩").replace("w", "𝗪").replace("x", "𝗫").replace("y", "𝗬").replace("z", "𝗭") 
@bot.message_handler(func=lambda message:True) 
def zagrafa(message):
	u=message.text
	D=en(u)
	print(D)
	bot.send_message(message.chat.id,D)
bot.infinity_polling()
