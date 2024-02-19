from dotenv import load_dotenv
import os
import sys
import time

import azure.cognitiveservices.speech as speech_sdk

load_dotenv()
speech_key      = os.environ['speech_key']
speech_region   = os.environ['speech_region']
speech_language = os.environ['speech_language']

if speech_language == "":
    print("Please create a file named .env with the following variables")
    print("speech_key")
    print("speech_region")
    print("speech_language")
    sys.exit(1)

def file_stream_helper(wav_file_path):
    
    # Configure speech service
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)
    audio_config = speech_sdk.audio.AudioConfig(filename=wav_file_path)

    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speech_sdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speech_sdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speech_sdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speech_sdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")


    print(result.text)

if len(sys.argv) > 1:
    wav_file_path = sys.argv[1]
    if os.path.exists(wav_file_path):
        print(f"Transcribing {wav_file_path} in batch")
        file_stream_helper(wav_file_path)
    else:
        print(f"File {wav_file_path} does not exist. Please check input")
else:
    print("Please specify an input wav file")

