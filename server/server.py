from threading import Thread
import socket
class user:
    users={}
    def ChickIn(self,id,time):
        name=["andro","kero","Nesr"]
        self.users[id]={'Name':name[id%3]+str(int(id/3)),'Items':{},'TimeCheckin':time}
    def PickUp(self,id,Item_id,Quantity):
        self.users[id]['Items'][Item_id]=Quantity
    def PutBack(self,id,Item_id,Quantityback):
        self.users[id]['Items'][Item_id]=self.users[id]['Items'][Item_id]-Quantityback
    def CheckOut(self,id,time):
        self.users[id]['TimeCheckout']=time
def get():
    out=""
    l_user=list(user.users)
    for i in range(0,len(l_user)):
        l_item=list(user.users[l_user[i]]['Items'])
        l_item_value=list(user.users[l_user[i]]['Items'].values())
        out+='''<table>
        <tr>
        <th>
        '''+str(user.users[l_user[i]]["Name"])+'''
        </th>
         <th>
        '''+str(user.users[l_user[i]]["TimeCheckin"])+'''
        </th>
        </tr>
        '''
        for r in range(0,len(l_item)):
            out+='''<tr>
            <td>'''+str(l_item[r])+'</td><td>'+str(l_item_value[r])+'''</td>
            </tr>'''
        out+='''</table>
        <p>&nbsp;<p>'''
    return out
def send(client_sock, client_addr):
    s='''<!DOCTYPE html>
    <html>
    <head>
    <meta chareset=\"UTF-8\">
    <meta http-equiv="refresh" content="10">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <style>
    body,html {
  background-image: url("'''+ip+'''/&image=GO.png");
  height: 100%;
  background-repeat: no-repeat;
  background-attachment: fixed;  
  background-size: cover;
  margin: 0;
        }
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
    </head>
    <body>'''+get()+'''
    </body>
    </html>'''
    client_sock.send("HTTP/1.1 200\r\n".encode('utf-8'))
    client_sock.send("Content type: text/html\r\n".encode('utf-8'))
    client_sock.send(("Content length: "+str(s.count)+"\r\n").encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    client_sock.send((s+"\r\n").encode('utf-8'))
    client_sock.shutdown(socket.SHUT_RDWR)
ip=socket.gethostbyname(socket.gethostname())
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip,8080))
server.listen()
def start():
    while(True):
        client_sock, client_addr=server.accept()
        s=client_sock.recv(1500)
        #print(s)
        if str(s).find("&image=logo.png") != -1:
            t=Thread(target= send_image,args=(client_sock, "/media/andro/0678823e-9314-4adb-aab0-eeaced6c3d21/Work/vedio/server/images/logo.png"))
            t.start()
        elif str(s).find("&image=GO.png") != -1:
            t=Thread(target= send_image,args=(client_sock, "/media/andro/0678823e-9314-4adb-aab0-eeaced6c3d21/Work/vedio/server/images/GO.png"))
            t.start()
        else:
             t=Thread(target= send,args=(client_sock, client_addr))
             t.start()
def send_image(client_sock,locatin):
    client_sock.send("HTTP/1.1 200\r\n".encode('utf-8'))
    client_sock.send("Content type: image/png \r\n".encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    with open(locatin, 'rb') as f:
        client_sock.sendfile(f, 0)
        f.close()
    client_sock.shutdown(socket.SHUT_RDWR)


Thread(target=start).start()