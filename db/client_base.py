from sqlalchemy.orm import Session
from sqlalchemy import create_engine


class DBClientBase:

    engine = create_engine("postgresql://admin:admin@127.0.0.1/lock_service")
    session = Session(engine)
