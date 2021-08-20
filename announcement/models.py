
from sqlalchemy import Text, Column, String, Date, Integer, Boolean
from .database import Base


class Announcement(Base):
    __tablename__ = "announce"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True)
    date = Column(Date)
    description = Column(Text, index=True)
    connect = Column(String, index=True)








