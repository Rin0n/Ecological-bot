import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def theme(ctx, num: int = None):
    # If no theme is provided, prompt the user to choose
    if num is None:
        await ctx.send('Выберите одну из двух тем: 1, 2, 3')
        return

    if num == 1:
        await water_pollution(ctx)
    elif num == 2:
        await deforestation(ctx)
    elif num == 3:
        await air_pollution(ctx)
    else:
        await ctx.send('Неверная тема. Выберите из: 1, 2, 3')


async def water_pollution(ctx):
    await ctx.send('Загрязнение вод: корпорации выбрасывают химикаты и нефть в водоёмы, вместо того что бы оккуратно утилизировать отходы и следить за оборудыванием')
    img_name = random.choice(os.listdir('water'))
    with open(f'water/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: корпорации не хотят терять свои доходы, но государтсво может на них надавить.')

async def deforestation(ctx):
    await ctx.send('Вырубка лесов пагубно сказывается на нас, по скольку мы дышим кислородом, которые вырабатывают деревья')
    img_name = random.choice(os.listdir('les'))
    with open(f'les/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: использовать менее органическое топливо')

async def air_pollution(ctx):
    await ctx.send('Заводы, фабрики и многое другое сильно загрязняет нашу атмосферу и вызывает болезни')
    img_name = random.choice(os.listdir('air'))
    with open(f'air/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Решение: использовать более экологически чистые продукты, и построить меньше заводов (оптимизировать процесс)')

bot.run("token")
