
input="media/input.wav"
#input="https://rr2---sn-h5q7knel.googlevideo.com/videoplayback?expire=1709318675&ei=s83hZeODA_Wqp-oPmoKR0A8&ip=81.44.43.9&id=o-AAVz0vuMvRZECpSma5QFJwx1qisACtxOhJkIPoH3NW-_&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=uP&mm=31%2C29&mn=sn-h5q7knel%2Csn-h5qzen7s&ms=au%2Crdu&mv=m&mvi=2&pl=19&initcwndbps=1108750&spc=UWF9f3HPKyt1HlPMWqnL6A0x8ajXCQ1P3qxsSX27G-HIgb4&vprv=1&svpuc=1&mime=video%2Fmp4&ns=b4Q8iFJUaMHajx9_MqwL7G4Q&cnr=14&ratebypass=yes&dur=663.417&lmt=1709262307615623&mt=1709295924&fvip=4&fexp=24007246&c=WEB&sefc=1&txp=5308224&n=uJaJPByyp1xQ7lonX&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIgVQYCwBDU1UKhSNWjJi6k7JwVriJIJtFzxItQmHhQWHoCIQDY-7zlnMaiQLYnkei-f01R1ER7n-IY5oEXr-_8mGiwmA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=APTiJQcwRQIhAIa7yd5Q2VK21rs-NUCdX0ww0Jq4G3TgsLXW1i72aw7-AiB741HJchCsbvHxkIfsr8IYJh30KoFVwbplwJ-sFFDYhg%3D%3D"

export SSL_CERT_DIR=/usr/lib/ssl/certs

ffmpeg -loglevel quiet -re -i $input -vn -ac 1 -c: pcm_s16le -ar 16000 -f wav - | python transcriber_wav_rt.py

