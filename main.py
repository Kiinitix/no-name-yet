from data_loader import DataLoader
from model import ModelTrainer
from prediction import PredictionSystem

class MalwareDetectionSystem:
    def __init__(self):
        self.data_loader = DataLoader()
        self.model_trainer = ModelTrainer()
        self.prediction_system = None

    def menu(self):
        while True:
            print("\n--- Malware Detection System ---")
            print("1. Load Dataset")
            print("2. Train Model")
            print("3. Make Prediction")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                self.data_loader.load_dataset()
                self.data_loader.display_sample_data()
            elif choice == '2':
                X_train, X_test, y_train, y_test = self.data_loader.preprocess_data()
                if X_train is not None:
                    self.model_trainer.train(X_train, y_train, X_test, y_test)
                    self.prediction_system = PredictionSystem(self.model_trainer.get_trained_model())
            elif choice == '3':
                if self.prediction_system:
                    self.prediction_system.make_prediction()
                else:
                    print("Model is not trained yet. Please train the model first.")
            elif choice == '4':
                print("Exiting the system. Have a great day!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    system = MalwareDetectionSystem()
    system.menu()
