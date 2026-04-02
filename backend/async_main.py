import asyncio

from wake_word import wait_for_wake_word
from stt import listen
from llm import ask_llm
from tts import speak
from router import route
from actions import execute
from memory_db import init_db, save_memory


async def main():
    await init_db()

    print("🟢 Джарвис запущен")

    while True:
        # ждём слово "Джарвис"
        await asyncio.get_event_loop().run_in_executor(None, wait_for_wake_word)

        # слушаем речь
        text = await asyncio.get_event_loop().run_in_executor(None, listen)

        if not text:
            continue

        print("Ты:", text)

        task_type = route(text)

        if task_type == "action":
            result = execute(text)
        elif task_type == "cloud":
            result = await ask_llm(text)
        else:
            result = await ask_llm(text)

        print("Джарвис:", result)

        await asyncio.get_event_loop().run_in_executor(None, speak, result)

        await save_memory(text, result)


# запуск
asyncio.run(main())