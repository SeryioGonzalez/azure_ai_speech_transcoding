
from dotenv import load_dotenv
import os
import subprocess
import sys
import time
import wave

import azure.cognitiveservices.speech as speech_sdk

def get_speech_config():
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

    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region, speech_recognition_language=speech_language)

    return speech_config

def run_recognizer_with_callback(pull_stream_callback, stream_format):
    stream = speech_sdk.audio.PullAudioInputStream(stream_format=stream_format, pull_stream_callback=pull_stream_callback)
    audio_config = speech_sdk.audio.AudioConfig(stream=stream)
    _run_recognizer(audio_config)

def _run_recognizer(audio_config):
    az_ai_speech_config = get_speech_config()
    
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config=az_ai_speech_config, audio_config=audio_config)

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

def wav_file_helper(wav_file_path):
    audio_config = speech_sdk.audio.AudioConfig(filename=wav_file_path)
    
    # Get audio config and run recognizer
    _run_recognizer(audio_config)

def mp3_file_stream_helper(mp3_file_path):
    callback = BinaryFileReaderCallback(mp3_file_path)
    compressed_format = speech_sdk.audio.AudioStreamFormat(compressed_stream_format=speech_sdk.AudioStreamContainerFormat.MP3)
    
    run_recognizer_with_callback(callback, compressed_format)

def mp4_file_stream_helper(mp4_file_path):
    callback = VideoFileReaderCallback(mp4_file_path)
    compressed_format = speech_sdk.audio.AudioStreamFormat(compressed_stream_format=speech_sdk.AudioStreamContainerFormat.ANY)

    run_recognizer_with_callback(callback, compressed_format)

def wav_input_stream_helper():
    callback = WavInputStreamReaderCallback()
    wave_format = speech_sdk.audio.AudioStreamFormat(samples_per_second=callback.get_frame_rate(), bits_per_sample=callback.get_bits_per_sample(), channels=callback.get_num_channels())
    
    run_recognizer_with_callback(callback, wave_format)

class VideoFileReaderCallback(speech_sdk.audio.PullAudioInputStreamCallback):
    def extract_audio_from_mp4(self, video_file_name):
        """
        Extracts the audio from an MP4 file and saves it as an audio file using ffmpeg.

        Args:
        video_file (str): Path to the MP4 video file.
        output_audio_file (str): Path for the output audio file (e.g., 'output_audio.mp4').
        """
        # Command to extract audio using ffmpeg
        output_audio_file_name = "tmp." + "".join(video_file_name.split(".")[0:-1]) + ".audio"

        audio_check_command = ['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_name', '-of', 'default=noprint_wrappers=1:nokey=1', '-select_streams', 'a', video_file_name]
        audio_extension = subprocess.run(audio_check_command, text=True, capture_output=True).stdout.split('\n', 1)[0]

        output_audio_file_name = "".join(video_file_name.split(".")[0:-1]) + ".audio." + audio_extension 

        print(f"Audio output from {video_file_name} is {output_audio_file_name}")

        conversion_command = ['ffmpeg', '-loglevel', 'error', '-i', video_file_name, '-vn', '-acodec', 'copy', output_audio_file_name, '-y']
        
        # Execute the command
        subprocess.run(conversion_command)

        return output_audio_file_name

    
    def __init__(self, video_file_name: str):
        super().__init__()
        
        audio_file_name = self.extract_audio_from_mp4(video_file_name)
        self._file_h = open(audio_file_name, "rb")

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