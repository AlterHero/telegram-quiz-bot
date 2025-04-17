import aiosqlite
from config import DB_NAME

async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS quiz_state (
            user_id INTEGER PRIMARY KEY, 
            question_index INTEGER, 
            score INTEGER
        )''')
        await db.commit()

async def get_quiz_index(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('SELECT question_index FROM quiz_state WHERE user_id = ?', (user_id,))
        result = await cursor.fetchone()
        return result[0] if result else 0

async def update_quiz_index(user_id, index):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            '''
            INSERT INTO quiz_state (user_id, question_index, score)
            VALUES (?, ?, COALESCE((SELECT score FROM quiz_state WHERE user_id = ?), 0))
            ON CONFLICT(user_id) DO UPDATE SET question_index = excluded.question_index
            ''',
            (user_id, index, user_id)
        )
        await db.commit()

async def update_score(user_id, score):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            '''
            INSERT INTO quiz_state (user_id, question_index, score)
            VALUES (?, COALESCE((SELECT question_index FROM quiz_state WHERE user_id = ?), 0), ?)
            ON CONFLICT(user_id) DO UPDATE SET score = excluded.score
            ''',
            (user_id, user_id, score)
        )
        await db.commit()

async def get_score(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('SELECT score FROM quiz_state WHERE user_id = ?', (user_id,))
        result = await cursor.fetchone()
        return result[0] if result and result[0] is not None else 0

async def get_all_scores():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute('SELECT user_id, score FROM quiz_state')
        return await cursor.fetchall()
