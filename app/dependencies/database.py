from app.database.database import SessionLocal

def _get_connection():
    conn = SessionLocal()
    try:
        yield conn
    finally:
        conn.close()

def get_repository(repo:):
