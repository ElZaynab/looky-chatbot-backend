import urllib.parse
from sqlalchemy import create_engine, text

# Connexion sécurisée
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=OUJ1-TT-PTB004;"
    "DATABASE=looky;"
    "Trusted_Connection=yes;"
)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)


def fetch_ticket_descriptions():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT TicketID, Description FROM tickets"))
        return result.fetchall()


def update_ticket_clean_description(ticket_id, clean_text):
    with engine.connect() as conn:
        query = text("UPDATE tickets SET Clean_description = :clean WHERE TicketID = :id")
        conn.execute(query, {"clean": clean_text, "id": ticket_id})
        conn.commit()

def fetch_clean_descriptions():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT TicketID, Clean_description FROM tickets WHERE Clean_description IS NOT NULL"))
        return result.fetchall()
