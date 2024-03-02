import os
import sys

import helper

if len(sys.argv) > 1:
    mp3_file_path = sys.argv[1]
    
    if os.path.exists(mp3_file_path):
        print(f"Transcribing {mp3_file_path} ")
        helper.mp3_file_stream_helper(mp3_file_path)
    else:
        print(f"File {mp3_file_path} does not exist. Please check input")
else:
    print("Please specify an input mp3 file")

