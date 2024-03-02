# Azure Speech to Text Transcription

This repo shows how to implement a real time transcription using [Azure AI Speech service](https://azure.microsoft.com/en-us/products/ai-services/ai-speech).
We will be using the Python SDK. 4 different scripts have been implemented making use of a common helper module.
The scenarios covered are:
- Transcription from an MP3 audio file
- Transcription from an MP4 video file
- Transcription from a WAV audio file
- Transcription from a WAV audio input stream

## Define Azure AI Speech variables
Create an .env file or enable the following values as system variables:
```
speech_key="YOUR_SPEECH_SERVICE_KEY"
speech_region="YOUR_SPEECH_SERVICE_REGION"
speech_language="en-us" #YOUR DESIRE LANGUAGE
```


## Install dependencies:
Install packages and depencies with the following script
```
./aux_installer.sh
```

## Load video content:
Load video content in the media folder using the following script. The source is defined in the [config.sh](https://github.com/SeryioGonzalez/azure_ai_speech_transcoding/blob/main/config.sh) file in the *input* variable.
```
./aux_content_generator.sh
```

## Test all sources:
A use case for each of the 4 scenarios listed above are implemented in the script [aux_tester.sh](https://github.com/SeryioGonzalez/azure_ai_speech_transcoding/blob/main/aux_tester.sh)
```
./aux_tester.sh

Testing MP3 file
Transcribing media/input.mp3 
SESSION STARTED
RECOGNIZING: if you're
RECOGNIZING: if you're a
.......
```

