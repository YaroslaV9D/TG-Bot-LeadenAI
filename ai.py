import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ad(niche: str, product: str, city: str) -> str:
    prompt = f"""
Ты — профессиональный маркетолог и копирайтер.
Создай продающую рекламу для Telegram.

Ниша: {niche}
Продукт/услуга: {product}
Город: {city}

Сделай 3 варианта:
1. Короткий яркий (1-2 предложения)
2. Средний (эмоциональный + польза)
3. Длинный продающий (с призывом)

Используй эмодзи. Тон живой и уверенный 🔥
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # или mixtral-8x7b-32768
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=800
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Ошибка Groq:\n{str(e)[:300]}"