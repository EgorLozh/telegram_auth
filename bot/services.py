import os
import time
from dotenv import load_dotenv
import aiohttp
import requests

load_dotenv()

LOGIN_ENDPOINT='/api/auth/login/'
CREATE_USER_ENDPOINT='/api/auth/user/'


def get_sessionid():

    url = os.getenv('APP_URL') + LOGIN_ENDPOINT
    data = {'username': os.getenv('ADMIN_NAME'), 'password': os.getenv('ADMIN_PASSWORD')}
    try:
        response = requests.post(url, data=data)
    except requests.exceptions.ConnectionError:
        time.sleep(15)  # wait for main app to start
        response = requests.post(url, data=data)

    return response.json()['session']


async def post_request(data, sessionid):
    url = os.getenv('APP_URL') + CREATE_USER_ENDPOINT
    csrf_token = None

    async with aiohttp.ClientSession(cookies={'sessionid': sessionid}) as session:
        async with session.get(os.getenv('APP_URL')) as response:
            csrf_token = response.cookies.get('csrftoken').value

        headers = {'X-CSRFToken': csrf_token}
        async with session.post(url, json=data, cookies={'sessionid': sessionid}, headers=headers) as response:
            return await response.json()
