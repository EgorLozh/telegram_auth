import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()

LOGIN_ENDPOINT='/api/auth/login/'
CREATE_USER_ENDPOINT='/api/auth/user/'



async def post_request(data, sessionid=None):
    url = os.getenv('APP_URL') + CREATE_USER_ENDPOINT
    csrf_token = None

    async with aiohttp.ClientSession(cookies={'sessionid': sessionid}) as session:
        async with session.get(os.getenv('APP_URL')) as response:
            csrf_token = response.cookies.get('csrftoken').value

        headers = {'X-CSRFToken': csrf_token}
        async with session.post(url, json=data, cookies={'sessionid': sessionid}, headers=headers) as response:
            return await response.json()
