from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry  
from core.config import settings
 
engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
mapper_registry = registry()

def init_db():
   mapper_registry.metadata.create_all(bind=engine)