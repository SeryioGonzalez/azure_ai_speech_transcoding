source .env

speech_region=$(echo "$speech_region" | tr -d '\r')

endpoint_response_code=$(curl -o /dev/null -s -w "%{http_code}\n" https://$speech_region.tts.speech.microsoft.com/cognitiveservices/voices/list --header "Ocp-Apim-Subscription-Key: $speech_key" )

if [ $endpoint_response_code = 200 ]
then
    echo "API IS OK"
else
    echo "ERROR IN API"
fi