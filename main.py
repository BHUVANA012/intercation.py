import pymongo
client=pymongo.MongoClient()
mydb=client["mydb"]
mycol=mydb["IPL2022"]
data={'team':'royal challengers banglore','matches':'9','won':'5','lost':'4','points':'10'}
mycol.insert_one(data)
datalist=[{'team':'Gujurat Titans','matches':'8','won':'7','lost':'1','points':'14'},{'team':'rajasthan royals','matches':'8','won':'6','lost':'2','points':'12'},{'team':'lucknow super giants','matches':'9','won':'6','lost':'3','points':'12'}]
mycol.insert_many(datalist)
show=mycol.find_one()
print(show)
display=mycol.find({'name':'rojasthan royals'})
print(display)
#mycol.update_one({"team":"royal challengers banglore"},{"$set":{"matches":"10"}})
#mycol.delete_one({"team":"royal challengers banglore"}
#dropping
#mycol.drop()




