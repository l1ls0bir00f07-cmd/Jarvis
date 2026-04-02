import aiosqlite

DB_NAME = "jarvis.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT,
                assistant TEXT
            )
        """)
        await db.commit()

async def save_memory(user, assistant):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO memory (user, assistant) VALUES (?, ?)",
            (user, assistant)
        )
        await db.commit()

async def get_memory(limit=5):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT user, assistant FROM memory ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = await cursor.fetchall()

    context = ""
    for row in reversed(rows):
        context += f"Пользователь: {row[0]}\nДжарвис: {row[1]}\n"

    return context