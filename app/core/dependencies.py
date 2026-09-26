from app.db.session import SessionLocal

#DB
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

