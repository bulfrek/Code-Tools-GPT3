#!/bin/bash
echo "Enter your OpenAI API key:"
read api_key

sed -i "s/openai.api_key = \".*\"/openai.api_key = \"$api_key\"/g" server.py

container=$( sudo docker ps | grep "my-flask-app" | awk '{print $1}')

if [[ $container ]]; then

    #remove previous container

    sudo docker rm -f $container

    sudo docker rmi -f my-flask-app
    
fi

#build container from Dockerfile

sudo docker build -t my-flask-app .

sudo docker run -d -p 5000:5000 my-flask-app