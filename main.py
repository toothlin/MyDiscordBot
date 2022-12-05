import os
from discord.ui import Button, View
import random
import requests
import asyncio
import json

player = 1
caty = 0
#L1=["x","xx"]
#L2=[0,0]
#L3=[0,0]
win = 0
botlist = []
aa = 0
ab = 0
ac = 0
ba = 0
bb = 0
bc = 0
ca = 0
cb = 0
cc = 0
r1 = [aa, ab, ac]
r2 = [ba, bb, bc]
r3 = [ca, cb, cc]
c1 = [aa, ba, ca]
c2 = [ab, bb, cb]
c3 = [ac, bc, cc]
d1 = [aa, bb, cc]
d2 = [ac, bb, ca]
rows = [r1, r2, r3]
columns = [c1, c2, c3]
diagonals = [d1, d2]
alls = [rows, columns, diagonals]
botlist = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]

def sets():
  global numb
  f = open("tower.txt", "w")
  f.close()
  global L1
  global L2
  global L3
  ph = ""
  L1 = []
  L2 = []
  L3 = []
  for i in range(numb):
    ph = ""
    for l in range(i + 1):
      ph += "x"
    L1.append(ph)
  for i in range(numb):
    L2.append("0")
    L3.append("0")
  reply = ""
  reply = display(numb, reply)
  return(reply)
  write()
  
def setit():
  global alls
  global botlist
  aa = 0
  ab = 0
  ac = 0
  ba = 0
  bb = 0
  bc = 0
  ca = 0
  cb = 0
  cc = 0
  r1 = [aa, ab, ac]
  r2 = [ba, bb, bc]
  r3 = [ca, cb, cc]
  c1 = [aa, ba, ca]
  c2 = [ab, bb, cb]
  c3 = [ac, bc, cc]
  d1 = [aa, bb, cc]
  d2 = [ac, bb, ca]
  rows = [r1, r2, r3]
  columns = [c1, c2, c3]
  diagonals = [d1, d2]
  alls = [rows, columns, diagonals]
  botlist = ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]
  reply = displayit()
  return (reply)


def displayit():
  global alls
  global botlist
  reply = ""
  for i in range(3):
    for h in range(3):
      ph = alls[0][i][h]
      if ph == 0:
        reply += "-"
      elif ph == 1:
        reply += "x"
      else:
        reply += "o"
    reply += "\n"
  return (reply)


def check():
  global alls
  global botlist
  global win
  win = 0
  pk = 0
  for i in range(3):
    if win == 0:
      pg = 0
      pj = 0
      for h in range(3):
        ph = alls[0][i][h]
        if ph == 0:
          pg = 1
          pk = 1
        pj = pj + ph
      if pg == 0:
        if pj == 3:
          win = 1
        elif pj == 6:
          win = 2
  for i in range(3):
    if win == 0:
      pg = 0
      pj = 0
      for h in range(3):
        ph = alls[1][i][h]
        if ph == 0:
          pg = 1
          pk = 1
        pj = pj + ph
      if pg == 0:
        if pj == 3:
          win = 1
        elif pj == 6:
          win = 2
  for i in range(2):
    if win == 0:
      pg = 0
      pj = 0
      for h in range(3):
        ph = alls[2][i][h]
        if ph == 0:
          pg = 1
          pk = 1
        pj = pj + ph
      if pg == 0:
        if pj == 3:
          win = 1
        elif pj == 6:
          win = 2
  if pk == 0 and win == 0:
    win = 3


def botmove(pnum):
  global alls
  d = 0
  e = 0
  global botlist
  if pnum != 0:
    if len(botlist) >= 1:
      a = random.choice(botlist)
      botlist.remove(a)
      x = 0
      for letter in a:
        if x == 0:
          if letter == "a":
            d = 0
          elif letter == "b":
            d = 1
          else:
            d = 2
          x = 1
        else:
          if letter == "a":
            e = 0
          elif letter == "b":
            e = 1
          else:
            e = 2
      alls[0][d][e] = pnum
      alls[1][e][d] = pnum
      if d == e:
        alls[2][0][e] = pnum
        if d == 1:
          alls[2][1][1] = pnum
      elif e == 2 and d == 0:
        alls[2][1][e] = pnum
      elif e == 0 and d == 2:
        alls[2][1][e] = pnum
    win = 4


def rg():
  global alls
  global botlist
  while win == 0:
    asyncio.sleep(1)
    botmove(1)
    displayit()
    check()
    if win == 0:
      asyncio.sleep(1)
      botmove(2)
      displayit()
      check()


