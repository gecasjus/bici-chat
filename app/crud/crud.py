import models
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies.database import get_db

def get_messages(id: str, db: Session = Depends(get_db)):
    return db.query(models.Message).filter(models.Message.chat_id == id).all()

def get_chat(id: str, db: Session = Depends(get_db)):
    return db.query(models.Chat).filter(models.Chat.id == id).first()

def insert(value, db: Session = Depends(get_db)):
    db.add(value)
    db.commit()
    db.refresh(value)