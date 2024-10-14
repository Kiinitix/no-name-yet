import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class DataLoader:
    def __init__(self):
        self.data = None

    def load_dataset(self):
        print("\nLoading dataset...")
        dataset = load_iris()
        self.data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        self.data['target'] = dataset.target
        print("Dataset loaded successfully!")

    def display_sample_data(self):
        if self.data is not None:
            print("\nHere’s a glimpse of the dataset:")
            print(self.data.head(), "\n")
        else:
            print("No data to display. Please load the dataset first.\n")

    def preprocess_data(self):
        if self.data is not None:
            print("\nPreprocessing data...")
            X = self.data.drop('target', axis=1)
            y = self.data['target']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            print("Data preprocessing complete.")
            return X_train, X_test, y_train, y_test
        else:
            print("Dataset not loaded. Please load the dataset first.")
            return None, None, None, None
