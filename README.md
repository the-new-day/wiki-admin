# Wiki Admin  

A set of Python scripts for automating administrative tasks on a MediaWiki-based wiki.

## Features
**Batch text replacement** – Replace text across multiple pages in one command.  
**Bulk page deletion** – Remove multiple pages at once.  

**🚧 Coming soon:** \
**Mass file upload** – Upload multiple files to the wiki.  
**Mass file deletion** – Delete multiple files from the wiki in a single command.  
**Logging system** – Supports `--verbose` mode for console output and `--no-log` to disable logging.  
**Flexible CLI** – Run commands like `python wiki-admin.py replace --old "foo" --new "bar"`

---

## Installation
1. **Clone the repository**  
```bash
git clone https://github.com/the-new-day/wiki-admin.git
cd wiki-admin
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Setup your configuration**

To use scripts, you have to [create a bot](https://www.mediawiki.org/wiki/Manual:Bots) on your wiki.
Fill `config.json` with your credentials:
```json
{
    "wiki_url": "your_wiki_url.com",
    "username": "bot_username",
    "password": "bot_password"
}
```

## Usage
### Script configuration
You can specify parameters for all scripts in the `script.json` file. At the moment the only parameter: `pages` - list of pages to perform the action.

### 📝 Replace text
```bash
python wiki-admin.py replace --old "foo" --new "bar" --pages "Page1" "Page2"
```
```bash
python wiki-admin.py replace --old "foo" --new "bar"
```

### 🗑 Delete Pages
```bash
python wiki-admin.py delete --pages "Page1" "Page2"
```
```bash
python wiki-admin.py delete
```

As you can see, you can also specify a list of pages in the argument list. If it is not in the argument list, it will be taken from `script.json`.

### ⚙ Additional Options
* `--verbose` – Enable detailed logging
* `--no-log` – Disable logging
