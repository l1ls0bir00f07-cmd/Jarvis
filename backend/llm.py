import requests
import asyncio
from memory_db import get_memory

def ask_llm_sync(prompt, context):
    full_prompt = f"""
Ты Джарвис — интеллектуальный ассистент.
Отвечай кратко и уверенно.

Контекст:
{context}

Пользователь: {prompt}
Джарвис:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    return response.json()["response"]


async def ask_llm(prompt):
    context = await get_memory()
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ask_llm_sync, prompt, context)