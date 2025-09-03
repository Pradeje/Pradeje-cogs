from redbot.core import commands
import discord

class CommandsBrowser(commands.Cog):
    """Interactive command browser for your server."""

    def __init__(self, bot):
        self.bot = bot
        self.categories = {
            "🎮 Gameplay": [("!build", "Show your Smite 2 build"),
                            ("!checkin", "Log your daily streak"),
                            ("!stats", "Display rank and W/L")],
            "🛠 Moderation": [("!purge", "Clear a user’s messages"),
                              ("!ban", "Remove a disruptive user"),
                              ("!timeout", "Silence a user temporarily")],
            "🎵 Music & Media": [("!sr", "Request a song"),
                                 ("!yt", "Share latest YouTube video"),
                                 ("!playlist", "Show song queue")],
            "🎉 Fun & Engagement": [("!hello", "Greet the chat"),
                                    ("!random", "Generate a fun fact"),
                                    ("!shoutout", "Highlight streamer")],
            "📊 Stats & Info": [("!time", "Show stream time"),
                                ("!vanish", "Clear your messages stealthily"),
                                ("!checkins", "View the streak leaderboard")]
        }

    @commands.command(name="commandsmenu")
    async def commandsmenu(self, ctx):
        """Open the interactive commands menu."""
        options = [
            discord.SelectOption(label=cat, value=cat) for cat in self.categories
        ]

        select = discord.ui.Select(placeholder="Select a category…", options=options)

        async def callback(interaction: discord.Interaction):
            selected = interaction.data["values"][0]
            cmds = self.categories.get(selected, [])
            desc = "\n".join(f"**{c[0]}** — {c[1]}" for c in cmds)
            embed = discord.Embed(
                title=f"{selected} Commands",
                description=desc or "No commands in this category.",
                color=0x00D9FF
            )
            await interaction.response.edit_message(embed=embed, view=view)

        select.callback = callback

        view = discord.ui.View()
        view.add_item(select)

        embed = discord.Embed(
            title="⚡ Pradeje Gaming — Commands Menu",
            description="Choose a category below to view commands.",
            color=0xFF2EF7
        )
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(CommandsBrowser(bot))