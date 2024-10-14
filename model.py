from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self):
        self.model = None
        self.trained = False

    def train(self, X_train, y_train, X_test, y_test):
        print("\nTraining the model...")
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)
        self.trained = True
        print("Model training complete!")
        self.evaluate(X_test, y_test)

    def evaluate(self, X_test, y_test):
        if self.trained:
            predictions = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model accuracy: {accuracy * 100:.2f}%\n")
        else:
            print("Model is not trained yet.")

    def get_trained_model(self):
        if self.trained:
            return self.model
        else:
            print("Model is not trained yet.")
            return None