def pm(pnum, location):
  global player
  global alls
  d = 0
  e = 0
  global botlist
  if pnum != 0:
    if len(botlist) >= 1:
      a = location
      if a in botlist:
        botlist.remove(a)
        x = 0
        for letter in a:
          if x == 0:
            if letter == "a":
              d = 0
            elif letter == "b":
              d = 1
            else:
              d = 2
            x = 1
          else:
            if letter == "a":
              e = 0
            elif letter == "b":
              e = 1
            else:
              e = 2
        alls[0][d][e] = pnum
        alls[1][e][d] = pnum
        if d == e:
          alls[2][0][e] = pnum
          if d == 1:
            alls[2][1][1] = pnum
        elif e == 2 and d == 0:
          alls[2][1][e] = pnum
        elif e == 0 and d == 2:
          alls[2][1][e] = pnum
      else:
        if player == 2:
          player = 1
        else:
          player = 2
    win = 4
    response = displayit()
    check()
    return (response)


def test(order, player):
  global alls
  for i in range(len(order)):
    pm(player[i], order[i])
    displayit()
    check()
    print(alls)
    asyncio.sleep(1)


def write():
  f = open("list.txt", "w")
  s1 = [json.dumps(L1), json.dumps(L2), json.dumps(L3)]
  s2 = json.dumps(s1)
  f.write(s2)
  f.close()


with open('list.txt') as f:
  lines = f.readlines()
lines0 = lines[0]
s3 = json.loads(lines0)
l1 = s3[0]
l2 = s3[1]
l3 = s3[2]
L1 = json.loads(l1)
L2 = json.loads(l2)
L3 = json.loads(l3)

#write()
numb = len(L1)


def move(ctx, start, end, num):
  global caty
  hold = "a"
  temp = 0
  switch = 0
  counter = ""
  for i in range(num):
    temp = start[i]
    temp = str(temp)
    if temp != "0" and switch == 0:
      hold = temp
      switch = 1
      place = i
    counter = i
  if hold == "a":
    hold = ""
    place = counter
  switch = 0
  hold2 = "a"
  for i in range(num):
    temp = end[i]
    temp = str(temp)
    #print("temp="+str(temp))
    #print("switch="+str(switch))
    if temp != "0" and switch == 0:
      hold2 = temp
      switch = 1
      place2 = i
    counter = i
    #print("impossible")
  if hold2 == "a":
    hold2 = ""
    place2 = counter
  else:
    place2 = place2 - 1
  #print(hold)
  #print(hold2)
  if len(hold) < len(hold2) or len(hold2) == 0:
    start[place] = 0
    end[place2] = hold
    #print("yes")
  elif len(hold) > len(hold2):
    caty = 1


def display(num, reply):
  f = open("tower.txt", "w")
  f.close()
  f = open("tower.txt", "w")
  f.write("-----------1-----------\n")
  for i in range(num):
    f.write(str(L1[i]) + "\n")
  f.write("-----------2-----------\n")
  for i in range(num):
    f.write(str(L2[i]) + "\n")
  f.write("-----------3-----------\n")
  for i in range(num):
    f.write(str(L3[i]) + "\n")
  f.close()
  with open('tower.txt') as f:
    for line in f:
      reply += line
  return (reply)


API = os.environ['APIkey']
my_secret = os.environ['MyToken']
extram = os.environ['extram']
import discord
from discord.ext import commands

intents = discord.Intents.all()
helpCommand = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix='A!',
                   intents=intents,
                   helpCommand=helpCommand)


@bot.event
async def on_connect():
  print("Your bot is active")


@bot.command(brief="Bot says hi")
async def message(ctx):
  button1 = Button(label="Click Me!", style=discord.ButtonStyle.green)
  async def button1Clicked(interaction):
    await interaction.response.send_message("Welcome to Allison Bot!")
  button1.callback = button1Clicked
  view = View()
  view.add_item(button1)
  await ctx.reply("Guess what?", view=view)

