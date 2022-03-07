from telethon.sync import TelegramClient
desa="kampungmaifambot"
import time
import asyncio

def cara():
    print("akun=lojin.akun(akunyangada=[])")
    print("akuns=lojin.login1(akun)  sampe 5 dan 10")

def grup(akuns):
    chennel=akuns.get_entity('t.me/joinchat/KEi3tBvIIQNS_YHAPfP49w')
    return (chennel)
            

def akun(akunyangada=[]):
    akun=[]
    if akunyangada!=[]:
        for i in akunyangada: akun.append(i)
    print(akun)
    sih=["01long"]
    sth=["sth1","sthm","sthj","sthk","sthh","sthn","sthu","sthd"]#"sthb","sthn","sthu","sthp","sthd"]
    #sth=["sth1","sthm","sthj","sthk","sthh","sthb","sthn","sthu","sthp","sthd"]
    mrj=["mrj1","mrjm","mrjh","mrjb","mrjn","mrju","mrjd"]
    ffo=["ffo1","ffom","ffoj","ffok","ffoh","ffob","ffon","ffou","ffod"]
    iis=["iis1","iism","iisk","iish"]
    bks=["bksm","bksj","bksh","bksb","bksn","bksu",]
    all=sth+mrj+ffo+iis+bks+sih
    spm=["mrjk","mrjp","ffop"]
    
    while True:
        acun=input("masukkan akun : ")
        if acun=="x":
            break
        elif acun == "sih":
            for i in sih:
                akun.append(i)
        elif acun == "sth":
            for i in sth:
                akun.append(i)
        elif acun == "mrj":
            for i in mrj:
                akun.append(i)
        elif acun == "ffo":
            for i in ffo:
                akun.append(i)
        elif acun == "iis":
            for i in iis:
                akun.append(i)
        elif acun == "bks":
            for i in bks:
                akun.append(i)
        elif acun == "all":
            for i in all:
                akun.append(i)
        elif acun == "spm":
            for i in spm:
                akun.append(i)
        else:
            try:
                o=open("akunakun/"+acun+".txt","r")
                akun.append(acun)
                o.close()
            except:
                print("file :", acun, "tidak ditemukan1")
    #print(akun)
    akun=list(dict.fromkeys(akun))
    print("--------------------")
    print("   jumlah akun : ", len(akun))
    for i in range (len(akun)): print ("    ",i, akun[i])
    return(akun)

def login1(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session1/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session1/"+a,int(l[1]),l[2]))
    return(client)

def login2(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()  
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session2/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session2/"+a,int(l[1]),l[2]))
    return(client)

def login3(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session3/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session3/"+a,int(l[1]),l[2]))
    return(client)

def login4(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session4/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session4/"+a,int(l[1]),l[2]))
    return(client)

def login5(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session5/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session5/"+a,int(l[1]),l[2]))
    return(client)

def login10(isi):
    cek= isinstance(isi,list)
    aa=[]
    client=[]
    if cek ==True:
        aa=isi
    else:
        aa=[]
        aa.append(isi)
        client=[]
    for a in aa:
        o=open("akunakun/"+a+".txt","r")
        p=o.read()
        l=p.split()
        o.close()
        if len(aa)==1:
            client=TelegramClient("session/"+a,int(l[1]),l[2])
        else:
            client.append(TelegramClient("session/"+a,int(l[1]),l[2]))
    return(client)
