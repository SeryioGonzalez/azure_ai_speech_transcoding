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

class BinaryFileReaderCallback(speech_sdk.audio.PullAudioInputStreamCallback):
    def __init__(self, filename: str):
        super().__init__()
        self._file_h = open(filename, "rb")

    def read(self, buffer: memoryview) -> int:
        try:
            size = buffer.nbytes
            frames = self._file_h.read(size)

            buffer[:len(frames)] = frames
        
            return len(frames)
        except Exception as ex:
            print('Exception in `read`: {}'.format(ex))
            raise

    def close(self) -> None:
        print('closing file')
        try:
            self._file_h.close()
        except Exception as ex:
            print('Exception in `close`: {}'.format(ex))
            raise


def file_stream_helper(mp3_file_path):
    callback = BinaryFileReaderCallback(mp3_file_path)
    compressed_format = speech_sdk.audio.AudioStreamFormat(compressed_stream_format=speech_sdk.AudioStreamContainerFormat.MP3)
    stream = speech_sdk.audio.PullAudioInputStream(stream_format=compressed_format, pull_stream_callback=callback)
    
    # Configure speech service
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)
    audio_config = speech_sdk.audio.AudioConfig(stream=stream)

    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    done = False

    def stop_cb(evt):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt.result.reason))
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt.result.text)))
    #speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED'))
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED'))
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED'))
    # stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()
    while not done:
        time.sleep(.5)

    speech_recognizer.stop_continuous_recognition()


if len(sys.argv) > 1:
    mp3_file_path = sys.argv[1]
    if os.path.exists(mp3_file_path):
        print(f"Transcribing {mp3_file_path} ")
        file_stream_helper(mp3_file_path)
    else:
        print(f"File {mp3_file_path} does not exist. Please check input")
else:
    print("Please specify an input mp3 file")

