import discord
import praw

# Discord Bot Token
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Reddit API Credentials
REDDIT_CLIENT_ID = 'YOUR_REDDIT_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'YOUR_REDDIT_CLIENT_SECRET'
REDDIT_USER_AGENT = 'YOUR_REDDIT_USER_AGENT'

# Subreddits to Monitor (add more as needed)
SUBREDDITS = ['news', 'worldnews','UpliftingNews','technews','sports']

# Initialize Discord Intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize Discord Client and Reddit API
client = discord.Client(intents=intents)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!news'):
        for subreddit_name in SUBREDDITS:
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.new(limit=5):  # Fetch the latest 5 posts
                embed = discord.Embed(title=submission.title, url=submission.url)
                embed.set_author(name=submission.author.name)
                await message.channel.send(embed=embed)

client.run(DISCORD_TOKEN)
