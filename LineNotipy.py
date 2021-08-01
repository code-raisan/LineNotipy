import requests

class LineNotipy:
    API_END_POINT = "https://notify-api.line.me/api/notify"

    def __init__(self, TOKEN: str) -> None:
        self.API_TOKEN = TOKEN
        return None
    
    def send(self, message: str,) -> dict:
        headers = {"Authorization": f"Bearer {self.API_TOKEN}"}
        payload = {"message": message}
        r = requests.post(self.API_END_POINT, headers=headers, params=payload)
        return r.json()