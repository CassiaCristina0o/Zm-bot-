import discord
import os
import random
from dotenv import load_dotenv
from unidecode import unidecode

load_dotenv()
my_token = os.getenv("DISCORD_TOKEN")

lista_comandos = ["zm","gm","Good morning","Morning","Gmorning","bom dia ", "dia bom","dia","Buenos días","Feliz día","Buen día","Annyeonghaseyo","안녕하세요","Joh eun achim","좋은 아침","Annyeong hasimnikka","안녕하십니까","Buongiorno","Buon mattino","Buona giornata"]

lista_comandos_n = ["zn","gn","Good night","Nighty night","Boa noite","Boa noitinha","noite","Buenas noches","annyeonghi jumuseyo","안녕히 주무세요","gutbam","굿밤","Buona notte"]

lista_respostas = ["Zm Zcasher","Zm zfriend","gm Zfriend", "gm Zcasher"]

lista_respostas_n = ["Zn Zcasher","Zn zfriend","gn Zfriend", "gn Zcasher"]

contador = 0

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event 
async def on_ready():
    print (f'estou pronto!zm meu ID é {client.user.id}')
    
@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot or message.channel.id !=  1080161118384820358:
        return 
    
    replied = False 
    awarded = False

    global contador
    target = random.randint(200,250)
    if(contador >= target):
        print("ganhou!!!!")
        awarded = True


    print(f"Contador: {contador} | Target: {target}")
    
    
    

    sticker_d = [1189750838722301952, 1213028820320522280]
    sticker_n = [1187411015642648737, 1187415785761669120, 1189751078292553748, 1189751207661682758, 1212889809283194900]
    
    

    portuguese_role = message.guild.get_role(979779292026261554)
    zcash_role = message.guild.get_role(1078741799306268727)
    dev_id = 1095310806385700905
    
    
    sticker_list = await message.guild.fetch_stickers()
    random_sticker = random.choice(sticker_list)  

    for cmd in lista_comandos:
        if unidecode(cmd.lower().replace(" ", "")) in unidecode(message.content.lower().replace(" ", "")):
            replied = True
            if awarded and portuguese_role in message.author.roles and zcash_role not in message.author.roles and message.author.id != dev_id:
                await message.reply(content="Parabéns, você ganhou um prêmio!", file=discord.File('./imagem/Golden_Ticket.png'))                
                contador = 0                
                return
            else:
                contador = contador + 1
        
            while random_sticker.id in sticker_n:
                random_sticker = random.choice(sticker_list) 
        
            try:
                await message.add_reaction ('<:SunIcon:1189330981866451035>') 
                resposta = random.choice(lista_respostas)
                await message.reply(content=resposta,stickers=[random_sticker])
            except:
                print ('erro ao tentar add reação')
            
            break

    for cmdn in lista_comandos_n:
        if replied:
            break 

        if unidecode(cmdn.lower().replace(" ", "")) in unidecode(message.content.lower().replace(" ", "")):
            if awarded and portuguese_role in message.author.roles and zcash_role not in message.author.roles and message.author.id != dev_id: 
                await message.reply(content="Parabéns, você ganhou um prêmio!", file=discord.File('./imagem/Golden_Ticket.png'))                
                contador = 0                
                return 
            else:
                contador = contador + 1
            
            while random_sticker.id in sticker_d:
                random_sticker = random.choice(sticker_list)            
           
            try:
             await message.add_reaction ('<:MoonIcon:1189330979156930702>') 
             resposta = random.choice(lista_respostas_n)
             await message.reply(content=resposta,stickers=[random_sticker])
            except:
                print ('erro ao tentar add reação')
        
            break

    if "zm" in unidecode(message.content).replace(" ", "").lower():
        try :
         await message.add_reaction ('<:Coffee01:1189301205021769758>') 
        except :
            print ('erro ao tentar add reação')    
    elif "zn" in unidecode(message.content).replace(" ", "").lower():
        try :
         await message.add_reaction ('<:Tea01:1189331115106902027>') 
        except :
            print ('erro ao tentar add reação')
client.run(my_token)