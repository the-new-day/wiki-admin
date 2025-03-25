import requests
import json

with open("config.json", "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

class WikiClient:
    def __init__(self):
        self.session = requests.Session()
        self.url = CONFIG["wiki_url"]
        self.username = CONFIG["username"]
        self.password = CONFIG["password"]
        self.edit_token = None

    def login(self):
        token_resp = self.session.get(f"{self.url}/api.php", params={
            "action": "query", "meta": "tokens", "type": "login", "format": "json"
        }).json()
        login_token = token_resp["query"]["tokens"]["logintoken"]

        login_resp = self.session.post(f"{self.url}/api.php", data={
            "action": "login",
            "lgname": self.username,
            "lgpassword": self.password,
            "lgtoken": login_token,
            "format": "json"
        }).json()
        
        if login_resp.get("login", {}).get("result") != "Success":
            raise Exception("Auth error")

    def get_edit_token(self):
        token_resp = self.session.get(f"{self.url}/api.php", params={
            "action": "query", "meta": "tokens", "format": "json"
        }).json()
        self.edit_token = token_resp["query"]["tokens"]["csrftoken"]

    def get_page_content(self, title):
        response = self.session.get(f"{self.url}/api.php", params={
            "action": "query", "prop": "revisions", "rvprop": "content",
            "titles": title, "format": "json"
        }).json()
        pages = response["query"]["pages"]
        page_id = next(iter(pages))
        return pages[page_id]["revisions"][0]["*"] if page_id != "-1" else None

    def edit_page(self, title, new_content, summary):
        response = self.session.post(f"{self.url}/api.php", data={
            "action": "edit",
            "title": title,
            "text": new_content,
            "token": self.edit_token,
            "format": "json",
            "summary": summary
        }).json()
        return response.get("edit", {}).get("result") == "Success"
