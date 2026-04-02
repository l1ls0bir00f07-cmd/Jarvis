import os
import webbrowser
import psutil


def execute(command):
    command = command.lower()

    # 🌐 открыть браузер
    if "браузер" in command:
        webbrowser.open("https://google.com")
        return "Открываю браузер"

    # 🎥 YouTube
    if "ютуб" in command:
        webbrowser.open("https://youtube.com")
        return "Открываю YouTube"

    # 📁 проводник
    if "проводник" in command or "файлы" in command:
        os.startfile("C:\\")
        return "Открываю проводник"

    # 🔌 выключение ПК
    if "выключи компьютер" in command:
        os.system("shutdown /s /t 5")
        return "Выключаю компьютер через 5 секунд"

    # 🔄 перезагрузка
    if "перезагрузи" in command:
        os.system("shutdown /r /t 5")
        return "Перезагрузка через 5 секунд"

    # 📊 CPU
    if "загрузка процессора" in command or "cpu" in command:
        cpu = psutil.cpu_percent(interval=1)
        return f"Загрузка процессора {cpu} процентов"

    # 💾 RAM
    if "оперативка" in command or "память" in command:
        ram = psutil.virtual_memory().percent
        return f"Используется {ram} процентов оперативной памяти"

    return "Команда не распознана"