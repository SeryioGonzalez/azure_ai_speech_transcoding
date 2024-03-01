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

<<<<<<< HEAD
=======
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

>>>>>>> main
def print_srt(srt_sequence, start_time, end_time, srt_text):
    print(srt_sequence)
    print(f"{start_time} --> {end_time}")
    print(srt_text)
    print("")
<<<<<<< HEAD
    
=======

>>>>>>> main

def speech_recognition_with_pull_stream(log_file=None):
    wave_callback = WavInputStreamReaderCallback()
    wave_format = speech_sdk.audio.AudioStreamFormat(samples_per_second=wave_callback.get_frame_rate(), bits_per_sample=wave_callback.get_bits_per_sample(), channels=wave_callback.get_num_channels())
    wave_stream = speech_sdk.audio.PullAudioInputStream(wave_callback, wave_format)
    
    audio_config = speech_sdk.audio.AudioConfig(stream=wave_stream)
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

    speech_config.set_property(property_id = speech_sdk.PropertyId.SpeechServiceResponse_StablePartialResultThreshold, value="5")
<<<<<<< HEAD
    speech_config.set_property(property_id = speech_sdk.PropertyId.SpeechServiceResponse_PostProcessingOption, value="TrueText")

=======
    speech_config.output_format = speech_sdk.OutputFormat.Detailed
 
    speech_config.request_word_level_timestamps()
    
>>>>>>> main
    if log_file is not None:
        speech_config.enable_audio_logging()
        speech_config.set_property(speech_sdk.PropertyId.Speech_LogFilename, log_file)

    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    done = False
    def stop_cb(evt: speech_sdk.SessionEventArgs):
        """callback that signals to stop continuous recognition upon receiving an event `evt`"""
        nonlocal done
        done = True

<<<<<<< HEAD
    srt_sequence = 1
=======
    srt_sequence = 0
>>>>>>> main
    def generate_srt(evt: speech_sdk.SessionEventArgs):
        start_time = helper.timestamp_from_ticks(evt.result.offset)
        end_time   = helper.timestamp_from_ticks(evt.result.offset + evt.result.duration)
        srt_text   = evt.result.text

        nonlocal srt_sequence

        print_srt(srt_sequence, start_time, end_time, srt_text)
        
        srt_sequence += 1

    # Connect callbacks to the events fired by the speech recognizer
    speech_recognizer.recognizing.connect(generate_srt)
        
    # Start continuous speech recognition
    speech_recognizer.start_continuous_recognition()

    while not done:
        time.sleep(.1)

    speech_recognizer.stop_continuous_recognition()
    

speech_recognition_with_pull_stream()