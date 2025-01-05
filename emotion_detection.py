import requests
import json



def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    dataObj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url,json = dataObj, headers = header)
    formatted_response=json.loads(response.text)

    result_data = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion_value = 0.0
    dominant_emotion = ""
    for key,value in result_data.items():
        if(dominant_emotion_value < value):
           dominant_emotion_value = value
           dominant_emotion = key
        
    result_data["dominant_emotion"] = dominant_emotion

    return result_data
