from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotional Detector")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze=request.args.get("textToAnalyze")

    response=emotion_detector(text_to_analyze)

    return '''For the given statement, the system response is 
    'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.
    '''.format(response["anger"],response["disgust"],response["fear"],response["joy"],response["sadness"],response["dominant_emotion"])


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)