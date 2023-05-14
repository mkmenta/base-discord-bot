# Base Bot for Discord
A base bot for Discord in *Python* that implements a few interactions.

## How to run it
First, I recommend you to read this README completely. It might help you understand better the following steps.
1. Create the Application and install install it in your Server by following 
[this](https://discord.com/developers/docs/getting-started#step-1-creating-an-app).
2. Create a `.env` file in the project root or add the following environment variables:
  - `DISCORD_BOT_TOKEN`: Check [this](https://discord.com/developers/docs/getting-started#step-1-creating-an-app)
  again to find how to get your bot token.
  - `DISCORD_GUILD_IDS`: a list of the guild ids separated by `,`. (Optional but VERY recommended while developing or 
  if you just want to run your bot in just a few servers. Continue reading this README to know why).
3. Install the requirements:
```bash
python3 -m pip install -r requirements.txt
```
4. Run the bot with:
```bash
python3 -m basebot
```

## Notes and explanations
Some explanations of things I learnt while developing this bot that could save you A LOT of time.
- **Guild**: A *guild* is a synonym for Discord *server*. 
- **Guild IDs**: (i.e. Server ID). If we implement a bot to handle a command like `/hello` (in this case), once the
  bot is started it tells all the Discord Servers/Guilds that it is handling that command, so that the users can see it when
  they first write `/`. This can take A LOT of time (in the docs it says up to an hour) unless we specify the list of 
  servers in which we want to register that command. If we specify that list, it will take <10 seconds to start. This
  is why setting the `DISCORD_GUILD_IDS` environment variable is very recommended.
  - *How to get your guild ID?*: (As of now) Open Discord, go to Settings > Advanced and enable developer mode.
  Then, right-click on the server title and select "Copy ID" to get the guild ID. (Source: *Wikipedia*)
- **Privileged Gateway Intents and Permissions**: the bot or application will have two types of permissions:
  - *Privileged Gateway Intents*: (as of now) they are just three (Presence Intent, Server Members intent and Message Content
  intent). These intents allow the bot to read that information, otherwise (I think) Discord won't even send that information 
  to your bot. *For example: if you want the bot to be able to answer to a message when it is mentioned, it will need to check 
  the content of all the messages sent to the server to see if it was mentioned in any of them. So it needs "Message Content
  intent"*
  - **Permissions**: these are the same permissions that can be given to any other *user* or *role* in your Discord server. You 
  can allow your bot to "Send messages", "Create public threads", "Attach files" or whatever.
    - The permissions of the bot are handled with the **bot role** (of the same name) that is created when you install the bot 
    in your server (and you can modify them at any time directly from the Discord App).
    - Be careful with the `@everyone` role! The permissions in Discord are summed (or accumulated) so even if you ONLY give your
    bot's role the permission of "Send Message" if the role `@everyone` in your Server allows it to do other stuff it will also 
    be able to do that other stuff (the same as *everyone* else in the server). (A way to handle this could be to reject all 
    permisions to the `@everyone` role and add a `@human` or `@user` role for human users).
    - To **reject** a permission to the bot, you can only do it in a specific channel. So you would need to go to that channel and
    specifically reject it in its settings.
- **The permissions in the bot installation URL Generator**: the OAuth2 URL Generator in the Discord Developer Application dashboard
lets you select all the permissions that the bot can have in a server when it is installed. THIS IS JUST A SHORTCUT. The permissions
you select when creating a URL are just the permissions that you give to the bot's role. So, it helps the user installing the bot 
to configure faster the bot's role. But the bot's role permissions can be modified at any time directly from the Discord App. 
  - So, basically you could install the bot without selecting any permission in the URL Generator and later add them to the bot's role
  in the Discord App if you want. 
  - This is not the same with the *Privileged Gateway Intents* which must be set directly in the [Discord Developer Application 
  dashboard](https://discord.com/developers/applications)

## References
- Getting started tutorial from Discord: https://discord.com/developers/docs/getting-started
- Python discord libraries: https://discord.com/developers/docs/topics/community-resources#libraries
  - I found the docs of the different python libraries a bit difficult to follow 
  (maybe because Discord allows so many possible actions for bots and I don't know all of them).
  I finally decided to use `py-cord` because it was similar to `discord.py` (the most starred library 
  right now) but with better docs.
- Pycord docs: https://docs.pycord.dev/en/stable/index.html
