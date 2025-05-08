from pydantic import BaseModel
from typing import List

class TicketText(BaseModel):
    ticket_id: str
    clean_description: str

class DataSplit(BaseModel):
    train: List[TicketText]
    test: List[TicketText]
