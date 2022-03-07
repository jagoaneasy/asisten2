from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl import functions,types
# Initialize bot and... just the bot!
import asyncio,base64,time
import random
#bot = TelegramClient('bot', 11716851, '9cf7b885f6a39ba1acec9572c65ca810').start(bot_token='5164503867:AAGI0ZG9DfYrginWMozPNa8_T_93uNt-c7E')

#bot1 = TelegramClient('bot1', 11716851, '9cf7b885f6a39ba1acec9572c65ca810').start(bot_token='5292078688:AAEiQ3-7hkqnheUaE7qOaDQbZaeo36Osnkg')

stasisten='1BVtsOGgBuwOPDg-dHXNIUnvKclxBNJj9FROk6jZK3UbJeH54sihBfrY4D7kRyNk9qffE5_Zi9HTEQnsBD3hgkaqiBkfo9Mugo6xtswJINmOAcmMUiiwavIEd9x3X6uRog3sbdll9Zm4AJ-5jHWRCc-leJWM6YXotDusd7d3QVna36SW0WOXtg9kDgzH8hGEzcHh9c1itFPOSNIQ6BztakXLTynCZqzVS6PejfKBT7mFLDppJJXyAiKbG_pDoXDW-DsNs39WLwzT8m3_Qj72wTx473Cj8eD8SIt6Id9V5jb8RMVkZAtP9jmaO1qYUi-ld9GFzHIf9ugt2eg22vsx9vGiYmpcoYYA='
r=770

#import lojin
#asisten1=lojin.login1("bks1")
asisten1=TelegramClient(StringSession(stasisten),10092191,"1d3cc411270e52f1168d3c2fada92bcd")
aq="batman800"
gw="grungeisnotdead"
intiid=[667384754,675854260,5035559152]
timebisu=0
akunsudah=[]
stopin=True
ditgl=time.time()//(3600*24)
Ayu=b'Ayu \xf0\x9f\x92\x8b'
ayu=Ayu.decode()
Kis=b'\xf0\x9f\x92\x8b\xf0\x9f\x92\x8b'
kis=Kis.decode()
Bayi=b'\xf0\x9f\x94\xba'
bayi=Bayi.decode()
akun2inti=[667384754,675854260]
spk=b'\xf0\x9f\x94\x89 '
sp=spk.decode()
Memo=b'\xf0\x9f\x93\x9d'
memo=Memo.decode()
Mediac=b'\xf0\x9f\x93\xb1\xf0\x9f\x93\x80'
mediac=Mediac.decode()
balesan=["Pesan kaka sudah di teruskan ke pemilik akun ini.\n ","Sudah saya ingatkan ke pemilik akun untuk membalas chat kaka.\n ","Tunggu sebentar ya kak. pemilik akunnya slow respon. Maaf.\n ","Agaknya pemilik akun ini masih sibuk (slow respon). Maaf.\n ","Sudah saya ingatkan ke pemilik akun ini.\n "]
sdhchat=[]
gc=0
async def cekbisu():
    global akunsudah
    if time.time()//(3600*24)!=ditgl:
        akunsudah=[]
    if time.time()-timebisu<0:return True
    else:return False


