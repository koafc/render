import datetime
from flask import Flask, render_template, request, jsonify
import replicate
from pydantic import BaseModel

class Prediction(BaseModel):
    id: str
    started_at: datetime.datetime
    completed_at: datetime.datetime

app = Flask(__name__)

@app.route("/")
def test_api_key():
  """Tests whether the Replicate.com API key is working properly.

  Returns:
    A JSON object with the message "Replicate.com API key is valid." or
    "Replicate.com API key is invalid."
  """

  try:
    # Create a Prediction object.
    prediction = Prediction(id="prediction-id", started_at=datetime.datetime.now(), completed_at=datetime.datetime.now())

    # Run the prediction without the output keyword argument.
    replicate.run("stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478", input={"prompt": "a 19th century portrait of a wombat gentleman"})

    return jsonify({"message": "Replicate.com API key is valid."})
  except Exception as e:
    print(e)
    return jsonify({"message": "Replicate.com API key is invalid."})

if __name__ == "__main__":
  app.run(debug=True)
