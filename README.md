# Reddit-News-Discord-Bot

The Reddit News Discord Bot is a Python-based bot that fetches and shares the latest posts from specified subreddits to a Discord server. The bot uses the `discord.py` library for Discord integration and the `praw` library to interact with the Reddit API.

## Features

- Fetches the latest posts from specified subreddits (e.g., r/news, r/worldnews).
- Posts are displayed as embedded messages in Discord, including the post title, author, and URL.
- Customizable command trigger to fetch news posts.
- Supports multiple subreddits to monitor.

## Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/reddit-news-discord-bot.git
   ```

2. Install the required Python libraries using pip:

   ```
   pip install discord.py praw
   ```

3. Create a Reddit API application and obtain the required credentials (client ID, client secret, user agent). Follow the instructions in the "Set Up a Reddit API Application" section of the script.

4. Open the `reddit_news_bot.py` file and replace the following placeholders:

   - `YOUR_DISCORD_BOT_TOKEN`: Replace this with your Discord bot token. You can create a bot on the Discord Developer Portal (https://discord.com/developers/applications).
   - `YOUR_REDDIT_CLIENT_ID`: Replace this with your Reddit API client ID.
   - `YOUR_REDDIT_CLIENT_SECRET`: Replace this with your Reddit API client secret.
   - `YOUR_REDDIT_USER_AGENT`: Replace this with your Reddit API user agent.

## Usage

1. Invite your bot to your Discord server by using the following URL:

   ```
   https://discord.com/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&scope=bot
   ```

   Replace `YOUR_BOT_CLIENT_ID` with your actual bot's client ID. You can find the client ID in the Discord Developer Portal.

2. Run the bot using the following command:

   ```
   python reddit_news_bot.py
   ```

3. In your Discord server, use the specified command trigger (default: `!news`) to request news posts. The bot will fetch the latest posts from the specified subreddits and display them as embedded messages.

## Customization

- You can modify the list of subreddits to monitor by adding or removing entries from the `SUBREDDITS` list in the script.
- To change the command trigger, update the value in the `on_message` event function (default: `!news`).

## Contributing

If you find any issues or want to suggest improvements, feel free to create a pull request or open an issue on this repository. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

---

Enjoy using the Reddit News Discord Bot to keep your server updated with the latest news from Reddit!
