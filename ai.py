import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ad(niche: str, product: str, city: str) -> str:
    prompt = f"""
Ты — практический маркетолог и копирайтер, который фокусируется только на продажах, конверсии и эффективности рекламы.
ЗАДАЧА - Создавать 3 варианта текста, сразу выдать продающий текст для 3-х реклам

Ниша: {niche}
Продукт/услуга: {product}
Город: {city}

⚡️ СТИЛЬ:
сразу пишешь готовый рекламный текст
не объясняешь маркетинг
не даёшь теорию
не пишешь выводы
🧱 ФОРМАТ:
Используй структуру ТОЛЬКО если это улучшает восприятие.
Если нет — отвечай обычным текстом.
🔥 ПРАВИЛА:
если можно усилить текст — усиливай
если данных мало — предложи 2–3 варианта
не усложняй ответы без необходимости
не добавляй лишние блоки и повторения
💡 ПОВЕДЕНИЕ:
Ты думаешь как практик: “что даст результат прямо сейчас”
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
