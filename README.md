
# Загруженность компьютера

Тестовое задание от НПО Автомотив на вакансию Full-stack Python разработчик Junior/Junior+

**Загруженность компьютера** — это десктопное приложение для мониторинга загрузки CPU, RAM и диска в реальном времени.

---

## 🛠️ Функционал

1. **Мониторинг загрузки:**
   - Отображение текущей загрузки процессора (CPU), оперативной памяти (RAM) и дискового пространства (Disk).
   - Обновление данных каждые `N` секунд (настраивается).

2. **Запись в базу данных:**
   - Кнопка "Начать запись" запускает сохранение данных в базу SQLite.
   - Таймер показывает время, прошедшее с начала записи.
   - Кнопка "Остановить запись" завершает сохранение данных.

3. **Настройка интервала обновления:**
   - Интервал можно задать в диапазоне от 1 до 60 секунд.

---

## 📂 Структура проекта

```
app-computer-load/
├── ui.py              # Интерфейс пользователя
├── database.py        # Работа с базой данных
├── monitoring.py      # Логика мониторинга
└── main.py            # Запуск приложения
```

---

## 🔧 Установка и запуск

### Требования
- Python 3.8+
- PyQt5
- psutil

### Установка зависимостей
1. Клонируйте репозиторий или загрузите файлы:
   ```bash
   git clone https://github.com/your-repo/app-computer-load.git
   cd app-computer-load
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

### Запуск
Запустите приложение из папки проекта:
```bash
python main.py
```

---

## 💻 Скриншоты

### Главный экран
> Отображение текущей загрузки CPU, RAM и диска.

### Таймер записи
> Кнопка "Начать запись" переключается на "Остановить запись" с отображением таймера.

---