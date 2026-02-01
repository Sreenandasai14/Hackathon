from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

# Ensure JSON file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/advisory", methods=["POST"])
def advisory():
    data = request.get_json()

    crop = data.get("crop")
    stage = data.get("stage")
    weather = data.get("weather")

    # RULE BASED ENGINE
    if stage == "sowing":
        message = "Apply light irrigation and organic manure."
    elif stage == "vegetative":
        message = "Moderate irrigation with nitrogen nutrients."
    elif stage == "flowering":
        if weather == "rainy":
            message = "Avoid irrigation. Disease risk high."
        else:
            message = "Normal irrigation and pest monitoring."
    elif stage == "harvest":
        message = "Reduce water and prepare for harvest."
    else:
        message = "Invalid input."

    record = {
        "crop": crop,
        "stage": stage,
        "weather": weather,
        "advisory": message
    }

    # ✅ SAFE JSON WRITE
    with open(DATA_FILE, "r") as f:
        records = json.load(f)

    records.append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)
