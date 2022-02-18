from threading import Thread
from time import sleep
import server
#to start server
Thread(target=server.start).start()
# to check in user
user1= server.user("1","andro",10)
#to pick up 
sleep(10)
user1.PickUp('aa',2)
sleep(10)
user2= server.user("2","micheal",10)
sleep(10)
user2.PickUp('aa',3)
#do net use this loop
while True:
    print(0)