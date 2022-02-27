import os
from threading import Thread 
import socket
import multiprocessing
manager = multiprocessing.Manager()
class UI:
    users=manager.dict()
    name = ["John", "Ali", "Mahmoud", "Azeem", "Azeez","Mohsen", "Edward","Salah", "Thomas", "Hakeem", "Yosef",
            "Yaseen", "Essam", "Bernard", "Mohamed", "Mina", "Sam", "Dexter", "VI", "Morgan", "Monsef", "Masry",
            "Hamasa", "Aboutreka", "Jinx"]
    list =[ ["Zeina Trio", 7],
                    ["Dream flour", 10],
                    ["Magy", 3.5],
                    ["Soup Bar", 5.5],
                    ["Hyper Oil 3kg", 50],
                    ["Zeina Large Roll", 20],
                    ["Lipton tea 100 gm", 11],
                    ["Elmtbkh vermicilli", 5],
                    ["Cooks salt", 12],
                    ["Maxell floor cleaner", 11],
                    ["Fine Escape", 9.5],
                    ["Cofee mix", 12],
                    ["Elmtbkh small rings", 5.5],
                    ["TopValue vineger", 4.5],
                    ["Prill", 22.5],
                    ["Finer Super", 19.5],
                    ["Elarosa Tea", 32.5],
                    ["Italiano semolina", 22],
                    ["Top value sugar", 10],
                    ["Hyper one 8 kg cleaner", 90],
                    ["Zeina Kitchen Roll", 12],
                    ["Lipton 100 packet", 22],
                    ["Hawaa Pasta", 9],
                    ["Vineger", 6],
                    ["Fabric Softner", 30],
                    ["Papia Roll", 23],
                    ["Royal lemon ginger", 13],
                    ["Regina Spaghetti", 30],
                    ["Honey Drops", 31],
                    ["Feba 4 kg", 29],
                    ["Fine Duetto", 15],
                    ["Nido 288 gm", 31],
                    ["Italino Rings", 27],
                    ["Honey pops", 13],
                    ["clorox 2 kg", 19],
                    ["Fine Fluffy", 35],
                    ["Rabea Tea", 31],
                    ["Queen Pasta", 9.5],
                    ["Fruit Hops", 17.5],
                    ["Clorox 4 kg", 33]
                  ]
    def ChickIn(self,d={}):
      id=d['User_id']
      time=d['CheckIn_time']
      UI.users[id]={'Name':self.name[id%25],'Items':{},'TimeCheckin':time}

    def PickUp(self,d={}):
      id=d['User_id']
      Item_name=UI.list[d['Item_id']][0]
      Quantity=d['Quantity']
      u=UI.users[id]
      v=u['Items']
      v[Item_name]={'Quantity':Quantity,'Price':UI.list[d['Item_id']][1]}
      u['Items']=v
      UI.users[id]=u


    def PutBack(self,d={}):
      id=d['User_id']
      Item_name=UI.list[d['Item_id']][0]
      Quantityback=['Quantity']
      u=UI.users[id]
      v=u['Items']
      k=v[Item_name]
      k['Quantity']=UI.users[id]['Items'][Item_name]['Quantity']-Quantityback
      v[Item_name]=k
      u['Items']=v
      UI.users[id]=u

    def CheckOut(self,d={}):
      id=d['User_id']
      time=d['CheckOut_time']
      u=UI.users[id]
      u['TimeCheckout']=time
      UI.users[id]=u

