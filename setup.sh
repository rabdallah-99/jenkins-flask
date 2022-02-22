#! /bin/bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
if (-d jenkins-flask ) 
  then 
         git clone https://github.com/rabdallah-99/jenkins-flask
fi
cd jenkins-flask
python3 -m venv
. ./venv/bin/activate
pip3 install -r requirements.txt

