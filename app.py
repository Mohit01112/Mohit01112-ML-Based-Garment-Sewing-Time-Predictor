from flask import Flask, render_template, request, jsonify
from src.predict import PredictionPipeline

app = Flask(__name__)

pipeline = PredictionPipeline()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    prediction = pipeline.predict(
        garment_type=data["garment_type"],
        order_quantity=int(data["order_quantity"]),
        num_stitch_operations=int(data["num_stitch_operations"])
    )

    return jsonify({
        "predicted_time": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)