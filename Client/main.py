import disnake
from disnake.ext import commands
import cfg

bot = commands.InteractionBot()


class RatBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def playsound(self, inter: disnake.ApplicationCommandInteraction, soundfile=disnake.File):
        print(soundfile)
        await inter.response.send_message("Роль выдана", ephemeral=True)


@bot.event
async def on_ready():
    print("Бот готов!")


def setup(bot: commands.InteractionBot):
    bot.add_cog(RatBot(bot))


setup(bot)
bot.run(cfg.TOKEN)
