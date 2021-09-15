from vimeo_downloader import Vimeo
from bot.helper.telegram_helper.message_utils import *
def getId(link,bot,update):
 linksp=link.split("/")
 print(link)
 for i in linksp:
     print(i)
     if (len(i)==9) and("vimeo" not in i):
        return i
        break
 else:
    sendMessage("didnt found a video id.check if its a correct link", bot, update)
def vimdown(link,site,qul,bot,update):
    

    preLink="https://vimeo.com/"
    Vlink=link.split('?')[0]
    videoId=getId(Vlink,bot,update)
    if site:
     videoEmb=site#.split('/')[-1]
    else:
     videoEmb=False
    if ("http" not in str(videoEmb)) and (videoEmb!=False):
        videoEmb="https://"+videoEmb
    if videoEmb:
     v = Vimeo(preLink+str(videoId),videoEmb)#503166067')
    else:
     v = Vimeo(preLink+str(videoId))
    try:
     qu=qul
    st = v.streams
    for s in st:
            if qu in s.quality :
                    return s.direct_url
                    break
    else: # If loop never breaks
        for s in st:
            return s.direct_url
            sendMessage(f"requested Quality not found. Downoading {s.quality}")
