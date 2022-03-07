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

async def decode(teks):
    bl=teks.split("start=")
    bos=bl[0]+"start="
    l1=bl[1].strip("=")
    l2=l1+("="*(len(l1)%4))
    l3=l2.encode('ascii')
    l4=base64.urlsafe_b64decode(l3)
    l5=l4.decode('ascii')
    print("tercode",bos,l5)
    return(bos,l5)
async def encode(angka):
    e1=str(angka).encode("ascii")
    e2= base64.urlsafe_b64encode(e1)
    e3= (e2.decode("ascii")).strip("=")
    return(e3)
async def olah(bos,sangka):
    print(sangka)
    a1=int(sangka)
    pot=[]
    iot=[]
    for i in range (10000,0,-1):
        if a1%i==0:
            if str(a1/i)[:3]=="100":
                pot.append(round(a1/i))
                iot.append(i)
    tekolah=""
    if len(pot)==0:tekolah=sangka+" Tak diketemukan\n"
    for i in range  (len(pot)):
        tekolah+="Id ch: "+str(pot[i])+" "+str(iot[i])+"\n"
        t1="get-"+str(pot[i]*1)+"-"+str(pot[i]*9987)
        t2=await encode(t1)
        while len(t2)%4!=0:
            t2+="="
        tekolah+=bos+t2+"\n"
    print(tekolah)
    return(tekolah)

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



#@bot.on(events.NewMessage(pattern='http'))
async def send_welcome(event):
    bos,l5=await decode(event.message.message)
    l6=l5.split("-")
    tekolah=""
    for i in range (1,len(l6)):
        tekolah+=str(l6[i])+" "+await olah(bos,l6[i])
    await event.reply(tekolah)

#@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    isi=event.message.message
    await event.reply("st  "+isi)

#@bot.on(events.NewMessage()) 
async def send_welcome444(event):          
    await event.reply(event.message)
    global r,bot1,asisten1
    if r==0:
        r+=1
        bot1.run_until_disconnected()
    if r==1:
        r+=1
        asisten1.run_until_disconnected()
    if event.message.message=="x":
        print("$%^&&")
        await  bot.disconnect()
    #print(event.message)

#@bot1.on(events.NewMessage())
async def send_welcome1(event):
    await event.reply(event.message)
    if event.message.message=="x":
        print("$%^&&")
        await  bot1.disconnect()
    #print(event.message)

async def main():
    async with TelegramClient(StringSession(stasisten),10092191,"1d3cc411270e52f1168d3c2fada92bcd") as asisten1:
        await asisten1.send_message('me', 'Hello, myself!')
        await client.run_until_disconnected()
        
    
try:await main()

# Otherwise
except:asyncio.run(main())

#@asisten1.on(events.NewMessage(chats=(gw,aq)))#from_users=lambda e:if e==aq or e==gw))
async def keaq(event):
    global timebisu
    print(event.stringify())
    if event.message.reply_to:
        pesan=await asisten1(functions.messages.GetMessagesRequest(id=[event.message.reply_to.reply_to_msg_id]))
        print(pesan.stringify())
        await asyncio.sleep(1)
        
        async for m in asisten1.iter_messages(pesan.users[2]):
                if pesan.messages[0].message==m.message:
                    idne=m.id
                    break
        #except:idne=0
        #idne=4997
        print(idne)
        await asisten1.send_message(pesan.users[2],event.message,reply_to=idne)#.username,event.message.message,reply_to=4969)#pesan.messages[0].id)
        await asyncio.sleep(1)
        """
        try:
            await pesan.reply(event.message)
            print(123)
        except:
            await pesan.messages[0].reply("ffwedd")#event.message.message)"""

    if "|" in event.message.message:
        pesan=event.message.message.split("|")
        siapa=pesan[0]
        isijawaban=pesan[1]
        await asisten1.send_message(siapa,isijawaban)
        print("udahjawab")
    if event.message.message=="cuy":
        await asisten1.disconnect()                 
        await bot.disconnect()
        await bot1.disconnect()                         
        exit()                                                      
    if "bisuu" in event.message.message:                        
            try:                                                    
                pd=int(event.message.message.split()[1])            
                timebisu=time.time()+(pd*60)                    
                print(timebisu)
                print("dibisukan",time.ctime(timebisu)) 
            except:print("error bisu")

