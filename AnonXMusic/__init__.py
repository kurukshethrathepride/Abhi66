from aiohttp import web
import os
from AnonXMusic.core.bot import Anony
from AnonXMusic.core.dir import dirr
from AnonXMusic.core.git import git
from AnonXMusic.core.userbot import Userbot
from AnonXMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

async def health(request):
    return web.Response(text="AnonXMusic is running", status=200)


async def start_health_server():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(__import__("os").environ.get("PORT", 1000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    LOGGER("AnonXMusic").info(f"Health server running on port {port}")
    return runner


app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
