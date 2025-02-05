import joblib

class ModelPredictor:
    def __init__(self, model_path):  
        self.model = joblib.load(model_path)

    def Predict(self, circuit_value):
        predicted_real = self.model.predict([[circuit_value]])[0]
        return predicted_real

# Example usage (optional)
if __name__ == "__main__":
    pass
