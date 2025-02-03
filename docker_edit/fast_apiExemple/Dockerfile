# Используем официальный Python-образ
FROM python:3.13-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /main/

# Копируем файлы проекта в контейнер
COPY . /main/

# Устанавливаем зависимости (если есть `requirements.txt`)
RUN pip install --no-cache-dir fastapi uvicorn

# Открываем порт
EXPOSE 8888

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
