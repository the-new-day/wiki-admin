import json
from utils.wiki_client import WikiClient
from utils.logger import logger

with open("script.json", "r", encoding="utf-8") as f:
    SCRIPT_CONFIG = json.load(f)

def replace_text(old_text, new_text, pages=None):
    """Replaces text on given pages"""
    if pages is None:
        pages = SCRIPT_CONFIG["pages"]

    logger.info("Start replacing text")
    logger.info(f"Replace '{old_text}' with '{new_text}' on pages: {pages}")

    wiki = WikiClient()
    wiki.login()
    wiki.get_edit_token()

    for page in pages:
        logger.info(f"Processing {page}...")

        content = wiki.get_page_content(page)
        if content is None:
            logger.warning(f"Page '{page}' not found")
            continue

        new_content = content.replace(old_text, new_text)

        if new_content == content:
            logger.info(f"On '{page}' nothing has changed")
        else:
            success = wiki.edit_page(page, new_content, f"Autoreplace: '{old_text}' → '{new_text}'")
            if success:
                logger.info(f"'{page}' is updated")
            else:
                logger.error(f"An error occured while updating '{page}'")
