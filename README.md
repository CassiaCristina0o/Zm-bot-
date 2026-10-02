# Zm-bot

Discord bot that replies to good morning and good night messages on the Zcash Brasil community server.

## What it does

- Replies to "good morning" and "good night" in several languages (Portuguese, English, Spanish, Italian and Korean), for example `gm`, `zm`, `bom dia`, `gn`, `zn`, `boa noite`.
- Replies with a message, a random server sticker and a reaction (sun in the morning, moon at night).
- Every 15 to 20 days, whoever says good morning or good night wins a prize: the Golden Ticket. Only members with the Portuguese role who are not on the Zcash team can win.
- Stores the winners in a SQLite database, so the same person can't win twice in a row.
- With the word `tabela`, sends a file with the list of winners.

The channel, role and sticker IDs are hardcoded, so the bot only works on the server it was built for.

## How to run

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with the bot token:

   ```
   DISCORD_TOKEN=your-token-here
   ```

3. Run the bot:

   ```bash
   python my_bot_gm.py
   ```

## Built with

- [discord.py](https://discordpy.readthedocs.io/)
- [peewee](https://docs.peewee-orm.com/) with SQLite
- python-dotenv, tabulate and Unidecode
