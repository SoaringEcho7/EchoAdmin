# EchoAdmin

A modern admin dashboard built with Python, Robyn and HTMX.

## Technology Stack

- Backend: Robyn (Python Web Framework)
- Frontend: HTMX + Tailwind CSS
- Database: SQLite (for development) / PostgreSQL (for production)

## Project Structure

```
EchoAdmin/
├── app/                    # Application package
│   ├── __init__.py        # Initialize app package
│   ├── models/            # Database models
│   ├── controllers/       # Request handlers
│   ├── services/         # Business logic
│   ├── templates/        # HTML templates
│   └── static/           # Static files (CSS, JS, images)
├── config/               # Configuration files
├── tests/               # Test cases
├── scripts/             # Utility scripts
└── requirements/        # Project dependencies
    ├── base.txt        # Base dependencies
    ├── dev.txt         # Development dependencies
    └── prod.txt        # Production dependencies
```

## Setup and Installation

1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install uv (if not already installed):
```bash
pip install uv
```

3. Install dependencies using uv:
```bash
# For development
uv pip install -r requirements/dev.txt

# For production
uv pip install -r requirements/base.txt
```

4. Run the application:
```bash
python run.py
```

## Development

- Follow PEP 8 style guide
- Write tests for new features
- Update requirements files when adding new dependencies

## License

MIT License
