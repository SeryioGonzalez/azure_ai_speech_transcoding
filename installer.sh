sudo apt-get update -y
sudo apt-get install python3 -y 
sudo apt-get install python3-pip -y 
sudo apt-get install python-is-python3 -y 
sudo apt-get install ffmpeg -y
sudo apt-get install cmake -y

pip install -r requirements.txt

mkdir media

cd libcaption 
cmake . && make
sudo make install
