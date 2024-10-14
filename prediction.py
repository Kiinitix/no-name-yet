from utils import validate_user_input, convert_input_to_float

class PredictionSystem:
    def __init__(self, model):
        self.model = model

    def make_prediction(self):
        if self.model is not None:
            print("\nEnter feature values for prediction (comma separated):")
            user_input = input().split(',')
            if validate_user_input(user_input, self.model.n_features_in_):
                user_input_float = convert_input_to_float(user_input)
                if user_input_float is not None:
                    prediction = self.model.predict([user_input_float])
                    print(f"Prediction result: {'Malicious' if prediction[0] == 1 else 'Benign'}\n")
        else:
            print("Model is not trained yet. Please train the model first.")
