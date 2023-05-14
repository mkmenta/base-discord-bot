"""Discord Bot's main file."""
import logging
import os
import discord
import coloredlogs
from dotenv import load_dotenv

# Initialize the logger
coloredlogs.install(level='INFO')
logger = logging.getLogger("basebot")

# Load the environment variables from the .env file (if it exists)
load_dotenv(dotenv_path=os.path.join(os.path.split(__file__)[0],
                                     '..',
                                     '.env'))
# Get the guild IDs (check the README for more information)
guild_ids = os.getenv('DISCORD_GUILD_IDS', None)
if guild_ids:
    guild_ids = guild_ids.split(',')


# Create the bot
bot = discord.Bot()


@bot.event
async def on_ready():
    """Handle the bot being ready."""
    logger.info(f'Logged in in as {bot.user}')


@bot.listen()
async def on_message(message: discord.Message):
    """Add a handler for the on_message event.

    The bot will create a thread if it is mentioned.

    Args:
        message (discord.Message): The message that was sent.
    """
    if bot.user in message.mentions:
        x = await message.create_thread(name="Unicorns and aliens")
        await x.send("Let's talk about it!")


@bot.slash_command(description="Greets someone", guild_ids=guild_ids)
async def hello(ctx: discord.ApplicationContext, name: str):
    """Greets someone.

    Args:
        ctx (discord.ApplicationContext): The context of the command.
        name (str): The name of the person to greet.
    """
    await ctx.respond(f"Hello {name}!")


@bot.listen()
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    """Add a handler for the on_raw_reaction_add event.

    The bot will send a message to the user that reacted with the heavy metal emoji.

    Args:
        payload (discord.RawReactionActionEvent): The payload of the event.
    """
    # Check if the reaction emoji is the heavy metal emoji and the
    # user that performed the reaction is not a bot
    if payload.emoji.name == "🤟" and not payload.member.bot:
        guild = bot.get_guild(payload.guild_id)
        user = guild.get_member(payload.user_id)

        # Send a message to the user
        await user.send("Rock'n'roll!")

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
