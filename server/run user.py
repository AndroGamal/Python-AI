

#to start server and push empty HTML page
from server import UI
'''import multiprocessing
manager = multiprocessing.Manager()
d=manager.dict()
d[1]={"a":"c","l":{}}
v=d[1]
v["l"]={"j":"k"}
d[1]=v
print(d[1])
'''
ux= UI()
ux.ChickIn({'User_id':0,'CheckIn_time':"2022-02-09 11:36:38.974880"})
ux.PickUp({'User_id':0,'Item_id':3,'Quantity':10})
ux.CheckOut({'User_id':0,'CheckOut_time':300})
ux.ChickIn({'User_id':1,'CheckIn_time':"2022-02-09 11:36:38.974880"})
ux.PickUp({'User_id':1,'Item_id':3,'Quantity':10})
ux.CheckOut({'User_id':1,'CheckOut_time':30})
ux.PickUp({'User_id':0,'Item_id':3,'Quantity':10})
#print(os.getcwd() +"/images/logo.png")