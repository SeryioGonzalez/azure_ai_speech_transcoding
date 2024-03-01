#input="https://rr3---sn-h5qzened.googlevideo.com/videoplayback?expire=1709222888&ei=iFfgZeSjFeKtp-oPgYKtoAw&ip=81.44.43.9&id=o-AGHSMhKby1uNINHGimahlr2Un39Zm5uDSTP7BOIZEGEc&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=dO&mm=31%2C26&mn=sn-h5qzened%2Csn-4g5edn6y&ms=au%2Conr&mv=m&mvi=3&pl=19&initcwndbps=1053750&spc=UWF9fzV69khfCz0ax_WQKCUeQGh0xsHCBvOkIA2d7Nj3qZQ&vprv=1&svpuc=1&mime=video%2Fmp4&ns=6LKKOBR5RKEB8Aki5Kg5SsAQ&cnr=14&ratebypass=yes&dur=74.884&lmt=1687637896132458&mt=1709200615&fvip=4&fexp=24007246&c=WEB&sefc=1&txp=1438434&n=DeDkJtO9-H_QQSbQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAJqVXr2ogRiUPMUNhDCr5erLj302-s0iE9l-4tM99OJYAiAi_N88R929ZGWFAg8nwI4HoU5PkR9sJyQDlNuVwtmy0Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=APTiJQcwRQIgFmPfybJlt5KZqXajHO4q1OJAg1d4wB1kcbNoiulEHNACIQCPxEcd7YJ74-nsFIytVn94fGpuyQtMxhrSmluC1xeojQ%3D%3D"
input="media/input.wav"

export SSL_CERT_DIR=/usr/lib/ssl/certs

echo "Starting stream to wav"
ffmpeg -loglevel quiet -re -i $input -vn -ac 1 -c:a pcm_s16le -ar 16000 -f wav - | python transcriber_wav_rt.py

