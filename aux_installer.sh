sudo apt-get update -y
sudo apt-get install python3 -y 
sudo apt-get install python3-pip -y 
sudo apt-get install python-is-python3 -y 
sudo apt-get install ffmpeg -y

sudo apt-get install gstreamer1.0-plugins-bad -y 
sudo apt-get install gstreamer1.0-plugins-base -y 
sudo apt-get install gstreamer1.0-plugins-good -y 
sudo apt-get install gstreamer1.0-plugins-ugly -y 

pip install -r aux_requirements.txt

source config.sh
mkdir $media_folder
