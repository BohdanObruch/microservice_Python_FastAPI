# User API

## Описание

Микросервис для управления пользователями с использованием FastAPI.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <repository_url>
    cd project
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск

1. Запустите сервер:
    ```bash
    uvicorn main:app --reload
    ```

2. Откройте в браузере:
    ```plaintext
    http://127.0.0.1:8000/docs
    ```

## Тестирование

Запустите автотесты:
```bash
pytest