def send_js(client_sock, client_addr):
    s='''
let url = "'''+ip+":"+str(port)+'''/&api=data.json";
setInterval(()=>{fetch(url).then(res => res.json()).then((out) => {
html=""
for(user in out){
  total_item=0;
  html+="<div class='table'><div class=\\"checkDetails user\\"><h2>Name: "+out[user]["Name"]+"</h2> <h2>"+out[user]["TimeCheckin"]+"</h2></div> <ul><li><span class='list-title'>Item Name</span><span class='list-title text-center'>Quantatiy</span><span class='list-title text-center'>Price</span><span class='list-title text-center'>Total</span></li>";
  for(item in out[user]["Items"]){
    total=out[user]["Items"][item]["Quantity"]*out[user]["Items"][item]["Price"];
    total_item+=total;
    html+="<li><span>"+item+"</span><span class=\\"text-center\\">"+out[user]["Items"][item]["Quantity"]+"</span><span class=\\"text-center\\">"+out[user]["Items"][item]["Price"]+" €</span><span class=\\"text-center\\">"+total+" €</span></li></ul>";
    }
  if("TimeCheckout" in out[user]){
    html+="<div class=\\"checkDetails total\\"><h2>Check Out Time: "+out[user]["TimeCheckout"]+"</h2><h2  class='text-center price'><span class='sm-appear'>Total Price:</span>"+total_item+" €</h2>";
   }
  html+="</div></div><p>&nbsp;<p>";
}
  document.getElementById("add_to_me").innerHTML=html;
}).catch(err => alert(err));},1000);
    '''
    client_sock.send("HTTP/1.1 200\r\n".encode('utf-8'))
    client_sock.send("Content type: text/javascript\r\n".encode('utf-8'))
    client_sock.send(("Content length: "+str(s.count)+"\r\n").encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    client_sock.send((s+"\r\n").encode('utf-8'))
    client_sock.shutdown(socket.SHUT_RDWR)
def send_html(client_sock, client_addr):
    s='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="'''+ip+":"+str(port)+'''/&image=GO.png" />
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

body::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 10px;
}

body::-webkit-scrollbar-thumb:hover {
  background: #555;
}

.bg-logo {
  position: absolute;
  z-index: -2;
  top: 50%;
  left: 50%;
  opacity: 0.4;
  transform: translate(-50%, -50%);
}
li {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  font-size: 1.4rem;
}

li span {
  width: 25%;
}

.user {
  background-color: #ff6600;
  color: black;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.list-title {
  font-weight: bold;
}

.text-center {
  text-align: center;
}
.table {
  background-color: #fff;
  border: 1px solid #777;
  border-radius: 10px;
  margin: 10px 15px;
  transition: 0.5s;
}

p,
h2 {
  font-size: 1.4rem;
  padding: 10px 0;
}

.total {
  border-top: 1px solid #191919;
}

.checkDetails {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
}

.sm-appear {
  display: none;
}

.total h2.price {
  width: 25%;
}
@media (max-width: 1600px) {
  .bg-logo {
    width: 911px;
    height: 500px;
  }
}

@media (max-width: 1000px) {
  .bg-logo {
    width: 547px;
    height: 300px;
  }
}

@media (max-width: 768px) {
  .checkDetails {
    display: block;
  }
  .total h2.price {
    width: 100%;
    text-align: start !important;
  }
  .sm-appear {
    display: inline-block;
  }
}

@media (max-width: 600px) {
  .bg-logo {
    width: 273px;
    height: 150px;
  }
}
    </style>
</head>
<body>
<img src="'''+ip+":"+str(port)+'''/&image=GO.png" alt="ordergo" class="bg-logo" />
<nav>
<img src="'''+ip+":"+str(port)+'''/&image=logo.png" alt="logo" />
</nav>
<dev id ="add_to_me">
</dev>
<script src='''+ip+':'+str(port)+'''/&javascript=script.js >
   </script>
</body>
</html>'''
    client_sock.send("HTTP/1.1 200 \r\n".encode('utf-8'))
    client_sock.send("Content type: text/html \r\n".encode('utf-8'))
    client_sock.send(("Content length: "+str(s.count)+" \r\n").encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    client_sock.send((s+"\r\n").encode('utf-8'))
    client_sock.shutdown(socket.SHUT_RDWR)
ip=socket.gethostbyname(socket.gethostname())
port=1500
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,port))
server.listen()
def start():
    while(True):
        client_sock, client_addr=server.accept()
        s=client_sock.recv(1500)
        #print(s)
        if str(s).find("&image=logo.png") != -1:
            t=Thread(target= send_image,args=(client_sock, os.getcwd()+"/images/logo.png"))
            t.start()
        elif str(s).find("&javascript=script.js") != -1:
             t=Thread(target= send_js,args=(client_sock, client_addr))
             t.start()
        elif str(s).find("&image=GO.png") != -1:
            t=Thread(target= send_image,args=(client_sock, os.getcwd()+"/images/GO.png"))
            t.start()
        elif str(s).find("&api=data.json") != -1:
          send_json(client_sock)
        else:
             t=Thread(target= send_html,args=(client_sock, client_addr))
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
  items=UI.users.items()
  s={str(key): value for key, value in items}
  json=str(s).replace("'",'"')
  client_sock.send("HTTP/1.1 200 \r\n".encode('utf-8'))
  client_sock.send("Content-type:application/json\r\n".encode('utf-8'))
  client_sock.send(("\r\n").encode('utf-8'))
  client_sock.send(json.encode('utf-8'))
  client_sock.shutdown(socket.SHUT_RDWR)

Thread(target=start,).start()