from sqlalchemy import Column, Integer, String, Text
from app.models.base import Base

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f"<Ticket(id={self.id}, description={self.description[:50]}...)>"