@bot.command(brief="button tic tac toe")
async def bttt(ctx):
  global p
  global win
  p=1
  setit()
  global alls
  global win
  buttonaa = Button(label=" ", style=discord.ButtonStyle.green, row=0)
  buttonab = Button(label=" ", style=discord.ButtonStyle.green, row=0)
  buttonac = Button(label=" ", style=discord.ButtonStyle.green, row=0)
  buttonba = Button(label=" ", style=discord.ButtonStyle.green, row=1)
  buttonbb = Button(label=" ", style=discord.ButtonStyle.green, row=1)
  buttonbc = Button(label=" ", style=discord.ButtonStyle.green, row=1)
  buttonca = Button(label=" ", style=discord.ButtonStyle.green, row=2)
  buttoncb = Button(label=" ", style=discord.ButtonStyle.green, row=2)
  buttoncc = Button(label=" ", style=discord.ButtonStyle.green, row=2)
  #buttonaa.disabled=False
  #buttonab.disabled=False
  #buttonac.disabled=False
  #buttonba.disabled=False
  #buttonbb.disabled=False
  #buttonbc.disabled=False
  #buttonca.disabled=False
  #buttoncb.disabled=False
  #buttoncc.disabled=False
  async def buttonaaClicked(interaction):
    nonlocal buttonaa
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonaa = Button(label=a, style=discord.ButtonStyle.green, row=0)
    buttonaa.disabled=True
    alls[0][0][0] = p
    alls[1][0][0] = p
    alls[2][0][0] = p
    print(alls)
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonaa.callback = buttonaaClicked
  async def buttonabClicked(interaction):
    nonlocal buttonab
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonab = Button(label=a, style=discord.ButtonStyle.green, row=0)
    buttonab.disabled=True
    alls[0][0][1] = p
    alls[1][1][0] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonab.callback = buttonabClicked
  async def buttonacClicked(interaction):
    nonlocal buttonac
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonac = Button(label=a, style=discord.ButtonStyle.green, row=0)
    buttonac.disabled=True
    alls[0][0][2] = p
    alls[1][2][0] = p
    alls[2][1][0] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonac.callback = buttonacClicked
  async def buttonbaClicked(interaction):
    nonlocal buttonba
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonba = Button(label=a, style=discord.ButtonStyle.green, row=1)
    buttonba.disabled=True
    alls[0][1][0] = p
    alls[1][0][1] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonba.callback = buttonbaClicked
  async def buttonbbClicked(interaction):
    nonlocal buttonbb
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonbb = Button(label=a, style=discord.ButtonStyle.green, row=1)
    buttonbb.disabled=True
    alls[0][1][1] = p
    alls[1][1][1] = p
    alls[2][0][1] = p
    alls[2][1][1] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonbb.callback = buttonbbClicked
  async def buttonbcClicked(interaction):
    nonlocal buttonbc
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonbc = Button(label=a, style=discord.ButtonStyle.green, row=1)
    buttonbc.disabled=True
    alls[0][1][2] = p
    alls[1][2][1] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonbc.callback = buttonbcClicked
  async def buttoncaClicked(interaction):
    nonlocal buttonca
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttonca = Button(label=a, style=discord.ButtonStyle.green, row=2)
    buttonca.disabled=True
    alls[0][2][0] = p
    alls[1][0][2] = p
    alls[2][1][2] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttonca.callback = buttoncaClicked
  async def buttoncbClicked(interaction):
    nonlocal buttoncb
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttoncb = Button(label=a, style=discord.ButtonStyle.green, row=2)
    buttoncb.disabled=True
    alls[0][2][1] = p
    alls[1][1][2] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttoncb.callback = buttoncbClicked
  async def buttonccClicked(interaction):
    nonlocal buttoncc
    global p
    global win
    global alls
    if p == 1:
      p = 2
      a = "o"
    elif p == 2:
      p = 1
      a = "x"
    buttoncc = Button(label=a, style=discord.ButtonStyle.green, row=2)
    buttoncc.disabled=True
    alls[0][2][2] = p
    alls[1][2][2] = p
    alls[2][0][2] = p
    check()
    if win == 3:
      await ctx.reply("its a tie!")
    elif win == 1:
      await ctx.reply("x wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    elif win == 2:
      await ctx.reply("o wins!")
      buttonaa.disabled=True
      buttonab.disabled=True
      buttonac.disabled=True
      buttonba.disabled=True
      buttonbb.disabled=True
      buttonbc.disabled=True
      buttonca.disabled=True
      buttoncb.disabled=True
      buttoncc.disabled=True
    view = View()
    view.add_item(buttonaa)
    view.add_item(buttonab)
    view.add_item(buttonac)
    view.add_item(buttonba)
    view.add_item(buttonbb)
    view.add_item(buttonbc)
    view.add_item(buttonca)
    view.add_item(buttoncb)
    view.add_item(buttoncc)
    await interaction.response.edit_message(view=view)
  buttoncc.callback = buttonccClicked
  view = View()
  view.add_item(buttonaa)
  view.add_item(buttonab)
  view.add_item(buttonac)
  view.add_item(buttonba)
  view.add_item(buttonbb)
  view.add_item(buttonbc)
  view.add_item(buttonca)
  view.add_item(buttoncb)
  view.add_item(buttoncc)
  await ctx.reply("tic tac toe", view=view)

#"Enter a name following command.\n Example: A!name May"
@bot.command(brief="say hi!")
async def name(ctx, name):
  await ctx.reply("Hello " + name + " from AllisonBot")


#"Enter two numbers with a space inbetween that you want to add after command name.\n Example: A!add 5 9"
@bot.command(brief="add numbers")
async def add(ctx, num1, num2):
  num3 = int(num1) + int(num2)
  await ctx.reply(num3)


#"Enter time after command name.\n Example: A!time 9:59 pm or A!time 8"
@bot.command(brief="response based on time given")
async def time(ctx, *, time: str):
  time2 = ""
  count = 0
  hold = ""
  for letter in str(time):
    if letter.isalpha():
      if letter == "p" and hold == "":
        hold = "p"
      if letter == "a" and hold == "":
        hold = "a"
    if ord(letter) >= 48 and ord(letter) <= 57 and count != 2:
      time2 += letter
      count = count + 1
    if ord(letter) == 58:
      count = 2
  if hold == "a" and time2 == "12":
    time2 = 0
  if hold == "p":
    time2 = int(time2) + 12
  if int(time2) < 5:
    await ctx.reply("Why are you awake? Go to sleep!")
  elif int(time2) < 12:
    await ctx.reply("Good morning!")
  elif int(time2) < 17:
    await ctx.reply("Good afternoon!")
  elif int(time2) < 22:
    await ctx.reply("Good evening!")
  elif int(time2) <= 24:
    await ctx.reply("Good night!")
  else:
    await ctx.reply(
      "Invalid format. Please use format like allisontime + ( xx pm/ xxam/ xx:xx(24 hour clock)/ xx(24 hour clock))"
    )


#"Enter command for cat photo.\n Example: A!cat"
@bot.command(brief="Cat photo")
async def cat(ctx):
  piclist = [
    "https://imgur.com/AD3MbBi", "https://i.imgur.com/k70MuHR.jpeg",
    "https://imgur.com/VVCngBC"
  ]
  await ctx.reply(random.choice(piclist))


"Enter phrase after command.\n Example: A!_8b will I pass my test"


@bot.command(brief="How likely is something to occur?")
async def _8b(ctx, *, phrase: str):
  list = [
    " Is highly likely", " Is highly ulikely", " Is never going to occur",
    " Will definetly occur", " Maybe"
  ]
  await ctx.reply(random.choice(list))


#"Enter 'rock' 'paper' or 'scissors' after command (you can also just use 'r' 'p' and 's'\n Example: A!rps rock"
@bot.command(brief="Rock, Paper, Scissors!")
async def rps(ctx, play):
  p1 = ""
  p2 = ""
  rr = ["rock", "paper", "scissors"]
  play2 = random.choice(rr)
  await ctx.reply(play2)
  count = 1
  for letter in play:
    if count == 1:
      if letter == "r" or letter == "p" or letter == "s":
        p1 += letter
        count = 0
  count = 1
  for letter in play2:
    if count == 1:
      if letter == "r" or letter == "p" or letter == "s":
        p2 += letter
        count = 0
  #await ctx.reply(p1+p2)
  if p1 == p2:
    await ctx.reply("It is a tie!")
  elif p1 == "r":
    if p2 == "p":
      await ctx.reply("You lose!")
      with open('losecount.txt', 'a') as f:
        f.write('x')
    else:
      await ctx.reply("You win!")
      with open('wincount.txt', 'a') as f:
        f.write('x')
  elif p1 == "p":
    if p2 == "s":
      await ctx.reply("You lose!")
      with open('losecount.txt', 'a') as f:
        f.write('x')
    else:
      await ctx.reply("You win!")
      with open('wincount.txt', 'a') as f:
        f.write('x')
  elif p1 == "s":
    if p2 == "r":
      await ctx.reply("You lose!")
      with open('losecount.txt', 'a') as f:
        f.write('x')
    else:
      await ctx.reply("You win!")
      with open('wincount.txt', 'a') as f:
        f.write('x')
  else:
    await ctx.reply("error")
  win = "error"
  lose = "error"
  with open('wincount.txt') as f:
    win = f.readlines()
    for letter in win:
      win = str(len(letter))
  with open('losecount.txt') as f:
    lose = f.readlines()
    for letter in lose:
      lose = str(len(letter))
  await ctx.reply("You have won " + win + " matches and you have lost " +
                  lose + " matches.")


#"Enter name after command.\n Example: A!nation jack"
@bot.command(brief="Find where a name is from")
async def nation(ctx, name):
  url = "https://api.nationalize.io/?name=" + name
  req = requests.get(url)
  data = req.json()
  id = data["country"][0]["country_id"]
  #await ctx.reply(id)
  url = "https://gist.githubusercontent.com/ssskip/5a94bfcd2835bf1dea52/raw/3b2e5355eb49336f0c6bc0060c05d927c2d1e004/ISO3166-1.alpha2.json"
  req = requests.get(url)
  data = req.json()
  nation = data[id]
  await ctx.reply("The most likely nation of origin for " + name + " is " +
                  nation)


#"Enter command for a joke.\n Example: A!joke"
@bot.command(brief="Get a joke")
async def joke(ctx):
  url = "https://official-joke-api.appspot.com/random_joke"
  req = requests.get(url)
  data = req.json()
  setup = data["setup"]
  punchline = data["punchline"]
  await ctx.reply(setup)
  await asyncio.sleep(2)
  await ctx.reply(punchline)


#"Enter command for current price of gold.\n Example: A!gold"
@bot.command(brief="Current price of gold")
async def gold(ctx):
  url = "https://gold-price-live.p.rapidapi.com/get_metal_prices"
  headers = {
    "X-RapidAPI-Key": "b7d06c2b80mshfa4facf2eeb497dp17e3f3jsnf4539b7f4961",
    "X-RapidAPI-Host": "gold-price-live.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers)
  data = response.json()
  gold = data["gold"]
  gold = str(gold)
  await ctx.reply("The current price of gold is $" + gold + " per ounce.")


#"Enter zip after command.\n Example: A!weather"
@bot.command(brief="Find the weather")
async def weather(ctx, zip):
  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&appid=" + API
  req = requests.get(url)
  data = req.json()
  name = data["name"]
  temp = data["main"]["temp"]
  temp = temp - 273
  temp = temp * 9
  temp = temp / 5
  temp = temp + 32
  temp = str(temp)
  desc = data["weather"][0]["description"]
  await ctx.reply("The weather in " + name + " is " + desc + " and " + temp +
                  " degrees fahrenheit")


#"Sets the height of tower, ex 3 = 3 high, enter number after command.\n Example: A!tset 4"
@bot.command(brief="Set up a tower")
async def tset(ctx, num):
  global numb
  numb = int(num)
  f = open("tower.txt", "w")
  f.close()
  global L1
  global L2
  global L3
  ph = ""
  L1 = []
  L2 = []
  L3 = []
  for i in range(numb):
    ph = ""
    for l in range(i + 1):
      ph += "x"
    L1.append(ph)
  for i in range(numb):
    L2.append("0")
    L3.append("0")
  reply = ""
  reply = display(numb, reply)
  await ctx.reply(reply)
  write()


#"Moves a piece from tower to tower. The start point comes first and end point second. Each tower has its own name (L1,L2,L3), enter two after command.\n Example: A!tmove L1 L2"
@bot.command(brief="Moves a piece from tower to tower.")
async def tmove(ctx, start, end):
  button1 = Button(label="Reset", style=discord.ButtonStyle.green)
  async def button1Clicked(interaction):
    reply=sets()
    await ctx.reply(reply)
    write()
  button1.callback = button1Clicked
  view = View()
  view.add_item(button1)
  global caty
  global numb
  test = globals()[start]
  for i in test:
    if str(i).isalpha():
      caty = caty + 1
  if int(caty) == 0:
    caty = 0
    await ctx.reply("Invalid move!")
  elif start != end:
    move(ctx, globals()[start], globals()[end], numb)
    if caty == 1:
      await ctx.reply("Invalid move!")
      caty = 0
    else:
      reply = ""
      reply = display(numb, reply)
      await ctx.reply(reply, view=view)
      write()
      x = 0
      for i in L1:
        if str(i).isalpha():
          x = 1
      y = 0
      for i in L2:
        if str(i).isalpha():
          y = 1
      z = 0
      for i in L3:
        if str(i).isalpha():
          z = 1
      if x == 0:
        if z == 0:
          await ctx.reply("You win!")
        elif y == 0:
          await ctx.reply("You win!")
  else:
    await ctx.reply("Invalid move!")
  

@bot.command(brief="sets up new tic tac toe game")
async def reset(ctx):
  reply = setit()
  await ctx.reply(reply)


@bot.command(brief="play a move")
async def pmove(ctx, location):
  global player
  pnum = player
  if player == 1:
    player = player + 1
  else:
    player = player - 1
  reply = pm(pnum, location)
  await ctx.reply(reply)
  if win == 3:
    await ctx.reply("its a tie!")
  elif win == 1:
    await ctx.reply("x wins!")
  elif win == 2:
    await ctx.reply("o wins!")


bot.run(my_secret)
#my_secret
