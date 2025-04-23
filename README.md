# 📚 Telegram Quiz Bot

Добро пожаловать в репозиторий **Telegram Quiz Bot** — это обучающий бот-квиз, написанный на Python с использованием библиотеки [aiogram 3.x](https://docs.aiogram.dev/).

---

## 🚀 Возможности

- ❓ Задаёт пользователю 10 вопросов по Python
- ✅ Обрабатывает правильные и неправильные ответы
- 💾 Сохраняет прогресс и результат пользователя в SQLite
- 📊 Выводит финальный результат после квиза

---

## 🔧 Как запустить бота локально

1. **Клонируй репозиторий:**

```bash
git clone https://github.com/AlterHero/telegram-quiz-bot.git
cd telegram-quiz-bot
```

2. **Создай и активируй виртуальное окружение:**

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
```

3. **Установи зависимости:**

```bash
pip install -r requirements.txt
или выполни установку вручную:
pip install aiofiles-23.2.1-py3-none-any.whl
pip install aiohttp-3.9.3-cp311-cp311-win_amd64.whl
pip install magic_filter-1.0.11-py3-none-any.whl
pip install aiogram-3.4.1-py3-none-any.whl
pip install nest_asyncio
pip install aiosqlite
```

4. **Создай файл `config.py`:**

```python
API_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
```

5. **Запусти бота:**

```bash
python bot.py
```

---

## 📎 Команды бота

- `/start` — Приветствие и кнопка «Начать игру»
- `Начать игру` — Запускает квиз
- `/stats` *(в разработке)* — Выводит последнюю статистику

---

## 🤖 Бот в Telegram

🔗 Имя: **@JamBoxKvizBot** — [t.me/JamBoxKvizBot](https://t.me/JamBoxKvizBot)

---

## 📂 Структура проекта

```
├── bot.py              # Основной файл бота
├── database.py         # Работа с SQLite
├── questions.py        # Набор вопросов
├── quiz.py             # Кнопки и логика квиза
├── requirements.txt    # Зависимости
├── config.py           # Секретный токен 
└── README.md           # Этот файл
```

---

## 🧠 Автор
- Telegram: [@ifiwant](https://t.me/ifiwant)
- GitHub: [github.com/AlterHero](https://github.com/AlterHero)

---
