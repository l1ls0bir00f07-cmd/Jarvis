from wake_word import wait_for_wake_word
from stt import listen
from llm import ask_llm
from tts import speak
from router import route
from actions import execute
from memory import add

print("🟢 Джарвис запущен")
add(text, result)
while True:
    wait_for_wake_word()  # 👈 Ждём "Джарвис"

    text = listen()

    if not text:
        continue

    print("Ты:", text)

    task_type = route(text)

    if task_type == "action":
        result = execute(text)
    else:
        result = ask_llm(text)

    speak(result)
    