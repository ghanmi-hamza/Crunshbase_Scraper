import redis

class Redis:
    
    def __init__(self, redis_host = "localhost", redis_port = 6379, redis_password = ""):
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
 
    
    def verify(self, collection):

        collist = self.database.list_collection_names()
        if collection in collist:
            return(True)
        else:
            return(False)

    def insert_data(self, collection,data):
        collection1 = self.database[collection]
        collection1.insert_one(data)
        return()