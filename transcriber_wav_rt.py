from dotenv import load_dotenv
import os
import sys
import time
import wave
import io

import azure.cognitiveservices.speech as speech_sdk
import helper


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

class WavInputStreamReaderCallback(speech_sdk.audio.PullAudioInputStreamCallback):
    """Example class that implements the Pull Audio Stream interface to recognize speech from
    an audio stream."""
    
    def get_num_channels(self):
        return self._file_h.getnchannels()

    def get_frame_rate(self):
        return self._file_h.getframerate()

    def get_bits_per_sample(self):
        return (self._file_h.getsampwidth()*8)    

    def __init__(self):
        super().__init__()
        self._file_h = wave.open(sys.stdin.buffer, mode='rb')
        
    def read(self, buffer: memoryview) -> int:
        """read callback function"""
        size = buffer.nbytes
        frames = self._file_h.readframes(size // self._file_h.getsampwidth())
        buffer[:len(frames)] = frames

        return len(frames)

    def close(self):
        """close callback function"""
        self._file_h.close()
        self._stream.close()

    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)


def get_timestamp(start : time, end : time) -> str :
    time_format = "%H:%M:%S.%f"
    # Truncate microseconds to milliseconds.
    return "{} --> {}".format(start.strftime(time_format)[:-3], end.strftime(time_format)[:-3])

def caption_from_real_time_result(result):
    start_time = helper.time_from_ticks(result.offset)
    end_time = helper.time_from_ticks(result.offset + result.duration)

    timestamp = get_timestamp(start_time, end_time)

    print(f"Recognized {timestamp}")


def generate_srt(evt: speech_sdk.SessionEventArgs):
    #start_time = helper.time_from_ticks(evt.result.offset)
    #start_time = evt.result.offset
    #end_time = helper.time_from_ticks(result.offset + result.duration)

    #caption_from_real_time_result(evt.result)
    #print(f"Text {evt.result.text} in offset {evt.result.offset}")
    print(f"offset {evt.result.duration}")
    

def speech_recognition_with_pull_stream():
    wave_callback = WavInputStreamReaderCallback()
    wave_format = speech_sdk.audio.AudioStreamFormat(samples_per_second=wave_callback.get_frame_rate(), bits_per_sample=wave_callback.get_bits_per_sample(), channels=wave_callback.get_num_channels())
    wave_stream = speech_sdk.audio.PullAudioInputStream(wave_callback, wave_format)
    
    audio_config = speech_sdk.audio.AudioConfig(stream=wave_stream)
    
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

    speech_config.set_property(property_id = speech_sdk.PropertyId.SpeechServiceResponse_StablePartialResultThreshold, value="5")
    speech_config.set_property(property_id = speech_sdk.PropertyId.SpeechServiceResponse_PostProcessingOption, value="TrueText")
    #speech_config.enable_audio_logging()
    #speech_config.set_property(speech_sdk.PropertyId.Speech_LogFilename, "logger.log")

    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    done = False
    def stop_cb(evt: speech_sdk.SessionEventArgs):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        nonlocal done
        done = True

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(generate_srt)
        
    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.1)

    speech_recognizer.stop_continuous_recognition()
    

speech_recognition_with_pull_stream()