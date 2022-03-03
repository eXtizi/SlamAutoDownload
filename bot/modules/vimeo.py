import requests
from bot.helper.telegram_helper.message_utils import *
def Vimeo(videoId,videoEmb=''):
   data = {
  'id': videoId,
  'ref': videoEmb
}

   response = requests.post('https://apivimeo.herokuapp.com/vim.php',  data=data)
   return response.json()
def getId(link,bot,update):
 linksp=link.split("/")
 print(link)
 for i in linksp:
     i=i.strip()
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
     v = Vimeo(str(videoId),videoEmb)#503166067')
    else:
     v = Vimeo(str(videoId))
    qu=qul
    
    st = v["data"]

    try:
     name=st["name"]
     thumb=st["thumb"]
     sendMessage(f"Name : {name}\nThumbnail :{thumb}", bot, update)
    except Exception as e:
         sendMessage(f"Error Occured : {e}", bot, update)

    for s in st:
            if qu in s :
                    return st[s]
                    break
    else: # If loop never breaks
        for s in st:
           if '0p' in s:
            return st[s]
            sendMessage(f"requested Quality not found. Downoading {s.quality}", bot, update)
