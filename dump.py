import re
import os
from telethon import TelegramClient, events, sync, functions, types, utils
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChat
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

name = 'session' #Название файла сесии
api_id = 23423434 ##Тут все ясно. если нет то лучше не ставь бота. ты тупой
api_hash = 'хэш тута' #Тут все ясно. если нет то лучше не ставь бота. ты тупой
adm_id = 12342344 #Ваш чат id 

client = TelegramClient(name, api_id, api_hash)
client.start()

def scope():
    try:
        count = 0
        with open (f'cc.txt','rb') as f:
            for line in f:
                count+=1
        return count
    except Exception as er:
        return er

@client.on(events.NewMessage)
async def reaction(event):
    message = event.message.message
    chatid = int(event.message.from_id.user_id)
    if message:
        filt = re.findall(r"\d{16}\S\d{2}\S\d{4}\S\d{3}", message, flags=re.M) #2202|22|2222|222
        if filt:
            print("Поймал 1")
            for item in filt:
                my_file = open("cc.txt", "at")
                my_file.write(f"{item}\n")
                my_file.close()
                
        filt1 = re.findall(r"\d{16}\s\d{2}/\d{4}\s\d{3}", message, flags=re.M) # 2202 22/2022 222
        if filt1:
            print("Поймал 2")
            for item in filt1:
                text = item.replace(' ', '|')
                my_file = open("cc.txt", "at")
                my_file.write(f"{text.replace('/', '|')}\n")
                my_file.close()
                
        filt2 = re.findall(r"\d{16}\S\d{2}\S\d{2}\S\d{3}", message, flags=re.M) #2202|22|22|222
        if filt2:
            print("Поймал 3")
            for item in filt2:
                my_file = open("cc.txt", "at") #Люблю аню, и всегда буду любить!
                my_file.write(f"{item}\n")
                my_file.close()
                
        filt3 = re.findall(r"\d{16}\s\d{2}/\d{2}\s\d{3}", message, flags=re.M) #2202 22/22 222
        if filt3:
            print("Поймал 4")
            for item in filt3:
                text = item.replace(' ', '|')
                my_file = open("cc.txt", "at")
                my_file.write(f"{text.replace('/', '|')}\n")
                my_file.close()
                
        if message == ".delclone":
            if chatid == adm_id:
                try:
                    id_msg = event.message.id
                    chat_group = event.message.peer_id.channel_id
                    await client.edit_message(chat_group, id_msg, 'Удаление мусора...')
                    cout = scope()
                    lines_set = set()
                    with open(r"cc.txt", "r") as fin, open(r"cc1.txt", "w") as fout:
                        for line in fin:
                            if line not in lines_set:
                                fout.write(line)
                            lines_set.add(line)
                    os.remove("cc.txt")
                    os.rename('cc1.txt', 'cc.txt')
                    new = scope()
                    await client.edit_message(chat_group, id_msg, f'Было строк: {cout}\nСтало строк: {new}\nИ того удалено: {cout - new}')
                except Exception as e:
                    print(f"Ошибка: {e}")
        if message == ".unloadcc":
            if chatid == adm_id:
                try:
                    id_msg = event.message.id
                    chat_group = event.message.peer_id.channel_id
                    await client.delete_messages(chat_group, id_msg)
                    await client.send_file(chat_group, 'cc.txt')
                except Exception as e:
                    print(f"Ошибка: {e}")
                    
        if message == ".helpcc":
            if chatid == adm_id:
                try:
                    id_msg = event.message.id
                    chat_group = event.message.peer_id.channel_id
                    await client.edit_message(chat_group, id_msg, f'<b>Бот Dump CC</b>\n\nКоманды бота:\n<code>.helpcc</code> - Вывести доступные команды\n<code>.delclone</code> - Удалить дубли строк\n<code>.unloadcc</code> - Выгрузить файл дампа', parse_mode="html")
                except Exception as e:
                    print(f"Ошибка: {e}")
                    
client.run_until_disconnected()