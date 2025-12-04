FROM python:3.11-slim

# Устанавливаем системные зависимости для Chrome и драйвера
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python-библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (тесты и код)
COPY . .

# Запуск pytest по умолчанию (можно переопределить командой в gitlab-ci.yml)
CMD ["pytest", "-m", "short_test", "--alluredir=allure-results", "-v"]
