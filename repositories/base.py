from config import SessionLocal

class BaseRepository:
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def save(self):
        print(self)

        # self.get_db(self)
        # self.get_db.commit()
        # self.get_db.refresh(self)
    
    # each individual repo




#     value = db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user



#         def get_messages(id: str, db: Session = Depends(get_db)):
#     return db.query(models.Message).filter(models.Message.chat_id == id).all()

# def get_chat(id: str, db: Session = Depends(get_db)):