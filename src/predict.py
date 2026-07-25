import joblib
import pandas as pd


class PredictionPipeline:

    def __init__(self):
        self.model = joblib.load("artifacts/model.pkl")
        self.encoder = joblib.load("artifacts/encoder.pkl")

    def predict(self, garment_type, order_quantity, num_stitch_operations):

        garment = self.encoder.transform([garment_type])[0]

        data = pd.DataFrame({
            "garment_type": [garment],
            "order_quantity": [order_quantity],
            "num_stitch_operations": [num_stitch_operations]
        })

        prediction = self.model.predict(data)

        return round(float(prediction[0]), 2)