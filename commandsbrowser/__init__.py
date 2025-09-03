from .commandsbrowser import CommandsBrowser

async def setup(bot):
    await bot.add_cog(CommandsBrowser(bot))