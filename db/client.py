from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app import app

engine = create_engine(app.config["DATABASE_URL"], convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import db.models.article
    import db.models.user
    Base.metadata.create_all(bind=engine)