#@asisten1.on(events.NewMessage())#(from_users!=aq))
async def jawabasisten(event):
    #print(event.stringify())
    global akunsudah,timebisu
    try:
        usernya= event.message.from_id.user_id 
        if usernya in intiid:return
        print(usernya,intiid)
        print(event.stringify())
        #print("from",event.message.from_id)
        if event.message.media:
            #print("ada poto")   
            print(event.stringify())
            await event.forward_to(aq)
            await asyncio.sleep(2)
            namee= await event.get_sender()
            teks="Wah Kak "+namee.first_name
            teks+=",\nIni apa kak?\nAssisten Ayu💋💋 "
            await event.reply(teks)
            #print("poto")                                           
            
        if event.message.from_id:
            print("peer user",event.message.peer_id.user_id)
            #print(event.stringify())
            if event.message.peer_id.user_id:
                #if event.message.peer_id.user_id==5044088670:
                    #print(event.stringify())
                
                if event.message.media:
                    print("ada potio")
                    await event.forward_to(aq)
                    #print("poto")
                    return
                if await cekbisu():
                    print("bisu",timebisu)
                    return
                if event.message.peer_id.user_id in akunsudah:
                    await event.respond("Pesan kaka sudah di teruskan ke pemilik akun ini. Salam Assisten Ayu 👩‍🏫 ")
                    await asyncio.sleep(1)
                    await asisten1.forward_messages(aq,event.message)
                    #siapa= await event.get_sender()
                    #await asisten1.send_message(aq,event.message.message+"\n"+siapa.first_name+" "+siapa.username)
                    #print("masuk di akunsudah")
                    return
                #print(event.message.message)
                #print(event.message.stringify())
                #try:
                #print("nama1")
                try:
                    namee= await event.get_sender()#event)
                    #print("nama2")
                #except Exception as e:print(e)
                    #print(namee,event.message.peer_id.user_id)
                    #print("bisanama")
                    teks=("Halo Kak "+namee.first_name+" @"+namee.username)
                except:
                    teks=("Halo Kak "+namee.first_name)
                teks+="\n\n Saya assisten nya @nokos_easy\n"
                teks+=" Saya akan menghubungi pemilik akun ini segera"
                teks+="\n Mohon bersabar menunggu. Terima kasih\n\n"
                teks+="Silahkan Kaka baca tulisan ini sebentar::\n \n [-Tentang Nokos](https://telegra.ph/Seputar-Nokos-03-03)\n\n [-Tentang Video easy](https://telegra.ph/seputar-pideo-nokos-easy-03-03)\n\nKalau masih ada yang bingung boleh ditanyakan kesini nnti akan segera di balas oleh @nokos_easy langsung. Atau kirimkan foto transferannya pasti dijawab cepet.. hehehe ^_^\nSalam Assisten Ayu 💋"
                #print(event.stringify())
                try:
                    await asyncio.sleep(2)
                    await event.respond(teks,link_preview=False)
                    akunsudah.append(event.message.peer_id.user_id)
                    print(akunsudah)
                    await asyncio.sleep(1)
                    #await asisten1.send_message(aq,event.message.message)
                    #await asyncio.sleep(1)
                    await asisten1.forward_messages(aq,event.message)
                except Exception as e:print("ee",e)
        else:
            #chat_from = event.chat if event.chat else (await event.get_chat()) # telegram MAY not send the chat enity
            #chat_title = chat_from.title
            #print(chat_title)
            pass#rint(event.message.stringify())
    except Exception as e:
        print("e",e)

        pass
        #print(event.message.message,event.message.peer_id)
    #if event.message.message=="cuy":
        #await asisten1.disconnect()
        #await bot.disconnect()
        #await bot1.disconnect()
        #exit()
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

#asisten1.send_message("me",'his message has **bold**, `code`, __italics__ and ''[nice website](https://example.com)!')
#asisten1.disconnect()
#bot.run_until_disconnected()
#bot1.disconnect()
#asyncio.run(main())

