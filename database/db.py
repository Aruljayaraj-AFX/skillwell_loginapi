from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL= "postgresql://ict_knif_user:PEw9NW5lNQd7a0HycO000mOZHEKhULCV@dpg-d2je037diees73c44mkg-a.oregon-postgres.render.com/ict_knif"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
session=SessionLocal(bind=engine)