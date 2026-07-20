"""Flask Server for emotion detection"""

#Import Flask and other required functions
from flask import Flask, render_template, request
#Import the emotion detector function from emotion detection package
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index():
    """Render index Page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detection():
    """Emotion Detection Function to generate the out put"""
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}.")

if __name__=="__main__":
    app.run()
