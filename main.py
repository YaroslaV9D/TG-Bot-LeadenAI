import telebot
from dotenv import load_dotenv
import os
from ai import generate_ad

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
        "Привет! 🔥\n\n"
        "Я AI рекламный помощник.\n"
        "Напиши мне в формате:\n"
        "`ниша + продукт + город`\n\n"
        "Пример:\n"
        "`фитнес + протеин + Москва`"
    )

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.strip()
    
    if '+' in text:
        try:
            parts = [x.strip() for x in text.split('+')]
            if len(parts) >= 3:
                niche = parts[0]
                product = parts[1]
                city = ' + '.join(parts[2:])  # на случай, если город состоит из нескольких слов
                
                bot.send_message(message.chat.id, "Генерирую рекламу 🔥")
                
                ad_text = generate_ad(niche, product, city)
                bot.send_message(message.chat.id, ad_text, parse_mode='Markdown')
            else:
                bot.send_message(message.chat.id, "Нужно минимум 3 части через `+`\nПример: фитнес + протеин + Москва")
        except:
            bot.send_message(message.chat.id, "Что-то пошло не так. Попробуй ещё раз.")
    else:
        bot.send_message(message.chat.id, "Напиши в формате: ниша + продукт + город")

print("Бот запущен...")
bot.infinity_polling()