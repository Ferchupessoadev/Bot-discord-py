# Discord´s bot

## Development setup

First, clone the repo and cd into the project

```bash
git clone https://github.com/Ferchupessoadev/Bot-discord-py
cd Bot-discord-py
```

Second, Create a virtual environments with venv and activate the environment

- Create environment

```bash
python3 -m venv .venv
```

- Activate environment

```bash
source .venv/bin/activate

```

Install dependencies.

```bash
pip install -r requirements.txt
```

Change the os.environ.get for your bot's token or create a global variable with the name TOKEN_DISCORD

```python
# Reemplaza 'TU_TOKEN_DEL_BOT' con tu token de bot
TOKEN = os.environ.get("TOKEN_DISCORD", default="TU_TOKEN_DEL_BOT")
```

Finally, run the script

```bash
python3 bot.py
```
