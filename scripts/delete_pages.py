import json
from utils.wiki_client import WikiClient
from utils.logger import logger

with open("script.json", "r", encoding="utf-8") as f:
    SCRIPT_CONFIG = json.load(f)

def delete_pages(pages, reason="Mass delete"):
    if pages is None:
        pages = SCRIPT_CONFIG["pages"]

    wiki = WikiClient()
    wiki.login()
    wiki.get_edit_token()

    for page in pages:
        logger.info(f"Deleting page '{page}'...")

        response = wiki.session.post(f"{wiki.url}/api.php", data={
            "action": "delete",
            "title": page,
            "token": wiki.edit_token,
            "format": "json",
            "reason": reason
        }).json()

        if "delete" in response:
            logger.info(f"Page '{page}' was deleted")
        else:
            logger.error(f"Error while deleting '{page}': {response}")