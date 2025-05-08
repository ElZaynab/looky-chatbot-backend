from app.preprocessing.data_splitter import prepare_train_test

def test_data_split():
    # Exécuter la fonction de split
    split = prepare_train_test()

    # Vérifier si les ensembles de données d'entraînement et de test existent
    assert split.train, "L'ensemble d'entraînement est vide."
    assert split.test, "L'ensemble de test est vide."

    # Vérifier que la somme des tailles d'entraînement et de test est égale à la taille totale des données
    total_size = len(split.train) + len(split.test)
    assert total_size == 1539, f"Erreur : la taille totale est incorrecte, attendue 1539 mais obtenu {total_size}."

    # Vérifier que l'ensemble d'entraînement représente environ 80% des données
    assert abs(len(split.train) / total_size - 0.8) < 0.1, "La répartition des données pour l'entraînement n'est pas correcte."

    # Vérifier que l'ensemble de test représente environ 20% des données
    assert abs(len(split.test) / total_size - 0.2) < 0.1, "La répartition des données pour le test n'est pas correcte."

    # Vérifier qu'il n'y a pas de chevauchement entre les ensembles d'entraînement et de test
    train_ids = [ticket.ticket_id for ticket in split.train]
    test_ids = [ticket.ticket_id for ticket in split.test]
    assert not any(ticket_id in test_ids for ticket_id in train_ids), "Il y a un chevauchement entre l'entraînement et le test."

    print("✅ Test de validation du split réussi.")
