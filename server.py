"""flask module EmotionDetection module"""
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotional Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Analyze text with emotion_detector and sends response"""
    text_to_analyze=request.args.get("textToAnalyze")

    response=emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        result_response = "Invalid text! Please try again!"
    else:
        result_response = f'''For the given statement, the system response is
                'anger': {response["anger"]}, 'disgust': {response["disgust"]},
                'fear': { response["fear"]}, 'joy': {response["joy"]}
                and 'sadness': {response["sadness"]}.
                The dominant emotion is {response["dominant_emotion"]}.
                '''
    return result_response

@app.route("/")
def render_index_page():
    """Render intro ui template"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
