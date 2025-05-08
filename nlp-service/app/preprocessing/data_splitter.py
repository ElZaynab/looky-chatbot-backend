import random
from app.utils.db import fetch_clean_descriptions
from app.models.split_dataset import TicketText, DataSplit
from typing import List

def split_data(tickets: List[tuple], ratio: float = 0.8) -> DataSplit:
    # Convertir en objets TicketText
    data = [TicketText(ticket_id=row[0], clean_description=row[1]) for row in tickets if row[1]]
    random.shuffle(data)
    split_idx = int(len(data) * ratio)
    return DataSplit(train=data[:split_idx], test=data[split_idx:])

def prepare_train_test():
    raw = fetch_clean_descriptions()
    return split_data(raw)
