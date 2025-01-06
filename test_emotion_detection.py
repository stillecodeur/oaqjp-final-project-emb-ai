from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    
    def test_emotion_detector(self):
        test1_result=emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(test1_result,"joy")

        test2_result=emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(test2_result,"anger")

        test3_result=emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(test3_result,"disgust")

        test4_result=emotion_detector("I am so sad about this	")["dominant_emotion"]
        self.assertEqual(test4_result,"sadness")

        test5_result=emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(test5_result,"fear")


unittest.main()