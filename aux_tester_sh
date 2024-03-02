
source config.sh

echo "Testing MP3 file"
python3 transcriber_mp3_file.py $mp3_file
echo ""

echo "Testing MP4 file"
python3 transcriber_mp4_file.py $mp4_file
echo ""

echo "Testing WAV file"
python3 transcriber_wav_file.py $wav_file
echo ""

echo "Testing WAV input"
ffmpeg -loglevel quiet -re -i $mp4_file -vn -ac 1 -c:a pcm_s16le -ar 16000 -f wav - | python transcriber_wav_stdin.py 
echo ""