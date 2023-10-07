import pickle
import pandas as pd
from flask import Flask
from flask import request, jsonify

model_path = "saved_model.pkl"


def load_model(model_path=model_path):
    with open(model_path, "rb") as fin:
        (model, dv) = pickle.load(fin)
        return (model, dv)


model, dv = load_model()

app = Flask("titanic")


@app.route("/predict", methods=["POST"])
def predict():
    passenger = request.get_json()
    df_dv = dv.transform(passenger)
    predicted_prob = model.predict_proba(df_dv)[0, 1]
    disaster = predicted_prob > 0.1
    result = {"disaster_probability": float(predicted_prob), "disaster": bool(disaster)}
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
