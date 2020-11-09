import traceback
from time import sleep
import requests
import os

def id(RFCID):
    idxz=len(str(RFCID))
    if idxz != 4:
        if idxz==1:
            xz="000"
            NewRFC_id= "rfc" + xz + str(RFCID)
        elif idxz==2:
            xz = "00"
            NewRFC_id = "rfc" + xz + str(RFCID)
        elif idxz==3:
            xz = "0"
            NewRFC_id = "rfc" + xz + str(RFCID)
    else:
        NewRFC_id="rfc" + str(RFCID)

    tdownurl=url+NewRFC_id+".txt"
    pdownurl=url+NewRFC_id+".pdf"
    return tdownurl,pdownurl

def requestsdownload(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

RFC_id = 1
End_id = 8820+1
url="https://www.ietf.org/rfc/"
for rfcidid in range(RFC_id,End_id):
    #print(id(rfcidid))
    tfilename="RFC/"+str(rfcidid)+".txt"
    pfilename="RFC/"+str(rfcidid)+".pdf"
    requestsdownload(id(rfcidid)[0],tfilename)
    requestsdownload(id(rfcidid)[1],pfilename)
    print("Finish:"+str(rfcidid/8820))
