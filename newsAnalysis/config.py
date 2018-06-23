import os

HOST=os.getenv('DB_HOST', None)
DB=os.getenv("DB_NAME", None)
PORT=os.getenv("DB_PORT", None)
USER=os.getenv("DB_USER", None)
PASSWORD=os.getenv("DB_PASSWORD", None)

NO_DOCS=os.getenv("NO_DOCS", 1000)
