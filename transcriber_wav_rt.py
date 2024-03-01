from dotenv import load_dotenv
import os
import sys
import time
import wave
import io

import azure.cognitiveservices.speech as speech_sdk

load_dotenv()
speech_key      = os.environ['speech_key']
speech_region   = os.environ['speech_region']
speech_language = os.environ['speech_language']

wav_samples_per_second = 16000
wav_channels = 1
wav_bits_per_sample = 16

if speech_language == "":
    print("Please create a file named .env with the following variables")
    print("speech_key")
    print("speech_region")
    print("speech_language")
    sys.exit(1)

def speech_recognition_with_pull_stream():
    class WavInputStreamReaderCallback(speech_sdk.audio.PullAudioInputStreamCallback):
        """Example class that implements the Pull Audio Stream interface to recognize speech from
        an audio stream."""
        
        def check_stream(self):
            # Quality checks
            assert self._file_h.getnchannels() == wav_channels
            assert self._file_h.getframerate() == wav_samples_per_second
            assert self._file_h.getsampwidth() == int(wav_bits_per_sample/8)
            assert self._file_h.getcomptype() == 'NONE'

        def __init__(self):
            super().__init__()
            self._stream = io.BytesIO(sys.stdin.buffer.read())
            self._file_h = wave.open(self._stream, mode='rb')
                       
            # Quality checks
            self.check_stream()
           
        def read(self, buffer: memoryview) -> int:
            """read callback function"""
            size = buffer.nbytes
            #print("Reading")
            frames = self._file_h.readframes(size // self._file_h.getsampwidth())
            buffer[:len(frames)] = frames

            return len(frames)

        def close(self):
            """close callback function"""
            self._file_h.close()
            self._stream.close()

        speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

    # Specify the audio format
    wave_format = speech_sdk.audio.AudioStreamFormat(samples_per_second=wav_samples_per_second, bits_per_sample=wav_bits_per_sample, channels=wav_channels)

    # Setup the audio 
    callback = WavInputStreamReaderCallback()
    stream = speech_sdk.audio.PullAudioInputStream(callback, wave_format)
    audio_config = speech_sdk.audio.AudioConfig(stream=stream)
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

    speech_config.enable_audio_logging()
    speech_config.set_property(speech_sdk.PropertyId.Speech_LogFilename, "logger.log")

    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    done = False

    def stop_cb(evt: speech_sdk.SessionEventArgs):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        print('CLOSING on {}'.format(evt))
        nonlocal done
        done = True

    print("Configuring event call backs")

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt.result.text)))
    
    # Stop continuous recognition on either session stopped or canceled events
    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.5)

    speech_recognizer.stop_continuous_recognition()

print("Creating recognition flow")
speech_recognition_with_pull_stream()