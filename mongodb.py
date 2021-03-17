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

    def insert_data(self, collection,data):
        collection1 = self.database[collection]
        collection1.insert_one(data)
        return()
    def show_data(self, collection):
        collection1 = self.database[collection]
        data = collection1.find_one()
        return(data)

