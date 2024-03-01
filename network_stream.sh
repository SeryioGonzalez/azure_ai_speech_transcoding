
input_stream="https://rr4---sn-h5qzened.googlevideo.com/videoplayback?expire=1709333904&ei=MAniZb3FE5_ZxN8Pn-KgiA8&ip=81.44.43.9&id=o-AK4PHQRYMof80m2KhvX7c50UsosyiYFe1AyoaBFNwy9H&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=rY&mm=31%2C29&mn=sn-h5qzened%2Csn-h5q7knld&ms=au%2Crdu&mv=m&mvi=4&pl=19&initcwndbps=1383750&spc=UWF9f52QpOSOSCWFzkPD52A-4ijcZ31gkUHbFpcBY2iGyWQ&vprv=1&svpuc=1&mime=video%2Fmp4&ns=QakvrU0FBhxVvPDSdU3g3kUQ&cnr=14&ratebypass=yes&dur=43.537&lmt=1709115351394936&mt=1709312024&fvip=3&fexp=24007246&c=WEB&sefc=1&txp=6308224&n=a2eXHU6zip5MUUaNJ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRAIgEYLIAMOH7P3Nvh8RMIfKo7b0z9brLxklhM5vmDxDi2MCIBYPA4niOSEH0TEr9x39HE42HX_F8oVUc0o6k9yeBBUU&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=APTiJQcwRgIhAKIU8JIvhFIcha6yPI8OupZgN4q4J-PC0EipvSrJIY1_AiEAl9QXhM0c0yXnkPFxk9BsYg-fTlc2ejG9fASuEtj4NBw%3D"
#input_stream="media/output.mp4"

output_format="mp4"
output_file="media/output.mp4"

fifo_name="myfifo.fifo"

if [ -p $fifo_name ]
then
    rm $fifo_name
fi

echo "Creating FiFo $fifo_name"
mkfifo $fifo_name

if [ -f $output_file ]
then
    rm $output_file
fi
set -e
echo "Streaming content"
#ffmpeg -loglevel quiet -re -sn -i $input_stream -c:v copy -c:a copy -f flv - | flv+srt - $fifo_name - | ffmpeg -loglevel quiet -y -i - -c:v copy -c:a copy -metadata:s:s:0 language=eng -f $output_format $output_file &
#ffmpeg -loglevel quiet -re -i $input_stream -vn -ac 1 -c: pcm_s16le -ar 16000 -f wav - | python transcriber_wav_rt.py > $fifo_name

echo "Reading subtitles"
ffmpeg -loglevel quiet -re -i $input_stream -vn -ac 1 -c: pcm_s16le -ar 16000 -f wav - | python transcriber_wav_rt.py  > out.srt
