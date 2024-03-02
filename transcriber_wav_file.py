import os
import sys

import helper

if len(sys.argv) > 1:
    wav_file_path = sys.argv[1]
    
    if os.path.exists(wav_file_path):
        print(f"Transcribing {wav_file_path}")
        helper.wav_file_helper(wav_file_path)
    else:
        print(f"File {wav_file_path} does not exist. Please check input")
else:
    print("Please specify an input wav file")