async def main():
    async with TelegramClient(StringSession(stasisten),10092191,"1d3cc411270e52f1168d3c2fada92bcd") as asisten1:
        await asisten1.send_message('me', 'Hello, myself!')
        


        @asisten1.on(events.NewMessage())
        async def bacaasisten(event):
            global sdhchat,ditgl,gc,timebisu
            pesan=event.message.message
            print("-->",pesan)

            if gc==0:
                gc=await asisten1.get_entity(-1001715337037)
                #print(gc)
            #baca
            try:
                #dr user
                user=event.message.peer_id.user_id
                #bkn bot
                if event.message.media:
                    print("mediadd")
                    namee= await event.get_sender()
                    await asisten1.send_message(gc,mediac+"[Laporan.xls](https://gmail.com/) -"+str((event.message.id))+" "+namee.first_name[:3])
                    teks="Wah Kak "+namee.first_name
                    teks+=",\nIni ngirim apa kak?\nkusimpen buat @nokos_easy kan.\nAssisten Ayu"+kis
                    await event.reply(teks)
                elif event.message.from_id:
                    #yg masuk
                    if event.message.out==False:
                        #bkn 2  akuninti
                        if event.message.peer_id.user_id not in akun2inti:
                            #print(event.stringify())
                            #print("M")
                            if time.time()//(3600*24)!=ditgl:
                                ditgl=time.time()//(3600*24)
                                sdhchat==[]
                            #print("MM")
                            if pesan=="cuy":
                                await asisten1,send_message(gc,"stop connection")
                                await asisten1.disconnect()
                                return
                            #print("MMMM")

                            if "apa_" in pesan:
                                teks= sp+sp+" Hai Kak, saya Indah "+ayu+"\nKaka kepengin punya assisten spt saya, rekrut saya aja kak. "+memo+"\n\n Tarifnya tergantung kerumitan tugas saya kak paling sekitaran 20k-200k untuk ngebuat tugasnya. Semua tugas bisa saya lakukan kok kak, g cuman jawab pesan masuk aja, tapi bisa buat reminder, jawab pesan di grup, mengatur grup, ngirim gambar, ngatur pesan terjadwal, dan lain-lain sesuka kaka, asal jgn di ajak VCS aja .. hihihihi ;)\n\n Kalau kaka minat tanya aja ya ke Mimin @nokos_easy \nDitunggu rekrutannya dan traktir saya ya... Salam "+ayu
                                await event.respond(teks)
                                return
                            if await cekbisu():
                                print("bisu",timebisu)
                                return
                            if event.message.peer_id.user_id in sdhchat:
                                teksb=b'Salam Assisten Ayu \xf0\x9f\x91\xa9\xe2\x80\x8d\xf0\x9f\x8f\xab'
                                teks=sp+random.choice(balesan)+teksb.decode()+"\n(butuh asissten spt ayu ketik : 'sapa_Ayu')"
                                print("ada yg ngechat lagi")
                                await asyncio.sleep(1)
                                await event.respond(teks)
                                await asyncio.sleep(1)
                                namee= await event.get_sender()#event)  
                                await asisten1.send_message(gc,"[Laporan.xls](https://gmail.com/) -" +str((event.message.id))+" "+namee.first_name[:3])

                            else:
                                print("ada akun baru chat")
                                try:
                                    namee= await event.get_sender()#event)      
                                    teks=(sp+"Halo Kak "+namee.first_name+" @"+namee.username)             
                                except: 
                                    teks=(sp+"Halo Kak "+namee.first_name)
                                teks+="\n\n Saya assisten nya @nokos_easy\n Saya akan menghubungi pemilik akun ini segera\n Mohon bersabar menunggu. Terima kasih\n\nSilahkan Kaka baca tulisan ini sebentar::\n \n [-Tentang Nokos](https://telegra.ph/Seputar-Nokos-03-03)\n\n [-Tentang Video easy](https://telegra.ph/seputar-pideo-nokos-easy-03-03)\n\nKalaumasih ada yang bingung boleh ditanyakan kesini nnti akan segera di balas oleh @nokos_easy langsung. Atau kirimkan foto transferannya pasti dijawab cepet.. hehehe ^_^\nSalam Assisten "+ayu
                                sdhchat.append(event.message.peer_id.user_id)
                                await asyncio.sleep(1)
                                await event.respond(teks,link_preview=False)
                                await asyncio.sleep(1)
                                await asisten1.send_message(gc,bayi+" [Laporan.xls](https://gmail.com/) -" +str((event.message.id))+" "+namee.first_name[:3])
                                print("samakan id",event.message.id)
                else:
                    print("akun")
                    print(event.stringify())
            except Exception as e:
                #print(e)
                print("bkn user")
                if await cekbisu():
                                print("bisu",timebisu)
                                return
                try:
                    if event.message.from_id:
                        if "bisuu" in event.message.message:                        
                            try:                                                    
                                pd=int(event.message.message.split()[1])            
                                timebisu=time.time()+(pd*60)                    
                                print(timebisu)
                                print("dibisukan",time.ctime(timebisu)) 
                                return
                            except:print("error bisu")
                        if pesan=="cuy":
                            await asisten1.disconnect()
                            return
                        if "." in pesan[0]:
                            #try:
                                siid=int(pesan.split()[0][1:])
                                print(siid)
                                await asyncio.sleep(2)
                                await event.delete()
                                sipes=await asisten1(functions.messages.GetMessagesRequest(id=[siid]))
                                #print(sipes.stringify())

                                #print("sipes")
                                #print(gc)
                                teks="dari : "+sipes.users[0].first_name 
                                try:teks+=" @"+sipes.users[0].username
                                except:pass
                                teks+="\n-------------\n"+sipes.messages[0].message
                                try:await asisten1.send_file(gc,sipes.messages[0],caption=teks)
                                except:await asisten1.send_message(gc,teks)
                                print(teks)
                                async for m in asisten1.iter_messages(gc):
                                    #print(m.message)
                                    if "dari"  in m.message:
                                        await asyncio.sleep(10)
                                        await m.delete()
                                        break
                except:print("ERROR")


                #print(event.stringify())

        await asisten1.run_until_disconnected()

#

        
    


# Otherwise
asyncio.run(main())

while stopin:
    try:
        try:
            asisten1.connect()
        except:
            pass
            
        asisten1.run_until_disconnected()
        print("MuLAI")
    except:
        exit()
        time.sleep(60)
        print("mulaijaringan")


