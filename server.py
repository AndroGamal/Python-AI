from re import L
from threading import Thread
import socket
class user:
    users={}
    ID=0
    def __init__(self,id,name,time):
        self.ID=id
        self.users[id]={'Name':name,'Items':{},'TimeCheckin':time}
    def PickUp(self,Item_id,Quantity):
        self.users[self.ID]['Items'][Item_id]=Quantity
    def PutBack(self,Item_id,Quantityback):
        self.users[self.ID]['Items'][Item_id]=self.users[self.ID]['Items'][Item_id]-Quantityback
    def CheckOut(self,time):
        self.users[self.ID]['TimeCheckout']=time


def get():
    out=""
    l_user=list(user.users)
    for i in range(0,len(l_user)):
        l_item=list(user.users[l_user[i]]['Items'])
        l_item_value=list(user.users[l_user[i]]['Items'].values())
        out+='''<table>
        <tr>
        <th colspan="2">
        '''+user.users[l_user[i]]["Name"]+'''
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
    s='''<html>
    <head>
    <meta chareset=\"UTF-8\">
    <meta http-equiv="refresh" content="5">
    <style>
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
    <body>'''+get()+'''</body>
    </html>'''
    client_sock.send("HTTP/1.1 200\r\n".encode('utf-8'))
    client_sock.send("Content type: text/html\r\n".encode('utf-8'))
    client_sock.send(("Content length: "+str(s.count)+"\r\n").encode('utf-8'))
    client_sock.send(("\r\n").encode('utf-8'))
    client_sock.send((s+"\r\n").encode('utf-8'))
    client_sock.shutdown(socket.SHUT_RDWR)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()),8080))
server.listen()
def start():
    while(True):
        client_sock, client_addr=server.accept()
        t=Thread(target= send,args=(client_sock, client_addr))
        t.start()
