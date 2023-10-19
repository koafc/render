from flask import Flask, render_template, request, jsonify
import replicate

app = Flask(__name__)

@app.route("/")
def test_api_key():
  """Tests whether the Replicate.com API key is working properly.

  Returns:
    A JSON object with the message "Replicate.com API key is valid." or
    "Replicate.com API key is invalid."
  """

  try:
    # Run a simple model to test the API key.
    replicate.run("stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478", input={"prompt": "a 19th century portrait of a wombat gentleman"})
    return jsonify({"message": "Replicate.com API key is valid."})
  except Exception as e:
    print(e)
    return jsonify({"message": "Replicate.com API key is invalid."})

if __name__ == "__main__":
  app.run(debug=True)
