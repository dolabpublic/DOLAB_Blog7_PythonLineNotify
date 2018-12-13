import requests, json
import urllib.parse
import sys

LINE_ACCESS_TOKEN = "MBGQR2l2mnSN7bjCeUgKobqS6AC9WMx4Ka3LuZcaCJ4"
URL_LINE = "https://notify-api.line.me/api/notify" 

def line_text(message):	
    msg = urllib.parse.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, data=msg)
    print(session_post.text)

def line_pic(message, path_file):
    file_img = {'imageFile': open(path_file, 'rb')}
    msg = ({'message': message})
    LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
    print(session_post.text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        # <Linux> 
        # python line.py "Hello DOLAB"
        line_text(sys.argv[1])
    else:
        # <Linux> 
        # python line.py "Hello DOLAB" "./logo-dolab.png"
        line_pic(sys.argv[1], sys.argv[2])
    
