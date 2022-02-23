from threading import Thread
from time import sleep
import server
#to start server and push empty HTML page
user= server.UI()
user.ChickIn(0,10)
# to check in user1 
# frist Parameter is id for user can be string or int 
# second Parameter is name user must be string type
# third Parameter is time in 
sleep(5)
user.ChickIn(1,10)
sleep(10)
#to pick up to user1
# frist Parameter is name of Item can be string or int 
# second Parameter is Quantity user must be int type

user.PickUp(1,'salt',2)
sleep(10)
# to check in user2
sleep(10)
#to pick up to user2
user.ChickIn(2,10)
user.PickUp(2,'tea',3)
#do not use this loop this loop to test only
while True:
    sleep(10)