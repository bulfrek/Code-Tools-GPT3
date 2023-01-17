# OpenAI-Code-Tools
This repository generate a web page with code tools using the OpenAI API.

### Warning ! 
This application must remain in your local network, no security measures have been taken and it may have major vulnerabilities.

## Enter your API KEY 

To access the openai API youn need to enter you api key here on the server.py file.

```
  openai.api_key = "ENTER YOUR API KEY HERE"
```
You can find this key here : https://beta.openai.com/account/api-keys

This repo also includes a script to replace the API key and build or rebuild the docker file automatically :

```

bash replace_api.sh

```

## Without Docker

Before running the server, make sure you have all the requirements :

```
pip install -r requirements.txt
```

To run the server, simply run the command :

```
python3 server.py
```

## With Docker 

Build the image from the Dockerfile :

```
docker build -t my-flask-app .
```

Run the server in detached mode with the right port :

```
docker run -d -p 5000:5000 my-flask-app
```

## Access the app 

To access the app paste into your web browser :

```
localhost:5000
```

If you are running this app on an other device, replace localhost whith your server IP or domain name

