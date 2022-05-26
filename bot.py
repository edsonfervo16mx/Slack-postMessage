import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
channel = os.getenv('CHANNEL')
headers = {'Authorization': 'Bearer {}'.format(token)}


def postMessage(text):
    data = {
        "channel": channel,
        "text": text
    }
    url = 'https://slack.com/api/chat.postMessage'
    response = requests.post(url, data=data, headers=headers)
    return response


if __name__ == '__main__':
    result = postMessage("Hello World from Python Script")
    print(result)
