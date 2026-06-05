# first - Notes API (backend)

Small, fast REST API for managing notes used by the first project.

Features
- Simple in-memory CRUD for notes (title, content, created_at/updated_at can be added).
- Single-file entrypoint: `main.py`
- FastAPI + Pydantic for fast development and automatic OpenAPI docs.

Requirements
- Python 3.8+
- Install dependencies (if you add any) via:
  ```sh
  pip install -r requirements.txt
  ```

Quick start (development)
- Run with Uvicorn:
  ```sh
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
  ```
- Open interactive docs: http://localhost:8000/docs

API Endpoints
- GET /notes
  - List all notes
  - Response: 200 OK, JSON array of notes
  - Example:
    ```sh
    curl http://localhost:8000/notes
    ```

- GET /notes/{id}
  - Get a single note by id
  - Response: 200 OK or 404 Not Found
  - Example:
    ```sh
    curl http://localhost:8000/notes/1
    ```

- POST /notes
  - Create a new note
  - Body (JSON): `{ "title": "...", "content": "..." }`
  - Response: 201 Created, created note JSON
  - Example:
    ```sh
    curl -X POST http://localhost:8000/notes \
      -H "Content-Type: application/json" \
      -d '{"title":"Sample","content":"This is a note."}'
    ```

- PUT /notes/{id}
  - Update a note
  - Body (JSON): `{ "title": "...", "content": "..." }`
  - Response: 200 OK or 404 Not Found
  - Example:
    ```sh
    curl -X PUT http://localhost:8000/notes/1 \
      -H "Content-Type: application/json" \
      -d '{"title":"Updated","content":"Updated content"}'
    ```

- DELETE /notes/{id}
  - Delete a note
  - Response: 204 No Content (or 200 with message) or 404 Not Found
  - Example:
    ```sh
    curl -X DELETE http://localhost:8000/notes/1
    ```

Data model
- create_note: title (str, required), content (str, required)
- Note_response: id (int), title (str), content (str)

Testing
- Add tests under `tests/` and run with:
  ```sh
  pytest
  ```

Development notes / known issues (recommendations)
- Return 404 when item not found (use fastapi.HTTPException).
- In `update_note` make sure the function parameter does not shadow the Pydantic model name and that `return` is inside the matching branch so the correct note is returned after update.
- Consider persistent storage (SQLite/postgres) instead of in-memory list for production.
- Add timestamps (created_at, updated_at) if required.

Contributing
- Open issues or PRs. Keep changes small and add tests.

License
- Add a LICENSE file for this repository.
