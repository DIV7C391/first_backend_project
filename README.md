# bfirst - Notes API (backend)

Small, fast REST API for managing notes used by the bfirst project.

Overview
- Simple CRUD API for notes (title, content, created_at, updated_at).
- Single-file entrypoint: [main.py](main.py)

Tech stack
- Python 3.x
- Minimal dependencies (see requirements or project file if present)

Quick start

1. Install dependencies (if any)
```sh
pip install -r requirements.txt  # if present
```

2. Run the server
```sh
python main.py
```
The main application entrypoint is [main.py](main.py).

API endpoints (common conventions)
- GET /notes
  - List all notes
  - Response: 200 OK, JSON array of notes
- GET /notes/{id}
  - Get a single note by id
  - Response: 200 OK or 404 Not Found
- POST /notes
  - Create a new note
  - Body (JSON): { "title": "...", "content": "..." }
  - Response: 201 Created, created note JSON
- PUT /notes/{id}
  - Update a note
  - Body (JSON): { "title": "...", "content": "..." }
  - Response: 200 OK or 404 Not Found
- DELETE /notes/{id}
  - Delete a note
  - Response: 204 No Content or 404 Not Found

Example curl (create)
```sh
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"Sample","content":"This is a note."}'
```

Environment & configuration
- Configure host/port or DB settings via environment variables or a config file if implemented in [main.py](main.py).

Testing
- Add unit or integration tests under a tests/ folder.
- Run with pytest if available:
```sh
pytest
```

Contributing
- Open issues or PRs for bugs and features.
- Keep changes small and add tests where applicable.

License
- Add a LICENSE file appropriate for your project.

Contact
- For questions about the code, inspect the server entrypoint: [main.py](main.py)