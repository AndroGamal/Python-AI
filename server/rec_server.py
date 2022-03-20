from threading import Thread
import socket
import multiprocessing
import os
import pandas as pd  

DATASET_Folder="/home/andro/url_moves/ml-latest"
movies = pd.read_csv(os.path.join(DATASET_Folder, "movies.csv"))
manager = multiprocessing.Manager()
rate=manager.dict()
user=manager.dict({"id":None})
films=manager.list()
ip=socket.gethostbyname(socket.gethostname())
port=8080
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
server.listen()
names = ["John Ali", "Ali Mahmoud", "Mahmoud Azeem", "Azeem Azeez", "Azeez Mohsen","Mohsen Edward", "Edward Salah","Salah Thomas", "Thomas Hakeem", "Hakeem Yosef", "Yosef Yaseen",
            "Yaseen Essam", "Essam Bernard", "Bernard Mohamed", "Mohamed Mina", "Mina Sam", "Sam Dexter", "Dexter VI", "VI Morgan", "Morgan Monsef", "Monsef Masry", "Masry Hamasa",
            "Hamasa Aboutreka", "Aboutreka Jinx", "Jinx John"]
def get_id_user():
  while(user["id"]==None):
    continue
  id_user = names.index(user["id"])
  return id_user

def set_film(ids):
  for i in ids:
    films.append(i)
def get_film():
  a=""
  while(len(films)==0):
    continue
  for h in films:
    row=movies.loc[lambda movies: movies['imdbId'] == h]
    a+='''
<a href="#home">
<div class="left">
<center>
<img src="'''+row.iloc[-1, row.columns.get_loc('poster_url')]+'''" alt="None image" width="150" height="150"/>
<figcaption>'''+row.iloc[-1, row.columns.get_loc('title')]+'''</figcaption> 
</center>
</div></a>'''
  return a


def get_rate():
  while(len(rate)==0):
    continue
  return rate

def send_html(client_sock,login):
    s='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="'''+ip+str(port)+'''/&image=GO.png" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OrderGo</title>
    <style>
    * {
  padding: 0;
  margin: 0;
  font-family: "lato";
}

body {
  background-color: #f1f1f1;
  position: relative;
  min-height: 100vh;
}
nav {
  background-color: #191919;
  padding: 0 15px;
  border-bottom: 3px solid #ff6600;
  height: 6vh;
  min-height: 60px;
  display: flex;
  align-items: center;
}

nav img {
  width: 128px;
  height: 50px;
}
.cont {
  display: flex;
  flex-direction: column-reverse;
}

body::-webkit-scrollbar {
  width: 10px;
}

body::-webkit-scrollbar-track {
  background: #fff;
}
div.scrollmenu {
  background-color: #333;
  overflow: auto;
  white-space: nowrap;
}

div.scrollmenu a {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px;
  text-decoration: none;
}

div.scrollmenu a:hover {
  background-color: #777;
}
body::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 10px;
}

body::-webkit-scrollbar-thumb:hover {
  background: #555;
}
.q3
{  
width:90%;
background-color: black;
border: 1;
color: white;
padding: 16px 32px;
text-decoration: none;
margin: 4px 2px;
cursor: pointer;
}
.tx
{  
width:80%;
background-color: #4CAF60;
border: none;
color: white;
padding: 16px 32px;
text-decoration: none;
margin: 4px 2px;
}
.bg-logo {
  position: absolute;
  z-index: -2;
  top: 50%;
  left: 50%;
  opacity: 0.4;
  transform: translate(-50%, -50%);
}
    </style>
</head>
<body>
<img src="'''+ip+":"+str(port)+'''/&image=GO.png" alt="ordergo" class="bg-logo" />
<nav>
<img src="'''+ip+":"+str(port)+'''/&image=logo.png" alt="logo" />
</nav>
'''
    if login:
      s+='''<div class="scrollmenu">'''+get_film()+'''
      </div>
      </body>
</html>'''
    else:
        s+='''
<form action="login.html" method="post(a)">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<center>
<table  name="a" style="width:50%">
<tr> 
<td>
<center> 
<table style="width:100%;height:100%" 
<tr>
<td>
<center>
<input class="tx" type="text" name="frist_name"  placeholder="enter your first name" value="" > 
</center>
</td>
</tr>
<tr>
<td>
<center>
<input class="tx" type="text" name="second_name"  placeholder="enter your second name" value="" > 
</center>
</td>
</tr>
</table> 
</center>
<center>
<input class="q3"type="submit"name="f"value="Sign in" >
</center>
</td>
</tr>
</table>
</center>
</form>
</body>
</html>'''
    client_sock.send("HTTP/1.1 200 \r\n".encode('utf-8'))
    client_sock.send("Content type: text/html \r\n".encode('utf-8'))
    client_sock.send(("Content length: "+str(s.count)+" \r\n").encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    client_sock.send((s+"\r\n").encode('utf-8'))
    client_sock.shutdown(socket.SHUT_RDWR)
def start():
    while(True):
        client_sock, client_addr=server.accept()
        s=str(client_sock.recv(1500))
        s=s[0:s.find(" HTTP")]
        if s.find("rate=") != -1:
          rate[s[s.find("usr_name=")+9:]]={"name_film":s[s.find("name_film=")+10:s.rfind("&")],"rate":s[s.find("rate=")+5:s.find("&")]}
        elif s.find("&image=logo.png") != -1:
            t=Thread(target= send_image,args=(client_sock, "/home/andro/url_moves/images/logo.png"))
            t.start()
        elif s.find("&image=GO.png") != -1:
            t=Thread(target= send_image,args=(client_sock, "/home/andro/url_moves/images/GO.png"))
            t.start()
        elif s.find("frist_name=") != -1:
            user["id"]=s[s.find("frist_name=")+11:s.find("&")]+" "+s[s.find("second_name=")+12:s.rfind("&")]
            t=Thread(target= send_html,args=(client_sock,True))
            t.start()
        else:
             t=Thread(target= send_html,args=(client_sock,False))
             t.start()
def send_image(client_sock,locatin):
    client_sock.send("HTTP/1.1 200\r\n".encode('utf-8'))
    client_sock.send("Content type: image/png \r\n".encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    with open(locatin, 'rb') as f:
        client_sock.sendfile(f, 0)
        f.close()
    client_sock.shutdown(socket.SHUT_RDWR)
def send_json(client_sock):
  json=str(rate).replace("'",'"')
  client_sock.send("HTTP/1.1 200 \r\n".encode('utf-8'))
  client_sock.send("Content-type:application/json\r\n".encode('utf-8'))
  client_sock.send(("\r\n").encode('utf-8'))
  client_sock.send(json.encode('utf-8'))
  client_sock.shutdown(socket.SHUT_RDWR)
Thread(target=start).start()