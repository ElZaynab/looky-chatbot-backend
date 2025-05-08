from pydantic import BaseModel

class TicketText(BaseModel):
    ticket_id: str  # Le ticket_id peut être une chaîne de caractères, si c'est ce qui est utilisé dans ta base
    clean_description: str
