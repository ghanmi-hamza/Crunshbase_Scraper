import pymongo

class MongoDb:
    
    def __init__(self,database_name):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = myclient[database_name]
        #self.database_name = database_name
        #self.database = database
 
    
    def verify(self, collection):

        collist = self.database.list_collection_names()
        if collection in collist:
            return(True)
        else:
            return(False)
    def verify_status(self, collection, status):
        collection2 = self.database[collection]
        if collection2.find_one({ "status": { '$exists': True, '$eq': status } }):
            return(True)
        else:
            return(False)
    
    def insert_data(self, collection,data):
        collection1 = self.database[collection]
        collection1.insert_one(data)

    def replace_data(self, collection,data):
        #self.database.collection.drop()
        collection1 = self.database[collection]
        collection1.replace_one({'status' : 'running'},data)

    def update_status(self, collection,data):
        collection1 = self.database[collection]
        collection1.update_one({'status' : 'failed'},{ "$set": data })
        return()

    def show_data(self, collection):
        collection1 = self.database[collection]
        data = collection1.find_one()
        return(data)

