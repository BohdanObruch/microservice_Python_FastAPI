# User API

## Description

A microservice for user management using FastAPI.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd project
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

## Running

1. Start the server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open in the browser:
    ```plaintext
    http://127.0.0.1:8000/docs
    ```

## Testing

Run the automated tests:
```bash
pytest
```

## Tests and methods realized

- [x] Create a new user
- [x] List all users
- [x] Get user by ID
- [x] Update user by ID (PUT)
- [x] Update user by ID (PATCH)
- [x] Delete user by ID
- [x] Register a new user
- [x] Login a user
