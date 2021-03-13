from functions import Profile
from mongodb import *
#from redis import *

def main():

    #startup_name = 'instadeep'  #'calyo'
    startup_name = 'calyo'
    database_name = 'hamza'

    p=Profile(startup_name)
    p.get_browser()
    data={}
    data.update(p.summary())
    data.update(p.technology())
    data.update(p.news())
    data.update(p.people())
    data.update(p.financial())
    p.close_browser()
    #print(data)

    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #mydb = myclient["hamza"]
    #collection = mydb[startup_name]
    #collection.insert_one(data)
    m=MongoDb(database_name)
    if m.verify(startup_name):
        print("data exist")
    else:
        m.insert_data(collection = startup_name, data = data)
        print("data inserted")
    
if __name__=='__main__':
    main()