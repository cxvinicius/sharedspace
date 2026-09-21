from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql+psycopg://"
    "sharedspace:sharedspace@localhost:5432/sharedspace"
)


engine = create_engine(
    DATABASE_URL,
    echo=False,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)