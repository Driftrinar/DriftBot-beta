# DriftBot-beta
DriftBot is a light and open source Discord bot written in discord.py by Driftrinar. DriftBot has a lot of features like: Kick, Ban, Mute (in development), Message Logging (in development), Music (in development), reaction roles, terminal logger (optional), embeds and settings via commands.



Setup:
1. Download DriftBot by `git clone https://github.com/Driftrinar/DriftBot-beta/`
2. Install python3 by going to your terminal and installing python3 with your package manager, example: `sudo apt install python3`.
3. Run `cd DriftBot-beta/DriftBot` to enter the file.
4. Create a profile in https://discord.com/developers/applications/ for your bot and copy the token.
5. Open an editor and create a .env file for token, in the file type `TOKEN=` and put your token after that.
6. Install discord.py, youtube-dl and dotenv by running `python3 -m pip install discord.py youtube-dl dotenv` in your terminal.
7. Then launch the bot by running `python3 DriftBot.py`

The change-prefix command isn't functional yet, the current default prefix is "!", to change it edit the DriftBot.py file and change replace "!" in
`bot = commands.Bot(command_prefix="!")`.

Contact: Driftrinar.xyz

Bot is still in development.
