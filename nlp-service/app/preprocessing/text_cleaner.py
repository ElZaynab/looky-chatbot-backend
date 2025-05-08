import re
from html import unescape

def clean_description(text: str) -> str:
    # Si le texte est None, retourner une chaîne vide
    if text is None:
        return ""

    # 1. Décodage des entités HTML
    text = unescape(text)

    # 2. Suppression des avertissements standardisés
    text = re.sub(r"⚠.*?fiable\.", "", text, flags=re.DOTALL)

    # 3. Suppression des balises HTML restantes et assimilées
    text = re.sub(r"</?[^>]+>", "", text)
    text = re.sub(r"\b(?:tbody|b|ul|li|pre|a href[^ ]*|img[^ ]*|src[^ ]*)\b", "", text)

    # 4. Suppression des URL, images, chemins
    text = re.sub(r"https?://\S+|www\.\S+|img src\S+|iconName\S+", "", text)

    # 5. Suppression des signatures et footers
    text = re.sub(r"Cordialement,.*?(?=(De :|Envoyé :|$))", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"Avant d.?imprimer.*", "", text)
    text = re.sub(r"Email envoyé par.*", "", text, flags=re.IGNORECASE)

    # 6. Suppression des entêtes d’e-mails
    text = re.sub(r"(De|Envoyé|À|Cc|Objet)\s?:.*", "", text, flags=re.IGNORECASE)

    # 7. Nettoyage HTML malformé
    text = re.sub(r"[\[\]<>]", "", text)
    text = re.sub(r"\b(width|height|alt|src|href)[^\s]*", "", text)

    # 8. Nettoyage général
    text = re.sub(r"[^\w\s,.@-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text
