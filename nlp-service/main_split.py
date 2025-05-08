from app.preprocessing.data_splitter import prepare_train_test

if __name__ == "__main__":
    print("🚀 Running data splitting...")

    # Appel de la fonction de séparation des données
    split = prepare_train_test()

    # Affichage de la taille du jeu d'entraînement et du jeu de test
    print(f"Train size: {len(split.train)}")
    print(f"Test size: {len(split.test)}")

    # Affichage des premiers éléments du train et test (juste pour vérifier)
    print("Exemple Train Data:")
    print(split.train[:2])  # Affiche les 2 premiers éléments

    print("Exemple Test Data:")
    print(split.test[:2])  # Affiche les 2 premiers éléments
