source config.sh

function check_mp4_file_present {
    if [ -f $mp4_file ]
    then
        ffprobe -v error  -show_streams -select_streams v:0 -of default=noprint_wrappers=1 $mp4_file | grep codec_long_name | grep MPEG-4 > /dev/null
        return $?
    else
        return 1
    fi

}

echo "Purging folder $media_folder"
find $media_folder -type f -name $media_file_prefix"*" -exec rm {} \;

echo "Loading an MP4 file into $mp4_file"
ffmpeg -loglevel quiet  -i $input -ss "00:00:00" -t $duration_for_sources_in_seconds -f mp4 $mp4_file

if check_mp4_file_present
then
    input=$mp4_file
fi

echo "Loading an MP3 file into $mp3_file"
ffmpeg -loglevel quiet -i $input -vn -ac 1 -f mp3 $mp3_file

echo "Loading an WAV file into $wav_file"
ffmpeg -loglevel quiet -i $input -vn -ac 1 -f wav $wav_file