# https://youtu.be/IaTfJ4vqHhc
# https://youtu.be/xsA5QAkr-04
# from discord.ext import commands
# from discord import Embed
# from typing import Optional

# class MyHelpCommand(commands.MinimalHelpCommand):
#   def get_command_signature(self, command):
#     return '{0.clean_prefix}{1.qualified_name} {1.signatire}' .format(self, command)

#   async def help_embed(self, title: str, description: Optional[str] = None, mapping: Optional[dict] = None):
#     embed = Embed(title=title)
#     if description:
#       embed.description = description
#     if mapping:
#       for cog, command_set in mapping.items():
#         filtered = await self.filter_commands(command_set, sort = True)
#         if not filtered:
#           continue
#         name = cog.qualified_name if cog else "No Category"
#         # \u2002 is an en-space
#         cmd_list = "\u2002".join(f"`{self.context.clean_prefix}{cmd.name}`" for cmd in filtered)
#         value = (f"{cog.description}\n{cmd_list}"
#           if cog and cog.description
#           else cmd_list)
#         embed.add_field(name = name, value = value)
#     return embed
  
#   async def send_bot_help(self, mapping: dict):
#     send await self.help_embed(title:"Bot Commands", description:self.context.bot.description, mapping=mapping)

#   async def send_command_help(self, command: commands.Command):
#     pass

#   async def send_cog_help(self, cog: commands.Cog):
#     pass

#   send_group_help = send_command_help

# class HelpCog(commands.Cog, name="Help"):
#   """Shows help info about commands"""

#   def __init__(self, bot):
#     self._original_help_command = bot.help_command
#     bot.help_command = MyHelpCommand()
#     bot.help_command.cog = self

#   def cog_unload(self):
#     self.bot.help_command = self._original_help_command

# def setup(bot: commands.Bot):
#   bot.add_cog(HelpCog(bot))
