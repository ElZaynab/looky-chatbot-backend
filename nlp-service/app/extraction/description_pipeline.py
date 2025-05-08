from app.utils.db import fetch_ticket_descriptions, update_ticket_clean_description
from app.preprocessing.text_cleaner import clean_description


def run_cleaning_pipeline():
    print("📦 Lancement du pipeline de nettoyage...")
    tickets = fetch_ticket_descriptions()
    for ticket in tickets:
        ticket_id = ticket[0]
        raw_description = ticket[1]
        cleaned = clean_description(raw_description)
        update_ticket_clean_description(ticket_id, cleaned)
        print(f"✅ Ticket {ticket_id} nettoyé.")
