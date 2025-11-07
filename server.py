"""Flask server for Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the main web interface."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detect():
    """Handle emotion detection requests and return formatted results."""
    text_to_analyze = request.form["text"]

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get("dominant_emotion")

    if dominant_emotion is None:
        return render_template(
            "index.html",
            error_message="Invalid text! Please try again!"
        )

    return render_template(
        "index.html",
        text=text_to_analyze,
        response=response,
        dominant_emotion=dominant_emotion
    )


if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000)
