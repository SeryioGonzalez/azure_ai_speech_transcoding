import os
import sys

import helper

if len(sys.argv) > 1:
    mp4_file_path = sys.argv[1]
    
    if os.path.exists(mp4_file_path):
        print(f"Transcribing {mp4_file_path}")
        helper.mp4_file_stream_helper(mp4_file_path)
    else:
        print(f"File {mp4_file_path} does not exist. Please check input")
else:
    print("Please specify an input mp4 file")
